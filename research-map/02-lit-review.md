# Literature Review: GNN-Based Focal Mechanism Estimation

> **Topic:** Earthquake Focal Mechanism Determination via Deep Learning & Graph Neural Networks  
> **Reference:** DM-EQ-GNN-001 (01-domain-map.md)  
> **Scope:** 16 anchor papers from domain map, categorized, compared, and critiqued  
> **Date:** June 2025

---

## 1. Paper Categorization by Taxonomy

### Category 1: Seismic Signal Processing — Phase Picking (Taxonomy 1.1)

| # | Paper | Year | Sub-category |
|---|-------|------|--------------|
| P01 | PhaseNet (Zhu & Beroza) | 2019 | CNN-based picking |
| P02 | EQTransformer (Mousavi et al.) | 2020 | Attention-based picking |
| P06 | Which Picker Fits My Data (Münchmeyer et al.) | 2022 | Benchmark / comparison |

### Category 2: Seismic Signal Processing — Event Detection & Association (Taxonomy 1.2)

| # | Paper | Year | Sub-category |
|---|-------|------|--------------|
| P03 | GENIE (Ross et al.) | 2022 | GNN event association |
| P04 | Earthquake Phase Association with GNN (McBrearty & Beroza) | 2023 | Graph-based association |
| P12 | GaMMA (Zhu et al.) | 2022 | Backprojection + GNN association |

### Category 3: Source Parameter Estimation — Focal Mechanism (Taxonomy 2.1)

| # | Paper | Year | Sub-category |
|---|-------|------|--------------|
| P08 | Focal Mechanisms from DL (Ross, Meier, Hauksson) | 2018 | First-motion polarity CNN |
| P14 | Focal Mechanism Determination by DL (Kuang et al.) | 2021 | DL-based FM estimation |
| P07 | Rapid Bayesian source inversion with DL (Münchmeyer et al.) | 2022 | Bayesian / uncertainty-aware |

### Category 4: Source Parameter Estimation — Magnitude & Location (Taxonomy 2.2–2.3)

| # | Paper | Year | Sub-category |
|---|-------|------|--------------|
| P11 | DL multi-station magnitude estimation (Mousavi) | 2020 | Network-level magnitude |
| P16 | Earthquake location with GNN (van den Ende / Münchmeyer) | 2022–2023 | Graph-based location |

### Category 5: GNN in Seismology — Architecture & Application (Taxonomy 4)

| # | Paper | Year | Sub-category |
|---|-------|------|--------------|
| P05 | TEAM - Transformer Earthquake Alerting Model (Münchmeyer et al.) | 2021 | Multi-station early warning |
| P15 | GNN for Earthquake Early Warning | 2023 | GNN architecture for EEW |

### Category 6: Datasets & Benchmarks (Cross-cutting)

| # | Paper | Year | Sub-category |
|---|-------|------|--------------|
| P10 | STEAD (Mousavi et al.) | 2019 | Global waveform dataset |
| P13 | INSTANCE (Michelini et al.) | 2021 | Italian regional dataset |

### Category 7: Transfer Learning / Broader DL Seismology (Taxonomy 5)

| # | Paper | Year | Sub-category |
|---|-------|------|--------------|
| P09 | MyShake ML aspects (Kong et al.) | 2019 | Smartphone network, transfer |

---

## 2. Individual Paper Summaries

### P01: PhaseNet (Zhu & Beroza, 2019, GJI)

**Problem:** Automated seismic phase picking is traditionally done with STA/LTA or template matching, which struggle with noisy/complex waveforms. **Method:** U-Net architecture applied to 3-component waveforms, outputting probability distributions for P, S arrivals and noise. Trained on Northern California catalog data. **Key Result:** Achieves human-expert-level picking accuracy with sub-sample precision; generalizes well across regions without retraining. **Limitation:** Single-station approach - does not leverage inter-station information. Cannot assess network-level consistency or handle cases where individual stations have ambiguous signals that could be resolved by network context.

### P02: EQTransformer (Mousavi et al., 2020, Nature Communications)

**Problem:** Simultaneous earthquake detection and phase picking in a single model for operational deployment. **Method:** Encoder-decoder architecture with transformer self-attention, processing 1-minute 3C windows. Multi-task output: detection + P pick + S pick. **Key Result:** State-of-the-art picking performance; robust to noise; detects ~4x more events than traditional catalogs when applied to continuous data. **Limitation:** Still single-station; attention mechanism operates temporally within one station's waveform rather than spatially across stations. No uncertainty quantification in the standard output.

### P03: GENIE (Ross et al., ~2022, GRL/JGR) [VERIFY]

**Problem:** Earthquake event detection and characterization using the full seismic network simultaneously rather than combining single-station detections post-hoc. **Method:** Graph neural network where stations are nodes and edges represent spatial relationships. Message passing aggregates information across the network to detect events and estimate source parameters. **Key Result:** Demonstrates that network-level GNN processing outperforms single-station approaches followed by association, particularly for small events near detection threshold. **Limitation:** Focused primarily on detection/association rather than full focal mechanism estimation. Graph construction uses simple spatial proximity without physics-informed edge weighting.

### P04: Earthquake Phase Association with GNN (McBrearty & Beroza, 2023, BSSA) [VERIFY]

**Problem:** Phase association - linking detected arrivals at multiple stations to their source events - is computationally challenging especially in regions with high seismicity rates. **Method:** Graph neural network formulation where picks are nodes and potential associations are edges; the network learns to classify edges as belonging to same/different events. **Key Result:** Scalable, accurate association that handles overlapping events and high-rate sequences better than traditional grid-search or backprojection methods. **Limitation:** Operates on pre-picked arrivals (depends on upstream picker quality). Does not extend to source parameter estimation beyond association.

### P05: TEAM (Münchmeyer et al., 2021, GJI)

**Problem:** Earthquake early warning requires rapid magnitude and location estimation from the first seconds of waveform data across a network. **Method:** Transformer-based model that processes multi-station waveforms with attention across both time and stations. Permutation-invariant station dimension allows variable network geometry. **Key Result:** Produces magnitude and location estimates with uncertainty within seconds of P-arrival; competitive with operational EEW systems. **Limitation:** Designed for EEW (seconds of data) rather than full source characterization. Does not output focal mechanism. Station interactions modeled via attention but not explicit graph structure.

### P06: Which Picker Fits My Data (Münchmeyer et al., 2022, JGR-SE)

**Problem:** Multiple DL pickers exist but comparison is difficult due to different training data, evaluation metrics, and deployment conditions. **Method:** Systematic benchmark of PhaseNet, EQTransformer, and other pickers across multiple datasets (ETHZ, GEOFON, INSTANCE, etc.) with standardized evaluation. **Key Result:** No single picker dominates all scenarios; performance depends heavily on noise conditions, magnitude range, and distance. PhaseNet and EQTransformer perform similarly overall. **Limitation:** Benchmark limited to single-station pickers. Does not evaluate network-level or GNN-based approaches. Does not address downstream task performance (e.g., how picking quality affects focal mechanism estimation).

### P07: Rapid Bayesian Source Inversion with DL (Münchmeyer et al., ~2022, GRL) [VERIFY]

**Problem:** Traditional moment tensor inversion is slow and requires manual selection of data windows and frequency bands. Point estimates lack uncertainty information. **Method:** Deep learning model (likely mixture density network or normalizing flow) trained to output posterior distributions over source parameters given multi-station waveforms. **Key Result:** Produces full Bayesian posteriors for source parameters in near-real-time; uncertainty estimates are well-calibrated and correlate with known quality metrics. **Limitation:** Likely trained on well-instrumented networks; transferability to sparse networks unclear. May not explicitly model station geometry as graph structure.

### P08: Focal Mechanisms from DL (Ross, Meier, Hauksson, ~2018, GRL) [VERIFY]

**Problem:** First-motion polarity-based focal mechanism determination requires manual polarity picks and sufficient azimuthal coverage, limiting catalog completeness. **Method:** CNN trained on waveforms to directly predict focal mechanism parameters (or polarity), bypassing manual polarity picking. Trained on Southern California catalog with HASH-determined mechanisms as labels. **Key Result:** Demonstrates feasibility of DL-based focal mechanism estimation; can produce mechanisms for events too small for traditional methods. **Limitation:** Pioneer work with relatively simple architecture. Single-station or simple aggregation without explicit network geometry modeling. Limited uncertainty quantification. Quality degrades significantly with poor azimuthal coverage.

### P09: MyShake ML Aspects (Kong et al., 2019, SRL) [VERIFY]

**Problem:** Earthquake detection on smartphones faces extreme noise challenges and variable sensor quality. **Method:** Machine learning classification of phone accelerometer data to distinguish earthquake shaking from human activities. Network of millions of phones as distributed sensors. **Key Result:** Successful detection of M≥5 events; demonstrates crowdsourced seismic monitoring is feasible. **Limitation:** Low SNR limits application to moderate-large events. Not directly relevant to focal mechanism but demonstrates network-level DL for seismology. Transfer learning across device types not deeply explored.

### P10: STEAD (Mousavi et al., 2019, IEEE Access)

**Problem:** DL seismology lacks a large, standardized, labeled benchmark dataset analogous to ImageNet. **Method:** Curation of ~1.2 million labeled seismic waveforms (P/S picks, event metadata) from global seismic networks, with standardized format and splits. **Key Result:** Enables training of large DL models; serves as transfer learning source. Widely adopted as community benchmark. **Limitation:** Predominantly body-wave signals from well-instrumented regions. Does not include focal mechanism labels. Class imbalance in magnitude distribution. Geographic bias toward North America and well-monitored regions.

### P11: DL Multi-Station Magnitude Estimation (Mousavi, ~2020, GRL) [VERIFY]

**Problem:** Single-station magnitude estimation has high variance; combining multiple stations traditionally uses simple averaging. **Method:** DL model that jointly processes waveforms from multiple stations to estimate magnitude, learning optimal combination weights implicitly. **Key Result:** Multi-station DL approach reduces magnitude estimation variance compared to single-station models and simple averaging. **Limitation:** Station combination is via simple concatenation or attention, not explicit graph structure. Does not extend to focal mechanism estimation where azimuthal information is critical.

### P12: GaMMA (Zhu et al., ~2022, JGR-SE) [VERIFY]

**Problem:** Earthquake phase association at scale, especially for dense catalogs produced by DL pickers. **Method:** Combines Gaussian Mixture Model Association with graph neural network refinement. Backprojection provides initial candidates; GNN refines associations. **Key Result:** Handles massive pick volumes from continuous DL picker deployment; scales to high-seismicity regions. **Limitation:** Focused on association task only. Graph structure is pick-based (not station-geometry-based). Does not produce source parameters beyond location.

### P13: INSTANCE (Michelini et al., 2021, ESSD)

**Problem:** Need for regional high-quality labeled seismic dataset for Italian seismicity, complementing global STEAD dataset. **Method:** ~1.2 million 3C waveforms from Italian National Seismic Network with comprehensive metadata (picks, magnitudes, focal mechanisms for subset). **Key Result:** High-quality regional dataset; includes noise traces; better metadata completeness than STEAD for Italian events. Some events have focal mechanism labels. **Limitation:** Regional scope (Italy only). Focal mechanism labels available for only a subset of events. Network geometry different from other regions, limiting generalization studies.

### P14: Focal Mechanism by DL (Kuang et al., ~2021) [VERIFY]

**Problem:** Extending DL focal mechanism estimation beyond first-motion polarity to use full waveform information. **Method:** DL architecture (likely CNN or hybrid) processing multi-station waveforms to directly output focal mechanism parameters. May use synthetic training data or transfer from well-labeled catalogs. **Key Result:** Shows improvement over polarity-only methods by leveraging amplitude ratio and waveform shape information. **Limitation:** Architecture details and exact approach need verification. Likely does not use GNN for station interaction modeling. May have limited evaluation scope.

### P15: GNN for Earthquake Early Warning (~2023) [VERIFY]

**Problem:** Earthquake early warning needs rapid assessment from heterogeneous, variable-geometry station networks. **Method:** GNN processing station waveforms with graph structure encoding station spatial relationships for real-time magnitude/intensity estimation. **Key Result:** GNN outperforms non-graph baselines for EEW by explicitly modeling station-station information flow. Handles missing stations gracefully. **Limitation:** Focused on EEW (magnitude/intensity), not focal mechanism. Short waveform windows limit source information content.

### P16: Earthquake Location with GNN (van den Ende / Münchmeyer, ~2022-2023) [VERIFY]

**Problem:** Earthquake location using DL that explicitly accounts for network geometry and station-to-station relationships. **Method:** GNN where stations are nodes, processing waveforms with message passing to output hypocenter coordinates. Graph structure encodes station geometry. **Key Result:** Demonstrates that GNN-based location outperforms single-station or simple concatenation approaches, especially for events with limited station coverage. **Limitation:** Applied to location only, not extended to full source characterization (focal mechanism). Graph construction strategy may be simplistic (distance-based).

---

## 3. Comparative Table

### 3.1 Methods Comparison

| Paper | Architecture | Input | Output | Multi-Station | Graph Structure | Uncertainty |
|-------|-------------|-------|--------|---------------|----------------|-------------|
| P01 PhaseNet | U-Net (CNN) | 1-station 3C | P/S picks | No | No | No |
| P02 EQTransformer | Encoder-Decoder + Attention | 1-station 3C | Det + P/S picks | No | No | No |
| P03 GENIE | GNN (message passing) | N-station waveforms | Event detection + params | Yes | Spatial proximity | Partial |
| P04 McBrearty GNN | GNN (edge classification) | Pick features | Phase association | Yes | Pick connectivity | No |
| P05 TEAM | Transformer | N-station waveforms | Mag + Location (EEW) | Yes | Implicit (attention) | Yes |
| P06 Picker Benchmark | Various (comparison) | 1-station 3C | P/S picks | No | No | Partial |
| P07 Bayesian Source | MDN / NF [VERIFY] | N-station waveforms | Moment tensor posterior | Yes | Unknown [VERIFY] | **Yes (full)** |
| P08 Ross FM-DL | CNN | 1/N-station waveforms | Focal mechanism | Partial | No | No |
| P11 Multi-Mag | DL (attention) | N-station waveforms | Magnitude | Yes | No (concatenation) | Partial |
| P12 GaMMA | GMM + GNN | Pick catalogs | Association | Yes | Pick-based graph | No |
| P14 Kuang FM-DL | CNN/hybrid [VERIFY] | N-station waveforms | Focal mechanism | Yes [VERIFY] | No | Unknown |
| P15 GNN-EEW | GNN | N-station waveforms | Mag/Intensity (EEW) | Yes | Spatial graph | Partial |
| P16 GNN-Location | GNN | N-station waveforms | Hypocenter | Yes | Spatial graph | Partial |

### 3.2 Datasets Used

| Paper | Training Dataset | Region | # Events (approx) | FM Labels? |
|-------|-----------------|--------|-------------------|------------|
| P01 PhaseNet | NCEDC | N. California | ~780K traces | No |
| P02 EQTransformer | STEAD | Global | ~1.2M traces | No |
| P03 GENIE | SCSN [VERIFY] | S. California | ~100K+ events | No (detection task) |
| P05 TEAM | Multiple (ETHZ, etc.) | Multi-region | ~100K events | No (EEW task) |
| P07 Bayesian Source | Regional catalog [VERIFY] | Likely S. California or Japan | ~10K-50K events | Yes |
| P08 Ross FM-DL | SCSN + HASH catalog | S. California | ~30K-100K FM | Yes |
| P10 STEAD | Global compilation | Global | ~1.2M traces | No |
| P13 INSTANCE | Italian network | Italy | ~1.2M traces | Partial |
| P14 Kuang FM-DL | Unknown [VERIFY] | Unknown | Unknown | Yes |

### 3.3 Performance Metrics (where reported)

| Paper | Task | Key Metric | Reported Performance |
|-------|------|-----------|---------------------|
| P01 PhaseNet | P picking | Mean absolute error | ~0.03s (P), ~0.05s (S) |
| P02 EQTransformer | P picking | Mean absolute error | ~0.02s (P), ~0.04s (S) |
| P02 EQTransformer | Detection | Precision/Recall | >95% precision at >90% recall |
| P05 TEAM | EEW magnitude | MAE | ~0.3 magnitude units (at 5s) |
| P08 Ross FM-DL | Focal mechanism | Kagan angle [VERIFY] | ~20-30° median rotation [VERIFY] |
| P14 Kuang FM-DL | Focal mechanism | Kagan angle [VERIFY] | Improvement over HASH [VERIFY] |

> **Note:** Focal mechanism accuracy is typically measured by Kagan angle (rotation angle between predicted and true double-couple). A Kagan angle <30° is generally considered acceptable; <15° is excellent.

---

## 4. Identified Gaps (Concrete & Actionable)

### Gap 1: No GNN Architecture Explicitly Designed for Focal Mechanism Estimation

**Observation:** Papers P03, P04, P12, P15, P16 demonstrate that GNNs are effective for seismic tasks (detection, association, location, EEW). Papers P08 and P14 show that DL can estimate focal mechanisms. However, **no paper in this corpus combines GNN with focal mechanism estimation.** The focal mechanism papers (P08, P14) use CNN or simple multi-station aggregation without explicit graph-based station interaction.

**Why this gap exists:**
- Focal mechanism estimation is historically a smaller community than phase picking
- The natural connection between graph structure and azimuthal coverage has not been formally exploited
- GNN in seismology papers have focused on "easier" tasks (detection, location) before tackling source inversion
- Training data requirements: need both waveforms AND reliable focal mechanism labels

**Why it's actionable now:**
- GNN tooling is mature (PyG, DGL)
- SCSN HASH catalog provides >100K focal mechanisms with waveforms
- Proof-of-concept exists for both components separately (GNN-seismic + DL-focal mechanism)

---

### Gap 2: Physics-Informed Graph Construction (Take-Off Angle + Azimuth as Edge Features)

**Observation:** All GNN seismology papers (P03, P04, P12, P15, P16) use **distance-based** or **k-NN spatial** graph construction. None incorporates physics of wave propagation into edge features or graph topology. For focal mechanisms specifically, the **take-off angle** and **azimuth** from source to each station are the fundamental quantities - yet these are never used as edge features or for graph construction.

**Why this gap exists:**
- Take-off angle requires a velocity model + hypocenter (chicken-and-egg with location)
- Simpler distance-based graphs "work well enough" for detection/location
- The seismology-ML community has prioritized end-to-end learning over physics-informed design

**Why it's actionable now:**
- For focal mechanism estimation, hypocenter is typically already known (from catalog)
- 1D velocity models are readily available for most regions
- Take-off angle computation is cheap and well-understood
- Incorporating physics into edges could dramatically reduce required training data

---

### Gap 3: Uncertainty-Aware GNN Focal Mechanism with Calibrated Posteriors

**Observation:** Paper P07 demonstrates Bayesian source inversion, but likely without GNN graph structure. GNN papers (P03, P15, P16) have at most partial uncertainty. **No work combines GNN architecture + focal mechanism + full Bayesian uncertainty quantification.**

**Why this gap exists:**
- Bayesian methods + GNN is computationally expensive (combining two sources of complexity)
- Calibrating uncertainty for structured outputs (strike/dip/rake on non-Euclidean manifold) is non-trivial
- The focal mechanism community and the GNN community have limited overlap

**Why it's actionable now:**
- Normalizing flows and evidential deep learning can produce calibrated uncertainties efficiently
- GNN + uncertainty has been explored in other domains (molecular property prediction)
- HASH quality metrics provide proxy ground-truth for uncertainty calibration

---

### Gap 4: Variable Network Geometry Robustness for Focal Mechanism

**Observation:** DL focal mechanism models (P08, P14) are trained on fixed or implicitly fixed network geometries. When deployed on events with different station subsets (due to outages, different regions, sparse networks), performance likely degrades. GNNs are architecturally suited to handle this (permutation invariant, variable input size) but this property has **not been demonstrated for focal mechanism estimation.**

**Why this gap exists:**
- Most focal mechanism DL studies use well-instrumented networks (SCSN) where geometry is relatively stable
- Testing generalization to sparse/different networks requires multi-region datasets with FM labels
- The "just retrain for each network" approach has been the default

**Why it's actionable now:**
- GNN naturally handles variable graph sizes (fewer nodes = fewer stations)
- Can be tested via station dropout experiments on SCSN data
- Directly relevant to deployment in under-instrumented regions (Indonesia, Africa)
- Can be validated with INSTANCE data (different network geometry)

---

### Gap 5: Graph Attention Interpretability Mapped to Focal Sphere

**Observation:** GNN attention weights (from GAT architectures) provide natural interpretability - which station pairs contribute most to the prediction. For focal mechanisms, these attention patterns should map to **physically meaningful structures on the focal sphere** (nodal planes, pressure/tension axes). No paper has demonstrated this connection.

**Why this gap exists:**
- Interpretability in GNN-seismology is rarely explored beyond basic visualization
- Mapping graph attention to focal sphere requires domain-specific interpretation
- Most GNN papers focus on predictive performance rather than scientific insight

**Why it's actionable now:**
- GAT attention weights are trivially extractable
- Focal sphere visualization is standard in seismology
- Could provide genuine scientific insight (which station configurations are most informative)
- Strong narrative for a paper: "The model learns seismologically meaningful attention patterns"

---

## 5. Controversies & Conflicting Clusters

### Controversy 1: End-to-End vs. Modular Approaches

**Cluster A (End-to-end):** P02 (EQTransformer), P03 (GENIE), P08 (Ross FM-DL) advocate for end-to-end learning directly from raw waveforms, arguing that hand-crafted features limit performance.

**Cluster B (Modular/hybrid):** P12 (GaMMA) uses traditional backprojection + GNN refinement. P04 (McBrearty) operates on pre-picked features. Implicit argument: decomposing the problem into stages allows better control and interpretability.

**Relevance to your work:** For GNN focal mechanism, you must decide: (a) end-to-end from waveforms through GNN to FM, or (b) modular (pick first, extract features, then GNN on features → FM). The modular approach is faster to implement and easier to debug, but end-to-end may achieve better performance.

### Controversy 2: Data-Driven vs. Physics-Informed

**Cluster A (Pure data-driven):** P01, P02, P08 train entirely from data with minimal physics constraints.

**Cluster B (Physics-informed):** P07 (Bayesian) incorporates physical priors on source parameters. TEAM (P05) uses physics-motivated station weighting.

**Relevance:** For focal mechanisms, physics provides strong constraints (double-couple constraint, moment tensor symmetry, amplitude radiation patterns). Ignoring these leads to physically implausible solutions. Incorporating them (as loss functions or architectural constraints) could be a key differentiator.

---

## 6. Papers to Read in Full (Priority Order)

Based on the gap analysis, these 5 papers are **essential** before writing:

| Priority | Paper | Reason |
|----------|-------|--------|
| 1 | **P08: Ross et al. (2018) - Focal Mechanisms from DL** | Direct predecessor to your work. Must understand architecture, limitations, and training approach in detail. |
| 2 | **P03: GENIE (Ross et al., 2022)** | Best example of GNN applied to multi-station seismology. Architecture decisions (graph construction, message passing) directly inform your design. |
| 3 | **P07: Münchmeyer et al. (2022) - Bayesian Source Inversion** | Closest to your target (source parameters + uncertainty). Understand how they handle multi-station input and uncertainty estimation. |
| 4 | **P05: TEAM (Münchmeyer et al., 2021)** | Multi-station transformer for source characterization. Attention mechanism over stations is analogous to what GAT would do. Compare design choices. |
| 5 | **P16: GNN Location (van den Ende/Münchmeyer)** | Most recent GNN + source parameter work. Graph construction choices and performance analysis directly relevant. |

**Secondary priority (read after the 5 above):**
- P14 (Kuang et al.) - verify what they actually did for DL focal mechanism
- P04 (McBrearty GNN association) - GNN architecture details
- P13 (INSTANCE) - potential validation dataset with FM labels

---

## 7. Gap-to-Paper Mapping (Your Novelty Justification)

| Your Proposed Contribution | Gap # | Papers That Don't Do This | Papers That Partially Approach |
|---------------------------|-------|--------------------------|-------------------------------|
| GNN architecture for focal mechanism | Gap 1 | P08, P14 (no GNN); P03, P15, P16 (no FM) | P07 (multi-station source, but likely not GNN) |
| Physics-informed edges (take-off angle, azimuth) | Gap 2 | All papers use distance/k-NN graphs | None (completely unexplored) |
| Uncertainty quantification on FM via GNN | Gap 3 | P08, P14 (no uncertainty); P03, P15 (no FM uncertainty) | P07 (uncertainty but likely not GNN) |
| Robustness to variable station geometry | Gap 4 | P08 (fixed network assumption) | P03, P05 (variable input but not FM) |
| Attention interpretability on focal sphere | Gap 5 | None currently do this | — |

**Minimum viable novelty for Q1 paper:** Gaps 1 + 2 (GNN for FM with physics-informed graph). Adding Gap 3 (uncertainty) strengthens to top Q1 (GRL/Nature Communications level).

---

## 8. Summary Statement for Introduction

> "While deep learning has achieved remarkable success in seismic phase picking (Zhu & Beroza, 2019; Mousavi et al., 2020) and graph neural networks have proven effective for multi-station event detection and association (Ross et al., 2022; McBrearty & Beroza, 2023; Zhu et al., 2022), the application of GNNs to earthquake focal mechanism estimation remains unexplored. Existing DL approaches to focal mechanisms (Ross et al., 2018; Kuang et al., 2021) process stations independently or via simple aggregation, failing to exploit the rich geometric information encoded in station-network topology — information that is fundamental to the focal mechanism problem. Here we propose [YOUR METHOD], a graph attention network that explicitly models station spatial relationships and take-off angle geometry to estimate focal mechanisms with calibrated uncertainty."

---

## Acceptance Checklist

- [x] 16 papers categorized into taxonomy (limited to input corpus per constraint)
- [x] Comparative table: methods × datasets × metrics
- [x] 5 concrete, actionable gaps identified
- [x] Each gap has "why it exists" + "why it's actionable now" argument
- [x] Controversy clusters identified (2)
- [x] 5 priority papers for deep reading identified
- [x] No citations added beyond input corpus
- [x] [VERIFY] tags preserved from DM-001

---

*Note: This review is based solely on the 16 anchor papers from DM-EQ-GNN-001. A complete literature review for submission should incorporate 30-50 papers including recent 2024-2025 preprints. The gaps identified are robust to the limited corpus but should be re-validated against a broader search.*
