# Dataset Guide: Relevant Datasets for FocalGNN

> **Purpose:** Comprehensive listing of datasets for training and evaluating GNN-based focal mechanism estimation  
> **Priority:** Ranked by relevance to FocalGNN project  
> **Date:** June 2025

---

## 1. PRIMARY DATASET (Training)

### 1.1 SCSN/SCEDC + HASH Focal Mechanism Catalog

| Field | Details |
|-------|---------|
| **Name** | Southern California Seismic Network (SCSN) + HASH Catalog |
| **Provider** | Southern California Earthquake Data Center (SCEDC), Caltech |
| **URL - Waveforms** | https://scedc.caltech.edu/data/waveform-access.html |
| **URL - FDSN** | `Client("SCEDC")` via ObsPy |
| **URL - Catalogs** | https://scedc.caltech.edu/data/alt-2011-dd-hauksson-yang-shearer.html |
| **URL - HASH** | https://scedc.caltech.edu/research-tools/alt-2011-yang-hauksson-shearer.html |
| **Coverage** | Southern California, 1981-present |
| **Events** | >500,000 relocated earthquakes (Hauksson, Yang, Shearer, 2012) |
| **Focal Mechanisms** | ~180,000 HASH solutions (Yang, Hauksson, Shearer, 2012) |
| **Magnitude Range** | M0.0 - M7.3 (Landers, Hector Mine, Ridgecrest) |
| **FM Quality** | A/B/C/D grades (A= best, ≥8 polarities, gap<90°) |
| **Waveform Format** | miniSEED via FDSN; continuous + event archives |
| **Stations** | ~400+ broadband/short-period stations |
| **Sampling Rate** | 100 Hz (HH channels), 20/40 Hz (BH), 100 Hz (EH) |
| **Components** | 3C (Z, N, E) |
| **Size Estimate** | ~5-10 TB raw continuous; ~200-500 GB for event waveforms |
| **License** | Open access (FDSN data policy) |

**Why PRIMARY:**
- Largest high-quality FM catalog in the world
- Dense station network → high-quality labels
- Consistent velocity model for take-off angle computation
- Used by Ross et al. (2018) as DL-FM benchmark

**Access Methods:**
```python
from obspy.clients.fdsn import Client
client = Client("SCEDC")

# Get waveforms
st = client.get_waveforms("CI", "PAS", "*", "BH?", starttime, endtime)

# Get events (catalog)
cat = client.get_events(starttime=t1, endtime=t2, minmag=2.0, 
                        minlat=32, maxlat=37, minlon=-121, maxlon=-115)
```

**Catalog Downloads (direct files):**
- Relocated catalog: `https://scedc.caltech.edu/data/alt-2011-dd-hauksson-yang-shearer.html`
- Focal mechanisms: search "Yang Hauksson Shearer 2012 focal mechanism catalog SCEDC"
- Alternative: SCEC Community Fault Model + stress data

---

### 1.2 SCEDC Event Waveform Archive (Pre-cut)

| Field | Details |
|-------|---------|
| **Name** | SCEDC Event Waveform Archive |
| **URL** | https://scedc.caltech.edu/data/stp-event.html |
| **Description** | Pre-cut event waveforms (P-arrival aligned) |
| **Format** | SAC or miniSEED |
| **Advantage** | No need to cut from continuous data |
| **Limitation** | May not cover all events in HASH catalog |

---

## 2. VALIDATION DATASETS (Cross-region testing)

### 2.1 INSTANCE (Italian Seismic Dataset for ML)

| Field | Details |
|-------|---------|
| **Name** | INSTANCE (Italian seismic dataset for machine learning) |
| **Provider** | INGV (Istituto Nazionale di Geofisica e Vulcanologia) |
| **Paper** | Michelini et al. (2021), Earth System Science Data |
| **URL** | https://doi.org/10.13127/instance |
| **GitHub** | https://github.com/INGV/instance |
| **Size** | ~50 GB (HDF5 format) |
| **Events** | ~1,160,000 3C waveforms + ~130,000 noise traces |
| **Stations** | Italian National Seismic Network (INSN, ~550 stations) |
| **Magnitude** | M0.0 - M6.5 |
| **Sampling Rate** | 100 Hz |
| **Duration** | 120 s per trace |
| **Focal Mechanisms** | YES - subset (~10,000+ events via TDMT catalog) |
| **FM Source** | INGV Time Domain Moment Tensor catalog |
| **Format** | HDF5 + CSV metadata |
| **License** | CC BY 4.0 |

**Why relevant:**
- Contains focal mechanism labels (TDMT solutions)
- Different network geometry from SCSN → tests generalization (Gap 4)
- Different tectonic regime (extensional + compressional)
- Ready-to-use ML format (HDF5)
- Well-documented metadata including station locations

**Access:**
```bash
# Download from INGV
wget https://doi.org/10.13127/instance
# or via direct INGV data portal
```

---

### 2.2 Global CMT Catalog + IRIS Waveforms

| Field | Details |
|-------|---------|
| **Name** | Global Centroid Moment Tensor (CMT) Catalog |
| **Provider** | Lamont-Doherty Earth Observatory, Columbia University |
| **URL - Catalog** | https://www.globalcmt.org/ |
| **URL - Waveforms** | IRIS DMC (https://ds.iris.edu/ds/) |
| **Coverage** | Global, 1976-present |
| **Events** | ~55,000+ moment tensor solutions |
| **Magnitude** | M≥5.0 (generally) |
| **FM Quality** | Full moment tensors (6 components), centroid parameters |
| **Format** | NDK format (catalog), miniSEED (waveforms via IRIS FDSN) |
| **License** | Open access |

**Why relevant:**
- Gold-standard moment tensor solutions (full waveform inversion)
- Global coverage → diverse mechanisms
- Larger events → higher SNR
- Can validate model on teleseismic distances
- Full moment tensor (not just DC) → can test non-DC component prediction

**Limitation:**
- Only M≥5 (small dataset)
- Teleseismic distances → different waveform character than regional SCSN

**Access:**
```python
# GCMT catalog
from obspy.clients.fdsn import Client
client = Client("GCMT")  # or download NDK files directly

# IRIS waveforms
client_iris = Client("IRIS")
st = client_iris.get_waveforms(...)
```

---

### 2.3 Japanese NIED F-net Moment Tensor Catalog

| Field | Details |
|-------|---------|
| **Name** | F-net Broadband Seismograph Network (NIED) |
| **Provider** | National Research Institute for Earth Science (NIED), Japan |
| **URL - Catalog** | https://www.fnet.bosai.go.jp/event/search.php?LANG=en |
| **URL - Waveforms** | https://www.fnet.bosai.go.jp/waveform/ |
| **Coverage** | Japan, 1997-present |
| **Events** | ~50,000+ moment tensor solutions |
| **Magnitude** | M≥3.0 |
| **Stations** | ~80 broadband stations (F-net) |
| **FM Quality** | Automated + reviewed MT solutions |
| **Format** | Custom format (catalog); SAC/miniSEED (waveforms) |
| **License** | Open for research (registration required) |

**Why relevant:**
- Dense network in highly seismic region
- Automated MT solutions → large catalog
- Subduction zone mechanisms (different from SCSN strike-slip)
- Good for testing model on thrust/normal fault mechanisms
- Moderate-sized events (M3+) with reliable solutions

---

## 3. BENCHMARK DATASETS (ML-ready)

### 3.1 STEAD (Stanford Earthquake Dataset)

| Field | Details |
|-------|---------|
| **Name** | STanford EArthquake Dataset (STEAD) |
| **Paper** | Mousavi et al. (2019), IEEE Access |
| **GitHub** | https://github.com/smousavi05/STEAD |
| **URL** | https://doi.org/10.7941/D76T22 (Stanford Digital Repository) |
| **Size** | ~70 GB (HDF5) |
| **Events** | ~1,050,000 earthquake waveforms + 100,000 noise |
| **Coverage** | Global (mainly US, Japan, New Zealand, Italy) |
| **Magnitude** | M-0.4 to M8.0 |
| **Sampling Rate** | 100 Hz |
| **Duration** | 60 s per trace |
| **Components** | 3C |
| **Labels** | P/S picks, distance, azimuth, magnitude, back_azimuth |
| **Focal Mechanisms** | NO (not included) |
| **Format** | HDF5 + CSV metadata |
| **License** | CC BY 4.0 |

**Why relevant:**
- Pre-training encoder (self-supervised or transfer learning)
- Noise traces for augmentation
- Azimuth/back-azimuth metadata available
- Industry-standard benchmark for seismic DL

**Limitation for FocalGNN:**
- NO focal mechanism labels
- Single-station traces (not multi-station per event)
- Must be used for pre-training only, not FM training

**Use case:** Pre-train CNN encoder on STEAD, then fine-tune on SCSN for FM estimation.

---

### 3.2 LEN-DB (Local Earthquake and Noise DataBase)

| Field | Details |
|-------|---------|
| **Name** | LEN-DB |
| **Paper** | Magrini et al. (2020), Artificial Intelligence in Geosciences |
| **URL** | https://doi.org/10.17632/7wv4j4bfn3 (Mendeley Data) |
| **Size** | ~3 GB |
| **Events** | ~200,000 waveforms (local Italian earthquakes) |
| **Components** | 3C |
| **Sampling Rate** | 100 Hz |
| **Duration** | Variable |
| **Focal Mechanisms** | No |
| **License** | CC BY 4.0 |

**Use case:** Additional noise traces; Italian waveform augmentation for INSTANCE validation.

---

### 3.3 DiTing Dataset (China)

| Field | Details |
|-------|---------|
| **Name** | DiTing: A large-scale Chinese seismic benchmark dataset |
| **Paper** | Zhao et al. (2023), Earthquake Science |
| **URL** | https://doi.org/10.12080/nedc.11.ds.d0001 |
| **Size** | ~230 GB |
| **Events** | ~2,700,000 3C waveforms (787,000 events) |
| **Coverage** | China, 2008-2019 |
| **Magnitude** | M0.0 - M7.1 |
| **Sampling Rate** | 50/100 Hz |
| **Labels** | P/S picks, first motion polarity, magnitude, distance |
| **Focal Mechanisms** | Partial (first-motion polarity available!) |
| **First-Motion Polarity** | YES (~350,000+ polarity picks) |
| **Format** | HDF5 |
| **License** | Research use |

**Why HIGHLY relevant:**
- Contains **first-motion polarity labels** → directly useful for FM training
- Massive scale (2.7M traces)
- Chinese seismic network = different geometry/tectonic regime
- Can augment polarity loss training even without full FM solutions

---

### 3.4 ETHZ/SED Swiss Seismic Dataset

| Field | Details |
|-------|---------|
| **Name** | Swiss Seismological Service (SED) Dataset |
| **Provider** | ETH Zurich |
| **Access** | FDSN via `Client("ETH")` in ObsPy |
| **Coverage** | Switzerland + surroundings |
| **Events** | ~15,000+ reviewed events/year |
| **FM** | Swiss MT catalog (available for M≥2.5) |
| **Stations** | ~200+ stations |

**Use case:** Additional cross-region validation with European Alpine tectonics.

---

## 4. SUPPLEMENTARY DATA SOURCES

### 4.1 USGS ComCat (Comprehensive Earthquake Catalog)

| Field | Details |
|-------|---------|
| **URL** | https://earthquake.usgs.gov/data/comcat/ |
| **API** | https://earthquake.usgs.gov/fdsnws/event/1/ |
| **Focal Mechanisms** | YES - USGS moment tensors for M≥4.5 globally |
| **Format** | QuakeML via FDSN |

```python
from obspy.clients.fdsn import Client
client = Client("USGS")
cat = client.get_events(starttime=t1, endtime=t2, 
                        minmag=4.5, includeallmagnitudes=True)
```

---

### 4.2 ISC Bulletin (International Seismological Centre)

| Field | Details |
|-------|---------|
| **URL** | https://www.isc.ac.uk/iscbulletin/ |
| **Coverage** | Global, reviewed bulletin |
| **FM** | ISC focal mechanism database (collected from multiple agencies) |
| **Polarities** | First-motion polarity picks from ISC analysts |
| **Format** | ISF format, QuakeML |

**Why relevant:** Largest collection of polarity picks globally. Can be used for polarity loss training data.

---

### 4.3 IRIS Searchable Product Depository (SPUD) - Moment Tensors

| Field | Details |
|-------|---------|
| **URL** | http://ds.iris.edu/spud/momenttensor |
| **Content** | Aggregated moment tensors from multiple agencies |
| **Coverage** | Global, M≥4.0 |
| **Sources** | GCMT, USGS, NIED, GFZ, etc. |

---

### 4.4 SCEDC Phase Pick Catalog (Polarity)

| Field | Details |
|-------|---------|
| **URL** | https://scedc.caltech.edu/data/phase-picks.html |
| **Content** | Analyst-reviewed P picks with polarity (U/D) |
| **Events** | >5 million polarity picks for SCSN events |
| **Format** | CSV/phase format |

**Critical for FocalGNN:** These polarity picks are what HASH uses to determine mechanisms. Having raw polarities allows:
1. Training polarity consistency loss
2. Comparing FocalGNN polarity predictions vs. analyst picks
3. Augmenting with events that have polarities but no HASH solution

---

## 5. SYNTHETIC DATA (Augmentation)

### 5.1 Generating Synthetic Training Data

For data augmentation or pre-training, synthetic waveforms can be generated:

| Method | Tool | Use |
|--------|------|-----|
| Full waveform simulation | Instaseis / AxiSEM | Realistic broadband synthetics |
| 1D Green's functions | fk (Zhu & Rivera) | Fast synthetic seismograms |
| Ray-based synthetics | ObsPy TauP + radiation pattern | Polarity + amplitude |
| Noise + synthetic | STEAD noise + synthetic signal | Augmented training data |

**Instaseis approach:**
```python
import instaseis
db = instaseis.open_db("syngine://ak135f_5s")
receiver = instaseis.Receiver(latitude=34.0, longitude=-118.0)
source = instaseis.Source.from_strike_dip_rake(
    latitude=34.5, longitude=-117.5, depth_in_m=10000,
    strike=45, dip=60, rake=-90, M0=1e15)
st = db.get_seismograms(source=source, receiver=receiver)
```

**Advantages of synthetic augmentation:**
- Perfect labels (known mechanism)
- Control over noise level, distance, network geometry
- Generate rare mechanisms (uncommon in SCSN)
- Pre-train before fine-tuning on real data

---

## 6. DATASET COMPARISON MATRIX

| Dataset | Region | FM Labels | Size | ML-Ready | Free | Priority |
|---------|--------|-----------|------|----------|------|----------|
| **SCSN + HASH** | S. California | ~180K solutions | ~500 GB | Needs processing | Yes | **#1 (TRAIN)** |
| **INSTANCE** | Italy | ~10K MT solutions | 50 GB | HDF5 ready | Yes | **#2 (VALIDATE)** |
| **DiTing** | China | Polarity (~350K) | 230 GB | HDF5 ready | Yes | **#3 (POLARITY)** |
| **Global CMT** | Global | ~55K full MT | Via IRIS | Needs download | Yes | #4 (teleseismic) |
| **F-net (NIED)** | Japan | ~50K MT | Needs download | Registration | Free | #5 (subduction) |
| **STEAD** | Global | None (picks only) | 70 GB | HDF5 ready | Yes | #6 (pre-train) |
| **USGS ComCat** | Global | M≥4.5 MT | Small | API ready | Yes | #7 (supplement) |
| **ISC** | Global | Polarities + FM | Large | ISF format | Yes | #8 (polarities) |
| **Swiss SED** | Switzerland | M≥2.5 MT | Moderate | Via FDSN | Yes | #9 (validation) |

---

## 7. RECOMMENDED DATA PIPELINE

### Phase 1: Minimum Viable Dataset (Week 1)

```bash
# 1. Download SCSN HASH catalog
wget [SCEDC_HASH_URL]  # ~100 MB

# 2. Filter quality A/B, M2.0-5.5 → ~80-100K events

# 3. Download waveforms via ObsPy FDSN (parallelized)
python focalgnn/data/download_waveforms.py \
    --hash-file scsn_hash_catalog.txt \
    --years 2000-2022 \
    --output data/processed/scsn_focalgnn.h5 \
    --workers 8

# Expected: 2-5 days download time for ~80K events
```

### Phase 2: Cross-Region Validation

```bash
# Download INSTANCE (pre-packaged HDF5)
wget https://doi.org/10.13127/instance  # ~50 GB

# Extract events with FM labels only
python scripts/extract_instance_fm.py \
    --input instance_events.hdf5 \
    --mt-catalog ingv_tdmt.csv \
    --output data/processed/instance_fm.h5
```

### Phase 3: Polarity Augmentation (Optional)

```bash
# Download DiTing polarity subset
python scripts/download_diting_polarity.py \
    --output data/processed/diting_polarity.h5
```

---

## 8. DATA BUDGET & STORAGE

| Dataset | Storage Needed | Download Time (est.) |
|---------|---------------|---------------------|
| SCSN waveforms (80K events) | ~200-500 GB | 3-5 days |
| INSTANCE | ~50 GB | 4-8 hours |
| DiTing (polarity subset) | ~50 GB | 4-8 hours |
| STEAD (for pre-training) | ~70 GB | 6-10 hours |
| **Total** | **~400-700 GB** | **~1 week** |

**Minimum viable:** SCSN + INSTANCE = ~300 GB, sufficient for paper.

---

## 9. IMPORTANT NOTES

### Access Requirements:
- **SCEDC:** No registration needed. Free FDSN access.
- **INSTANCE:** Direct download. CC BY 4.0.
- **NIED F-net:** Registration required (https://www.fnet.bosai.go.jp/)
- **DiTing:** Available from National Earthquake Data Center of China.
- **IRIS:** No registration for data access.

### Citation Requirements:
If you use these datasets, cite:
- SCSN/HASH: Hauksson et al. (2012), Yang et al. (2012)
- INSTANCE: Michelini et al. (2021)
- STEAD: Mousavi et al. (2019)
- DiTing: Zhao et al. (2023)
- GCMT: Ekström et al. (2012)

### Data Quality Considerations:
- HASH quality A: ≥8 first-motion polarities, azimuthal gap <90°, both acceptable planes within 35°
- HASH quality B: ≥8 polarities, gap <90°, acceptable but less stable
- Filter out quality C/D for training (unreliable labels = noisy supervision)
- Consider weighting loss by quality grade (A > B)

---

*This document provides all dataset information needed to start the FocalGNN data pipeline immediately.*
