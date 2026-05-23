# Domain Map: Earthquake Focal Mechanism Estimation via Deep Learning & Graph Neural Networks

> **Author context:** PhD-level researcher with prior experience in seismic phase picking using CNN-based deep learning.  
> **Goal:** Identify a publishable Q1-target research gap within the intersection of focal mechanism determination and GNN-based deep learning.  
> **Date:** June 2025

---

## 1. Taxonomy of the Subfield

```
Earthquake Deep Learning
├── 1. Seismic Signal Processing
│   ├── 1.1 Phase Picking (P/S arrival)
│   │   ├── CNN-based (PhaseNet, EQTransformer)
│   │   ├── RNN/Transformer-based
│   │   └── GNN-based (station-graph picking)
│   ├── 1.2 Event Detection & Association
│   │   ├── Single-station detection
│   │   ├── Multi-station association (GaMMA, GENIE)
│   │   └── Graph-based event association
│   └── 1.3 Denoising & Signal Enhancement
│       ├── Autoencoder-based
│       └── GAN-based denoising
│
├── 2. Source Parameter Estimation
│   ├── 2.1 Focal Mechanism / Moment Tensor
│   │   ├── First-motion polarity classification (DL)
│   │   ├── Full waveform inversion with DL surrogates
│   │   ├── GNN for station-network focal mechanism
│   │   ├── Bayesian / uncertainty-aware approaches
│   │   └── Hybrid physics-informed neural networks
│   ├── 2.2 Magnitude Estimation
│   │   ├── Single-station ML/DL
│   │   └── Network-level aggregation (GNN)
│   └── 2.3 Hypocenter / Location
│       ├── Travel-time based DL
│       ├── Waveform-based (end-to-end)
│       └── Graph-based location (station graph)
│
├── 3. Earthquake Prediction / Forecasting
│   ├── 3.1 Aftershock prediction
│   ├── 3.2 Spatio-temporal forecasting (ETAS + DL)
│   └── 3.3 Early warning systems (DL-enhanced)
│
├── 4. Graph Neural Networks in Seismology
│   ├── 4.1 Station-network as graph
│   │   ├── Spatial graph (station geometry)
│   │   ├── Spatio-temporal graph (dynamic edges)
│   │   └── Heterogeneous graph (station + event nodes)
│   ├── 4.2 GNN architectures applied
│   │   ├── GCN (spectral / spatial)
│   │   ├── GAT (attention-based)
│   │   ├── GraphSAGE
│   │   └── Message-passing neural networks (MPNN)
│   └── 4.3 Graph construction strategies
│       ├── k-NN spatial graph
│       ├── Delaunay triangulation
│       ├── Fully connected + learned attention
│       └── Physics-informed edges (ray-path, velocity model)
│
└── 5. Foundation Models & Transfer Learning
    ├── 5.1 Pre-trained seismic encoders
    ├── 5.2 Self-supervised learning on waveforms
    └── 5.3 Cross-region / cross-network transfer
```

---

## 2. Top Venues (Conferences + Journals)

| # | Venue | Type | Ranking / Metric | Notes |
|---|-------|------|------------------|-------|
| 1 | **Geophysical Research Letters (GRL)** | Journal | Q1 (Scimago), h5-index ~120 | High-impact, letter format, fast turnaround |
| 2 | **Journal of Geophysical Research: Solid Earth (JGR-SE)** | Journal | Q1 (Scimago), h5-index ~85 | Full-length papers, strong seismology coverage |
| 3 | **Seismological Research Letters (SRL)** | Journal | Q1 (Scimago), h5-index ~55 | Active in ML-seismology, e-supplements |
| 4 | **Bulletin of the Seismological Society of America (BSSA)** | Journal | Q1 (Scimago), h5-index ~45 | Classical seismology + emerging DL papers |
| 5 | **Geophysical Journal International (GJI)** | Journal | Q1 (Scimago), h5-index ~60 | Strong European community presence |
| 6 | **Nature Communications / Communications Earth & Environment** | Journal | Q1, h5-index ~300 / ~30 | High visibility for methodological breakthroughs |
| 7 | **NeurIPS / ICML (AI4Science workshops)** | Conference | CORE A*, h5-index ~250+ | For methodological ML contribution |
| 8 | **AGU Fall Meeting / EGU General Assembly** | Conference | Premier geoscience conferences | Presentation + fast abstract, networking |

---

## 3. Active Labs & Researchers

| # | Researcher | Affiliation | Focus Area |
|---|-----------|-------------|------------|
| 1 | **Zachary E. Ross** | Caltech | DL for seismology (PhaseNet co-contributor, GNN event association, focal mechanisms) |
| 2 | **Weiqiang Zhu** | UC Berkeley / formerly Stanford | PhaseNet, EQCCT, GNN-based seismic methods |
| 3 | **S. Mostafa Mousavi** | Stanford / Google | EQTransformer, STEAD dataset, DL seismology |
| 4 | **Men-Andrin Meier** | Caltech / ETH Zurich | Early warning, DL source characterization |
| 5 | **Jannes Münchmeyer** | GFZ Potsdam / Universitat Potsdam | GNN for seismology, Bayesian source estimation, TEAM framework |
| 6 | **Ian McBrearty** | Stanford | ML focal mechanisms, moment tensors |
| 7 | **Qingkai Kong** | Berkeley Seismological Lab | ML seismology, MyShake, transfer learning |
| 8 | **Martijn van den Ende** | Universite Cote d'Azur | Graph-based seismology, fiber optics + DL |
| 9 | **Dmitry Kuznetsov** | ETH Zurich [VERIFY] | GNN-based seismic monitoring |
| 10 | **Daniel Trugman** | University of Nevada, Reno | Source parameter estimation, stress drops, ML |

---

## 4. Three Hot Themes (2022-2025)

### Theme 1: GNN-Based Multi-Station Seismic Processing
Graph neural networks that model seismic station networks as graphs for tasks ranging from phase association to source characterization. The key insight is that inter-station relationships (distance, azimuthal coverage, coherence) carry critical information that traditional single-station DL ignores.

**Representative work:** GENIE (Ross et al.), GNN-based earthquake location, graph attention for event association.

### Theme 2: Uncertainty-Aware / Bayesian Deep Learning for Source Parameters
Moving beyond point estimates to full posterior distributions for focal mechanisms and moment tensors. This includes Bayesian neural networks, mixture density networks, and Monte Carlo dropout applied to source inversion problems.

**Representative work:** Munzmeyer et al. Bayesian earthquake location, probabilistic focal mechanism with DL.

### Theme 3: Foundation Models & Self-Supervised Pre-training for Seismology
Large-scale pre-trained models on massive waveform datasets (STEAD, INSTANCE) that can be fine-tuned for downstream tasks. Inspired by success of BERT/GPT paradigm in NLP, applied to continuous seismic data.

**Representative work:** Seismic foundation model efforts, contrastive learning for waveform embeddings.

---

## 5. Blind Spots / Under-Explored Areas

### Blind Spot 1: GNN-Based Focal Mechanism Determination with Explicit Graph Structure Learning
Most focal mechanism studies use single-station or simple concatenation of multi-station data. Very few works explicitly model the **station network as a graph** where the graph topology itself (azimuthal coverage, distance distribution, take-off angle geometry) is learned or optimized for focal mechanism inversion. This is a natural fit because:
- Focal mechanism solutions depend critically on azimuthal station distribution
- Graph attention can learn which station pairs/triplets carry the most discriminative information
- The polarity pattern on the focal sphere is inherently a geometric/graph problem

**Opportunity:** Design a GNN that takes station waveforms as node features, with edges encoding spatial/geometric relationships, and outputs full focal mechanism parameters (strike/dip/rake or moment tensor components) with uncertainty estimates.

### Blind Spot 2: Physics-Informed Graph Construction for Seismological GNNs
Current GNN approaches in seismology typically use simple k-NN or distance-based graphs. There is limited work on constructing graph edges based on **seismic physics** (e.g., ray-path connectivity through velocity models, shared sensitivity kernels, wavefield coherence). Incorporating physics into the graph structure could dramatically improve data efficiency and generalization.

### Blind Spot 3: Low-Data / Few-Shot Focal Mechanism Estimation for Under-Instrumented Regions
Most DL focal mechanism studies train on well-recorded catalogs (e.g., Southern California). Transferring these models to sparse networks (e.g., Indonesia, developing nations) with few labeled focal mechanisms remains largely unexplored. GNN architectures could be particularly suited here because they can naturally handle variable network configurations.

---

## 6. Anchor Papers (Read in Full)

> Papers are selected for their foundational role, methodological innovation, or direct relevance to GNN + focal mechanism research. All from Q1 venues or highly influential.

| # | Title | Authors | Venue | Year |
|---|-------|---------|-------|------|
| 1 | "PhaseNet: A Deep-Neural-Network-Based Seismic Arrival Time Picking Method" | Zhu, W. & Beroza, G.C. | Geophysical Journal International | 2019 |
| 2 | "Earthquake transformer - an attentive deep-learning model for simultaneous earthquake detection and phase picking" | Mousavi, S.M., Ellsworth, W.L., Zhu, W., Chuber, L.Y., Beroza, G.C. | Nature Communications | 2020 |
| 3 | "GENIE: Graph-based Earthquake Neural Interpretable Estimator" [VERIFY exact title] | Ross, Z.E. et al. | Geophysical Research Letters or JGR | 2022 [VERIFY year] |
| 4 | "Earthquake Phase Association with Graph Neural Networks" | McBrearty, I.W. & Beroza, G.C. | Bulletin of the Seismological Society of America | 2023 [VERIFY] |
| 5 | "The Transformer Earthquake Alerting Model: A new versatile approach to earthquake early warning" | Munchmeyer, J., Bindi, D., Leser, U., Tilmann, F. | Geophysical Journal International | 2021 |
| 6 | "Which Picker Fits My Data? A Quantitative Evaluation of Deep Learning Based Seismic Pickers" | Munchmeyer, J. et al. | Journal of Geophysical Research: Solid Earth | 2022 |
| 7 | "Rapid Bayesian earthquake source inversion with deep learning" [VERIFY exact title] | Munchmeyer, J. et al. | Geophysical Research Letters | 2022 [VERIFY] |
| 8 | "Earthquake Focal Mechanisms from Deep Learning" [VERIFY exact title] | Ross, Z.E., Meier, M.-A., Hauksson, E. | Geophysical Research Letters | 2018 [VERIFY] |
| 9 | "Machine Learning Aspects of the MyShake Global Smartphone Seismic Network" | Kong, Q. et al. | Seismological Research Letters | 2019 [VERIFY] |
| 10 | "STanford EArthquake Dataset (STEAD): A Global Data Set of Seismic Signals for AI" | Mousavi, S.M. et al. | IEEE Access | 2019 |
| 11 | "Deep learning for multi-station seismic waveform-based earthquake magnitude estimation" [VERIFY exact title] | Mousavi, S.M. | Geophysical Research Letters | 2020 [VERIFY] |
| 12 | "GaMMA: Earthquake Phase Association with Backprojection and Graph Neural Networks" [VERIFY exact title] | Zhu, W. et al. | Journal of Geophysical Research: Solid Earth | 2022 [VERIFY] |
| 13 | "INSTANCE - the Italian seismic dataset for machine learning" | Michelini, A. et al. | Earth System Science Data | 2021 |
| 14 | "Focal Mechanism Determination by Deep Learning: A Preliminary Study" [VERIFY exact title] | Kuang, W. et al. | Geophysical Research Letters or BSSA | 2021 [VERIFY] |
| 15 | "Graph Neural Networks for Earthquake Early Warning" [VERIFY exact title] | Various (check specific authors) | GRL or SRL | 2023 [VERIFY] |
| 16 | "Earthquake location and magnitude estimation with graph neural networks" [VERIFY exact title] | van den Ende, M. et al. or Munchmeyer, J. et al. | GJI or JGR | 2022-2023 [VERIFY] |

---

## 7. Suggested Research Direction (Quick Take)

Given your constraints (compute, data, time = 1 month target) and background (CNN picking experience), the highest-value gap is:

**"GNN-based focal mechanism estimation using station-network graph with learned attention and uncertainty quantification"**

Why this works for you:
- **Builds on your expertise:** You already understand waveform processing with DL
- **Novel combination:** GNN + focal mechanism is barely explored
- **Data available:** Southern California catalog (SCSN) has abundant focal mechanisms for training
- **Compute-friendly:** GNNs are generally lightweight compared to large transformers
- **Clear contribution:** Modeling azimuthal coverage and station geometry as graph structure is physically motivated and novel
- **Publishable framing:** "We show that explicit graph modeling of station geometry improves focal mechanism accuracy, especially for events with sparse/poor azimuthal coverage"

### Concrete 1-Month Plan Sketch:
1. **Week 1:** Literature deep-dive on anchor papers, dataset preparation (SCSN waveforms + HASH focal mechanisms)
2. **Week 2:** Implement baseline (CNN per-station + simple aggregation) and GNN architecture (GAT on station graph)
3. **Week 3:** Experiments, ablations (graph construction strategies, attention visualization)
4. **Week 4:** Write-up targeting GRL (letter format, ~4500 words)

---

## 8. Verification Notes

Items marked [VERIFY] require manual checking against Google Scholar or publisher databases before citation. Key verification needed:
- Exact titles of Ross (2018) focal mechanism paper
- GENIE paper details (year, exact venue)
- McBrearty phase association paper venue/year
- GaMMA exact title and venue
- Papers #14-16 need full verification of existence and details

**Recommended verification approach:** Search Google Scholar for `author:"Ross ZE" focal mechanism deep learning` and similar queries for each [VERIFY] item.

---

*Document prepared as research acceleration guide. All [VERIFY]-tagged items should be confirmed before inclusion in any manuscript bibliography.*
