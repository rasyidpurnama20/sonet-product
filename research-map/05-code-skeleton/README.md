# FocalGNN - Code Skeleton

Implementation of FocalGNN: Physics-Informed Graph Attention Network for Earthquake Focal Mechanism Estimation.

## Project Structure

```
focalgnn/
├── config/
│   └── default.yaml          # Hyperparameters & experiment config
├── data/
│   ├── download_waveforms.py # FDSN waveform retrieval
│   ├── preprocess.py         # Filtering, windowing, normalization
│   ├── dataset.py            # PyTorch Dataset + PyG Data objects
│   └── graph_builder.py      # Physics-informed graph construction
├── models/
│   ├── encoder.py            # 1D ResNet per-station encoder
│   ├── gat_layers.py         # GATv2 with edge features
│   ├── readout.py            # Global attention pooling + prediction head
│   ├── focalgnn.py           # Full model assembly
│   └── baselines.py          # Baseline models (Single-CNN, Concat, Transformer)
├── losses/
│   ├── nll_loss.py           # Heteroscedastic NLL
│   ├── dc_constraint.py      # Double-couple regularization
│   └── polarity_loss.py      # Polarity consistency loss
├── training/
│   ├── train.py              # Main training loop
│   ├── evaluate.py           # Evaluation metrics (Kagan angle, calibration)
│   └── uncertainty.py        # MC Dropout inference
├── analysis/
│   ├── attention_viz.py      # Attention weights → focal sphere
│   ├── station_importance.py # Station contribution analysis
│   └── calibration_plot.py   # Reliability diagrams
├── utils/
│   ├── focal_mech.py         # MT ↔ strike/dip/rake conversion
│   ├── kagan_angle.py        # Kagan angle computation
│   └── geometry.py           # Azimuth, take-off angle utilities
├── scripts/
│   ├── run_experiment.sh     # Full experiment pipeline
│   ├── run_ablations.sh      # Ablation study automation
│   └── run_baselines.sh      # Baseline training
├── requirements.txt
└── setup.py
```

## Quick Start

```bash
# 1. Install
pip install -e .

# 2. Download data
python data/download_waveforms.py --catalog scsn_hash --years 2000-2022

# 3. Preprocess
python data/preprocess.py --input raw/ --output processed/

# 4. Train
python training/train.py --config config/default.yaml

# 5. Evaluate
python training/evaluate.py --checkpoint best_model.pt --test-data processed/test/

# 6. Analyze
python analysis/attention_viz.py --checkpoint best_model.pt --events sample_events.csv
```

## Dependencies

- Python >= 3.9
- PyTorch >= 2.0
- PyTorch Geometric >= 2.3
- ObsPy >= 1.4
- NumPy, SciPy, Pandas
- Matplotlib, Seaborn
- PyYAML
- Wandb (optional, for experiment tracking)
