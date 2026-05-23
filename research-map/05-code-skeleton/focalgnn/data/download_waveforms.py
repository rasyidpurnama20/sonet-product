"""
Data acquisition pipeline for FocalGNN.
Downloads waveforms from SCEDC/FDSN and prepares HASH focal mechanism labels.

Usage:
    python download_waveforms.py --catalog scsn_hash --years 2000-2022 --output data/raw/
    
Requirements:
    - ObsPy (for FDSN client and waveform processing)
    - Internet access to SCEDC FDSN web services
    
Pipeline:
    1. Download HASH focal mechanism catalog from SCSN
    2. Filter events by magnitude, quality, station count
    3. Download 3C waveforms for each event-station pair
    4. Compute source-station geometry (azimuth, take-off angle)
    5. Package into HDF5 for training
"""

import os
import argparse
import numpy as np
import pandas as pd
import h5py
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

try:
    from obspy import UTCDateTime, read_inventory
    from obspy.clients.fdsn import Client
    from obspy.taup import TauPyModel
    from obspy.geodetics import gps2dist_azimuth, kilometers2degrees
except ImportError:
    raise ImportError("ObsPy is required. Install with: pip install obspy")


# Configuration
SCEDC_CLIENT = "SCEDC"
VELOCITY_MODEL = "iasp91"  # or custom SoCal model
SAMPLING_RATE = 100.0  # Hz
WINDOW_BEFORE_P = 1.0  # seconds before P
WINDOW_AFTER_P = 9.0   # seconds after P
FILTER_BAND = (1.0, 20.0)  # Hz bandpass


class WaveformDownloader:
    """
    Downloads and preprocesses seismic waveforms for FocalGNN training.
    """

    def __init__(
        self,
        client_name: str = SCEDC_CLIENT,
        velocity_model: str = VELOCITY_MODEL,
        output_dir: str = "data/raw",
    ):
        self.client = Client(client_name)
        self.taup_model = TauPyModel(model=velocity_model)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def download_catalog(
        self,
        starttime: str = "2000-01-01",
        endtime: str = "2022-12-31",
        minmagnitude: float = 2.0,
        maxmagnitude: float = 5.5,
        minlatitude: float = 32.0,
        maxlatitude: float = 37.0,
        minlongitude: float = -121.0,
        maxlongitude: float = -115.0,
    ) -> pd.DataFrame:
        """
        Download earthquake catalog from SCEDC.
        
        Returns DataFrame with columns:
            event_id, origin_time, lat, lon, depth, magnitude
        """
        print(f"Downloading catalog: {starttime} to {endtime}, M{minmagnitude}-{maxmagnitude}")
        
        cat = self.client.get_events(
            starttime=UTCDateTime(starttime),
            endtime=UTCDateTime(endtime),
            minmagnitude=minmagnitude,
            maxmagnitude=maxmagnitude,
            minlatitude=minlatitude,
            maxlatitude=maxlatitude,
            minlongitude=minlongitude,
            maxlongitude=maxlongitude,
        )
        
        events = []
        for event in cat:
            origin = event.preferred_origin() or event.origins[0]
            mag = event.preferred_magnitude() or event.magnitudes[0]
            
            events.append({
                'event_id': str(event.resource_id).split('/')[-1],
                'origin_time': str(origin.time),
                'latitude': origin.latitude,
                'longitude': origin.longitude,
                'depth_km': origin.depth / 1000.0,
                'magnitude': mag.mag,
            })
        
        df = pd.DataFrame(events)
        print(f"  Retrieved {len(df)} events")
        return df

    def load_hash_catalog(self, hash_file: str) -> pd.DataFrame:
        """
        Load HASH focal mechanism catalog.
        
        Expected format (SCSN HASH output):
            event_id, strike, dip, rake, quality, num_polarities, azimuthal_gap, ...
        
        Args:
            hash_file: path to HASH catalog file
        Returns:
            DataFrame with focal mechanism parameters
        """
        # HASH catalog format varies - adapt to specific file format
        # This is a placeholder for the actual parsing logic
        print(f"Loading HASH catalog: {hash_file}")
        
        # Common HASH output columns
        df = pd.read_csv(hash_file, comment='#', sep=r'\s+', names=[
            'event_id', 'year', 'month', 'day', 'hour', 'min', 'sec',
            'lat', 'lon', 'depth', 'mag',
            'strike1', 'dip1', 'rake1',
            'strike2', 'dip2', 'rake2',
            'num_pol', 'az_gap', 'quality',
        ])
        
        # Filter by quality
        df = df[df['quality'].isin(['A', 'B'])]
        print(f"  {len(df)} events with quality A/B")
        
        return df

    def compute_geometry(
        self,
        event_lat: float,
        event_lon: float,
        event_depth_km: float,
        station_lat: float,
        station_lon: float,
    ) -> dict:
        """
        Compute source-station geometry: azimuth, take-off angle, distance.
        
        Args:
            event_lat, event_lon, event_depth_km: event location
            station_lat, station_lon: station location
        Returns:
            dict with azimuth, takeoff_angle, distance_km, and circular encodings
        """
        # Geodetic distance and azimuth
        dist_m, az, baz = gps2dist_azimuth(event_lat, event_lon, station_lat, station_lon)
        dist_km = dist_m / 1000.0
        dist_deg = kilometers2degrees(dist_km)
        
        # Take-off angle from TauP
        try:
            arrivals = self.taup_model.get_travel_times(
                source_depth_in_km=event_depth_km,
                distance_in_degree=dist_deg,
                phase_list=['p', 'P'],
            )
            if arrivals:
                takeoff_angle = arrivals[0].takeoff_angle
            else:
                takeoff_angle = 90.0  # fallback
        except Exception:
            takeoff_angle = 90.0  # fallback
        
        # Circular encodings for neural network input
        az_rad = np.radians(az)
        to_rad = np.radians(takeoff_angle)
        
        return {
            'azimuth': az,
            'takeoff_angle': takeoff_angle,
            'distance_km': dist_km,
            'cos_azimuth': np.cos(az_rad),
            'sin_azimuth': np.sin(az_rad),
            'cos_takeoff': np.cos(to_rad),
            'sin_takeoff': np.sin(to_rad),
        }

    def download_event_waveforms(
        self,
        event_id: str,
        origin_time: str,
        event_lat: float,
        event_lon: float,
        event_depth_km: float,
        max_distance_deg: float = 2.0,
    ) -> dict:
        """
        Download waveforms for a single event from all nearby stations.
        
        Args:
            event_id: unique event identifier
            origin_time: event origin time (UTC string)
            event_lat, event_lon, event_depth_km: event location
            max_distance_deg: maximum station distance (degrees)
        Returns:
            dict with 'waveforms', 'geometry', 'stations', or None if failed
        """
        t0 = UTCDateTime(origin_time)
        
        try:
            # Get available stations
            inventory = self.client.get_stations(
                starttime=t0 - 60,
                endtime=t0 + 60,
                latitude=event_lat,
                longitude=event_lon,
                maxradius=max_distance_deg,
                channel="BH?,HH?",  # broadband
                level="channel",
            )
        except Exception as e:
            return None

        waveforms = []
        geometries = []
        station_ids = []

        for network in inventory:
            for station in network:
                # Get P arrival time
                geo = self.compute_geometry(
                    event_lat, event_lon, event_depth_km,
                    station.latitude, station.longitude
                )
                
                # Estimate P arrival time
                try:
                    arrivals = self.taup_model.get_travel_times(
                        source_depth_in_km=event_depth_km,
                        distance_in_degree=kilometers2degrees(geo['distance_km']),
                        phase_list=['p', 'P'],
                    )
                    if not arrivals:
                        continue
                    p_time = t0 + arrivals[0].time
                except Exception:
                    continue

                # Download waveform
                try:
                    st = self.client.get_waveforms(
                        network=network.code,
                        station=station.code,
                        location="*",
                        channel="BH?,HH?",
                        starttime=p_time - WINDOW_BEFORE_P,
                        endtime=p_time + WINDOW_AFTER_P,
                    )
                except Exception:
                    continue

                # Process waveform
                wf = self._process_waveform(st)
                if wf is not None:
                    waveforms.append(wf)
                    geometries.append([
                        geo['azimuth'],
                        geo['takeoff_angle'],
                        geo['distance_km'],
                        geo['cos_azimuth'],
                        geo['sin_azimuth'],
                        geo['cos_takeoff'],
                        geo['sin_takeoff'],
                    ])
                    station_ids.append(f"{network.code}.{station.code}")

        if len(waveforms) < 5:  # minimum stations
            return None

        return {
            'waveforms': np.array(waveforms),      # (N, 3, T)
            'geometry': np.array(geometries),      # (N, 7)
            'stations': station_ids,
        }

    def _process_waveform(self, stream):
        """
        Process ObsPy Stream to standardized numpy array.
        
        Steps:
            1. Merge and fill gaps
            2. Remove instrument response (to velocity)
            3. Bandpass filter
            4. Resample to target rate
            5. Extract 3C array
            6. Normalize
        
        Returns:
            wf: (3, T) numpy array or None if processing fails
        """
        try:
            # Need exactly 3 components
            stream.merge(fill_value=0)
            
            if len(stream) < 3:
                return None
            
            # Select 3 components (Z, N, E or Z, 1, 2)
            stream = stream.select(channel="??Z") + \
                     stream.select(channel="??N") + \
                     stream.select(channel="??E")
            
            if len(stream) < 3:
                stream_orig = stream.copy()
                stream = stream_orig.select(channel="??Z") + \
                         stream_orig.select(channel="??1") + \
                         stream_orig.select(channel="??2")
            
            if len(stream) < 3:
                return None
            
            # Take first 3 traces
            stream = stream[:3]
            
            # Remove response (deconvolve to velocity)
            # stream.remove_response(output="VEL")  # requires inventory attachment
            
            # Bandpass filter
            stream.filter('bandpass', freqmin=FILTER_BAND[0], freqmax=FILTER_BAND[1])
            
            # Resample
            stream.resample(SAMPLING_RATE)
            
            # Extract as numpy array
            target_samples = int((WINDOW_BEFORE_P + WINDOW_AFTER_P) * SAMPLING_RATE)
            wf = np.zeros((3, target_samples))
            
            for i, tr in enumerate(stream[:3]):
                data = tr.data[:target_samples]
                wf[i, :len(data)] = data
            
            # Joint 3C normalization (preserve relative amplitudes + polarity)
            max_val = np.max(np.abs(wf))
            if max_val > 0:
                wf = wf / max_val
            else:
                return None
            
            # SNR check (simple)
            noise_window = wf[:, :int(WINDOW_BEFORE_P * SAMPLING_RATE)]
            signal_window = wf[:, int(WINDOW_BEFORE_P * SAMPLING_RATE):]
            
            noise_rms = np.sqrt(np.mean(noise_window ** 2))
            signal_rms = np.sqrt(np.mean(signal_window[:, :int(2 * SAMPLING_RATE)] ** 2))
            
            if noise_rms > 0:
                snr = signal_rms / noise_rms
                if snr < 3.0:
                    return None
            
            return wf
            
        except Exception:
            return None

    def build_hdf5(
        self,
        events_df: pd.DataFrame,
        hash_df: pd.DataFrame,
        output_path: str = "data/processed/focalgnn_data.h5",
        max_workers: int = 4,
    ):
        """
        Download all waveforms and package into HDF5.
        
        HDF5 Structure:
            /train/
                /event_001/
                    waveforms: (N, 3, T)
                    geometry: (N, 7)
                    moment_tensor: (6,)
                    polarities: (N,)
                /event_002/
                    ...
            /val/
                ...
            /test/
                ...
        """
        from focalgnn.utils.focal_mech import sdr_to_mt6
        
        # Merge events with HASH focal mechanisms
        merged = events_df.merge(hash_df, on='event_id', how='inner')
        print(f"Events with focal mechanisms: {len(merged)}")
        
        # Temporal split
        merged['year'] = pd.to_datetime(merged['origin_time']).dt.year
        train_mask = merged['year'] <= 2018
        val_mask = (merged['year'] >= 2019) & (merged['year'] <= 2020)
        test_mask = merged['year'] >= 2021
        
        splits = {
            'train': merged[train_mask],
            'val': merged[val_mask],
            'test': merged[test_mask],
        }
        
        for split_name, split_df in splits.items():
            print(f"  {split_name}: {len(split_df)} events")
        
        # Create HDF5
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with h5py.File(output_path, 'w') as f:
            for split_name, split_df in splits.items():
                split_group = f.create_group(split_name)
                
                success_count = 0
                for idx, row in tqdm(split_df.iterrows(), total=len(split_df),
                                     desc=f"Downloading {split_name}"):
                    
                    # Download waveforms
                    result = self.download_event_waveforms(
                        event_id=row['event_id'],
                        origin_time=row['origin_time'],
                        event_lat=row['latitude'],
                        event_lon=row['longitude'],
                        event_depth_km=row['depth_km'],
                    )
                    
                    if result is None:
                        continue
                    
                    # Convert strike/dip/rake to moment tensor
                    mt6 = sdr_to_mt6(row['strike1'], row['dip1'], row['rake1'])
                    
                    # Store in HDF5
                    event_group = split_group.create_group(row['event_id'])
                    event_group.create_dataset('waveforms', data=result['waveforms'],
                                              compression='gzip')
                    event_group.create_dataset('geometry', data=result['geometry'])
                    event_group.create_dataset('moment_tensor', data=mt6)
                    
                    # Metadata
                    event_group.attrs['magnitude'] = row['magnitude']
                    event_group.attrs['depth_km'] = row['depth_km']
                    event_group.attrs['latitude'] = row['latitude']
                    event_group.attrs['longitude'] = row['longitude']
                    event_group.attrs['num_stations'] = result['waveforms'].shape[0]
                    event_group.attrs['strike'] = row['strike1']
                    event_group.attrs['dip'] = row['dip1']
                    event_group.attrs['rake'] = row['rake1']
                    
                    success_count += 1
                
                print(f"  {split_name}: {success_count}/{len(split_df)} events successful")
        
        print(f"\nHDF5 saved: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Download waveforms for FocalGNN")
    parser.add_argument('--catalog', type=str, default='scsn_hash',
                        help='Catalog source')
    parser.add_argument('--hash-file', type=str, default=None,
                        help='Path to HASH focal mechanism catalog file')
    parser.add_argument('--years', type=str, default='2000-2022',
                        help='Year range (e.g., 2000-2022)')
    parser.add_argument('--output', type=str, default='data/processed/focalgnn_data.h5',
                        help='Output HDF5 path')
    parser.add_argument('--min-mag', type=float, default=2.0)
    parser.add_argument('--max-mag', type=float, default=5.5)
    parser.add_argument('--workers', type=int, default=4)
    args = parser.parse_args()
    
    # Parse years
    start_year, end_year = args.years.split('-')
    
    # Initialize downloader
    downloader = WaveformDownloader(output_dir='data/raw')
    
    # Step 1: Download event catalog
    events_df = downloader.download_catalog(
        starttime=f"{start_year}-01-01",
        endtime=f"{end_year}-12-31",
        minmagnitude=args.min_mag,
        maxmagnitude=args.max_mag,
    )
    
    # Step 2: Load HASH focal mechanisms
    if args.hash_file:
        hash_df = downloader.load_hash_catalog(args.hash_file)
    else:
        print("WARNING: No HASH file provided. Using catalog events without FM labels.")
        print("  For training, you need the SCSN HASH catalog.")
        print("  Download from: https://service.scedc.caltech.edu/ftp/catalogs/SCEC_DC/")
        return
    
    # Step 3: Build HDF5
    downloader.build_hdf5(
        events_df=events_df,
        hash_df=hash_df,
        output_path=args.output,
        max_workers=args.workers,
    )


if __name__ == '__main__':
    main()
