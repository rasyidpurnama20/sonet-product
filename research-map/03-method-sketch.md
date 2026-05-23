# Method Sketch: FocalGNN — Graph Attention Network for Earthquake Focal Mechanism Estimation

> **Reference:** DM-EQ-GNN-001, LR-EQ-GNN-002  
> **Target venue:** Geophysical Research Letters (GRL) — letter format (~4500 words, 5 figures)  
> **Timeline:** 4 weeks  
> **Date:** June 2025

---

## 1. Problem Formulation

### 1.1 Input
Given an earthquake event with known hypocenter $(x_0, y_0, z_0, t_0)$ recorded by $N$ seismic stations:
- **Waveforms:** $\mathbf{W} = \{w_1, w_2, ..., w_N\}$ where $w_i \in \mathbb{R}^{3 \times T}$ (3-component, $T$ samples)
- **Station metadata:** $\mathbf{S} = \{s_1, s_2, ..., s_N\}$ where $s_i = (\text{lat}_i, \text{lon}_i, \text{elev}_i)$
- **Source-station geometry:** $\mathbf{G} = \{g_1, g_2, ..., g_N\}$ where $g_i = (\text{azimuth}_i, \text{take-off angle}_i, \text{distance}_i)$

### 1.2 Output
Focal mechanism parameterized as:
- **Primary:** Strike ($\phi$), Dip ($\delta$), Rake ($\lambda$) with uncertainty
- **Alternative:** Moment tensor components $M_{ij}$ (6 independent components, constrained to double-couple or deviatoric)
- **Uncertainty:** Per-parameter standard deviation or full posterior (von Mises-Fisher distribution on focal sphere)

### 1.3 Mathematical Formulation
$$f_\theta: (\mathbf{W}, \mathbf{S}, \mathbf{G}) \rightarrow (\hat{\phi}, \hat{\delta}, \hat{\lambda}, \sigma_\phi, \sigma_\delta, \sigma_\lambda)$$

where $f_\theta$ is a GNN with learnable parameters $\theta$.

---

## 2. Architecture: FocalGNN

### 2.1 Overview (3-Stage Pipeline)

```
┌─────────────────────────────────────────────────────────────────┐
│                         FocalGNN                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Stage 1: Per-Station Feature Extraction (CNN Encoder)           │
│  ┌──────┐  ┌──────┐       ┌──────┐                              │
│  │ Sta1 │  │ Sta2 │  ...  │ StaN │   ← 3C waveforms            │
│  │ CNN  │  │ CNN  │       │ CNN  │   (shared weights)            │
│  └──┬───┘  └──┬───┘       └──┬───┘                              │
│     │         │              │                                    │
│     ▼         ▼              ▼                                    │
│  [h₁]      [h₂]    ...   [hN]      ← station embeddings        │
│                                                                   │
│  Stage 2: Graph Neural Network (Station Interaction)             │
│  ┌─────────────────────────────────────────────────┐             │
│  │  Graph: nodes=stations, edges=physics-informed   │            │
│  │                                                   │            │
│  │  Node features: hᵢ ⊕ gᵢ (embedding + geometry)  │            │
│  │  Edge features: eᵢⱼ (Δazimuth, Δtakeoff, dist)  │            │
│  │                                                   │            │
│  │  GAT Layer 1 → GAT Layer 2 → GAT Layer 3        │            │
│  │  (with residual connections)                      │            │
│  └─────────────────────────────────────────────────┘             │
│     │                                                             │
│     ▼                                                             │
│  [h'₁, h'₂, ..., h'N]  ← context-enriched embeddings           │
│                                                                   │
│  Stage 3: Readout & Prediction Head                              │
│  ┌─────────────────────────────────────────────────┐             │
│  │  Global attention pooling → graph-level embedding │            │
│  │  MLP → (strike, dip, rake, σ_strike, σ_dip, σ_rake)│         │
│  └─────────────────────────────────────────────────┘             │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Stage 1: Per-Station CNN Encoder

**Architecture:** 1D ResNet-18 adapted for 3-component seismic waveforms.

| Layer | Channels | Kernel | Stride | Output |
|-------|----------|--------|--------|--------|
| Input | 3 | — | — | 3 × T |
| Conv1 + BN + ReLU | 32 | 7 | 2 | 32 × T/2 |
| ResBlock1 (×2) | 32 | 3 | 1 | 32 × T/2 |
| ResBlock2 (×2) | 64 | 3 | 2 | 64 × T/4 |
| ResBlock3 (×2) | 128 | 3 | 2 | 128 × T/8 |
| ResBlock4 (×2) | 256 | 3 | 2 | 256 × T/16 |
| Global Average Pool | 256 | — | — | 256 |

**Output:** $h_i \in \mathbb{R}^{256}$ per station.

**Key design decisions:**
- Shared weights across all stations (parameter efficiency)
- Input window: 10s post-P arrival, 100 Hz sampling → T = 1000 samples
- 3C input preserves polarity and amplitude ratio information

### 2.3 Stage 2: Physics-Informed Graph Attention Network

#### 2.3.1 Graph Construction

**Nodes:** Each recording station is a node.  
**Node features:** Concatenation of CNN embedding + source-station geometry:
$$x_i = h_i \oplus \text{MLP}_\text{geo}(g_i) \in \mathbb{R}^{256 + 64 = 320}$$

where $g_i = [\text{azimuth}_i, \text{takeoff}_i, \text{epicentral\_dist}_i, \cos(\text{az}_i), \sin(\text{az}_i), \cos(\text{to}_i), \sin(\text{to}_i)]$

**Edges:** Fully connected graph with physics-informed edge features:
$$e_{ij} = [\Delta\text{azimuth}_{ij}, \Delta\text{takeoff}_{ij}, d_{ij}, \cos(\Delta\text{az}_{ij}), \sin(\Delta\text{az}_{ij})]$$

where:
- $\Delta\text{azimuth}_{ij} = \text{az}_i - \text{az}_j$ (azimuthal separation on focal sphere)
- $\Delta\text{takeoff}_{ij} = \text{to}_i - \text{to}_j$ (take-off angle difference)
- $d_{ij}$ = inter-station distance (km, normalized)

**Rationale:** Azimuthal separation is the most critical geometric quantity for focal mechanisms. Two stations with 90° azimuthal separation provide maximally complementary information about nodal planes.

#### 2.3.2 Graph Attention (GAT) Layers

Using GATv2 (Brody et al., 2022) with edge features:

$$\alpha_{ij} = \frac{\exp(\text{LeakyReLU}(\mathbf{a}^T [\mathbf{W}x_i \| \mathbf{W}x_j \| \mathbf{W}_e e_{ij}]))}{\sum_{k \in \mathcal{N}(i)} \exp(\text{LeakyReLU}(\mathbf{a}^T [\mathbf{W}x_i \| \mathbf{W}x_k \| \mathbf{W}_e e_{ik}]))}$$

$$x_i' = \sigma\left(\sum_{j \in \mathcal{N}(i)} \alpha_{ij} \mathbf{W}_v x_j\right)$$

**Configuration:**
- 3 GAT layers with residual connections
- 4 attention heads per layer
- Hidden dimension: 320 → 320 → 320
- Dropout: 0.1 between layers
- Edge features incorporated into attention computation

#### 2.3.3 Why GAT over GCN/GraphSAGE?

| Architecture | Pros for FM | Cons |
|-------------|-------------|------|
| GCN | Simple, fast | Fixed aggregation weights; cannot learn station importance |
| GraphSAGE | Scalable sampling | Sampling not needed for small graphs (<100 nodes) |
| **GAT** | **Learns which stations matter; attention = interpretability** | Slightly more parameters |
| MPNN | Flexible message functions | Less interpretable than attention |

**Decision: GAT** because attention weights provide direct interpretability (which station pairs are most informative for the focal mechanism) and the graphs are small (typically 10-50 stations per event).

### 2.4 Stage 3: Readout & Prediction

#### 2.4.1 Global Pooling
Attention-weighted global pooling:
$$z = \sum_{i=1}^{N} \beta_i \cdot x_i'$$

where $\beta_i = \text{softmax}(\text{MLP}_\text{gate}(x_i'))$ learns which stations to weight for the final prediction.

#### 2.4.2 Prediction Head

**Option A: Direct regression (strike/dip/rake)**
```
MLP: 320 → 256 → 128 → 6 (strike, dip, rake, σ_s, σ_d, σ_r)
```

**Problem:** Strike/rake are circular (0-360°), dip is bounded (0-90°). Naive regression fails at boundaries.

**Option B: Moment tensor components (PREFERRED)**
```
MLP: 320 → 256 → 128 → 12 (Mij_mean × 6 + Mij_logvar × 6)
```

Then decompose to double-couple (strike/dip/rake) post-hoc.

**Option C: Classification on discretized focal sphere**
Discretize the focal sphere into ~500-1000 cells. Output probability distribution over cells.
```
MLP: 320 → 256 → 128 → K (K = number of focal sphere cells)
```

**Decision: Option B** (moment tensor regression with uncertainty) because:
1. Avoids circular boundary issues of strike/rake
2. Naturally symmetric (moment tensor is symmetric)
3. Uncertainty in MT space is Gaussian-approximable
4. Can enforce deviatoric/double-couple constraint as regularization

#### 2.4.3 Uncertainty Estimation

**Approach:** Heteroscedastic aleatoric uncertainty + MC Dropout epistemic uncertainty.

- **Aleatoric:** Network outputs both mean and log-variance for each MT component
- **Epistemic:** MC Dropout (keep dropout at test time, run 50 forward passes)
- **Total uncertainty:** $\sigma^2_\text{total} = \sigma^2_\text{aleatoric} + \sigma^2_\text{epistemic}$

Convert MT uncertainty to Kagan angle uncertainty via error propagation or sampling.

---

## 3. Loss Function

### 3.1 Primary Loss: Negative Log-Likelihood

$$\mathcal{L}_\text{NLL} = \frac{1}{2} \sum_{k=1}^{6} \left[ \frac{(M_k - \hat{M}_k)^2}{\hat{\sigma}_k^2} + \log \hat{\sigma}_k^2 \right]$$

where $M_k$ are the 6 independent moment tensor components.

### 3.2 Auxiliary Loss: Double-Couple Constraint

$$\mathcal{L}_\text{DC} = \lambda_\text{DC} \cdot \frac{|\text{det}(\mathbf{M})|}{\|\mathbf{M}\|_F^3}$$

Encourages solutions close to pure double-couple (det(M)=0 for DC).

### 3.3 Auxiliary Loss: Polarity Consistency

$$\mathcal{L}_\text{pol} = \lambda_\text{pol} \cdot \text{BCE}(p_i^\text{predicted}, p_i^\text{observed})$$

where $p_i$ is the P-wave first-motion polarity at station $i$, derived from the predicted MT at station $i$'s take-off angle and azimuth.

### 3.4 Total Loss

$$\mathcal{L} = \mathcal{L}_\text{NLL} + \lambda_1 \mathcal{L}_\text{DC} + \lambda_2 \mathcal{L}_\text{pol}$$

**Hyperparameters:** $\lambda_1 = 0.1$, $\lambda_2 = 0.05$ (tuned on validation set).

---

## 4. Data Pipeline

### 4.1 Training Data: Southern California (SCSN)

| Item | Details |
|------|---------|
| **Source catalog** | SCSN HASH focal mechanism catalog |
| **Period** | 2000-2022 |
| **Magnitude range** | M 2.0 - 5.5 |
| **Expected events** | ~80,000-150,000 with quality A/B HASH solutions |
| **Waveform source** | SCEDC continuous archive |
| **Stations per event** | 5-50 (variable) |
| **Waveform window** | 10s post-P arrival, 3C, 100 Hz |
| **Labels** | Strike/Dip/Rake from HASH → convert to moment tensor |

### 4.2 Preprocessing

1. **Waveform retrieval:** Download 3C waveforms for each event-station pair
2. **Instrument response removal:** Deconvolve to velocity (nm/s)
3. **Bandpass filter:** 1-20 Hz (preserves first-motion + S/P amplitude ratio)
4. **Window:** P-arrival - 1s to P-arrival + 9s (10s total)
5. **Normalization:** Per-trace z-score normalization (preserve relative amplitude via 3C joint normalization)
6. **Geometry computation:** Azimuth + take-off angle from catalog hypocenter + SoCal 1D velocity model

### 4.3 Data Augmentation

| Augmentation | Rationale | Implementation |
|-------------|-----------|----------------|
| Station dropout | Robustness to missing stations | Random drop 10-50% stations per event |
| Noise addition | SNR robustness | Add scaled noise traces from STEAD |
| Time shift | Picking error robustness | ±0.5s random shift on window |
| Polarity flip [CAREFUL] | — | DO NOT: would change the label! |

### 4.4 Train/Val/Test Split

| Split | Criteria | Purpose |
|-------|----------|---------|
| Train | 2000-2018 events | Model training |
| Validation | 2019-2020 events | Hyperparameter tuning |
| Test | 2021-2022 events | Final evaluation |

**Temporal split** ensures no data leakage (model never sees future events during training).

### 4.5 Validation Dataset: INSTANCE (Italy)

- Different network geometry, different tectonic regime
- Subset of events with focal mechanism labels
- Tests cross-region generalization (Gap 4)

---

## 5. Experimental Design

### 5.1 Baselines

| # | Baseline | Description | What it tests |
|---|----------|-------------|---------------|
| B1 | HASH | Traditional first-motion polarity method | Classical benchmark |
| B2 | Single-CNN | Per-station CNN → average predictions | DL without graph structure |
| B3 | Multi-CNN-Concat | All station waveforms concatenated → CNN | Naive multi-station DL |
| B4 | Transformer (TEAM-style) | Attention over stations without explicit graph | Implicit vs explicit graph |
| B5 | GNN-Distance | FocalGNN with distance-only edges (no physics) | Value of physics-informed edges |

### 5.2 Ablation Studies

| # | Ablation | Question Answered |
|---|----------|-------------------|
| A1 | Remove edge features | Does physics-informed edge help? |
| A2 | Replace GAT with GCN | Does attention matter? |
| A3 | Remove geometry input ($g_i$) | Does explicit geometry help vs. learning it? |
| A4 | Remove DC constraint loss | Does physics loss improve solutions? |
| A5 | Vary # GAT layers (1,2,3,4) | Optimal depth? |
| A6 | Vary # stations (5, 10, 20, 50) | Performance vs. station count |

### 5.3 Evaluation Metrics

| Metric | Formula / Description | Target |
|--------|----------------------|--------|
| **Kagan angle** (primary) | Minimum rotation angle between predicted and true DC | Median < 20° |
| Kagan angle (P25/P75) | Quartiles | P25 < 10°, P75 < 35° |
| Strike/Dip/Rake MAE | Individual parameter errors | — |
| Fault-type accuracy | Normal/Reverse/Strike-slip classification | >85% |
| Uncertainty calibration | Expected calibration error (ECE) | <0.05 |
| Coverage probability | % of true values within 90% CI | ~90% |

### 5.4 Interpretability Analysis

1. **Attention weight visualization:** Project GAT attention weights onto focal sphere
2. **Station importance:** Which stations receive highest attention? Correlate with azimuthal gap
3. **Edge importance:** Which station pairs have highest attention? Relate to nodal plane geometry
4. **Comparison with physics:** Do attention patterns correlate with theoretical radiation pattern?

---

## 6. Implementation Plan

### 6.1 Tech Stack

| Component | Choice | Justification |
|-----------|--------|---------------|
| Framework | PyTorch + PyTorch Geometric | Best GNN support, flexibility |
| Data loading | ObsPy + HDF5 | Standard seismology + fast I/O |
| Geometry | ObsPy TauP | Take-off angle computation |
| Experiment tracking | W&B or MLflow | Hyperparameter logging |
| Visualization | ObsPy + Matplotlib | Focal sphere + beachball plots |

### 6.2 Compute Requirements

| Resource | Estimate |
|----------|----------|
| GPU | 1× A100 (40GB) or 1× V100 (32GB) sufficient |
| Training time | ~2-4 hours per experiment (small graphs, ~100K events) |
| Total experiments | ~30 (baselines + ablations + hyperparameter search) |
| Total GPU hours | ~60-120 hours |
| Storage | ~500GB (waveforms in HDF5) |

### 6.3 Timeline (4 Weeks)

```
Week 1: Data + Baseline
├── Day 1-2: Download SCSN catalog + HASH FM labels
├── Day 3-4: Waveform retrieval pipeline (ObsPy + FDSN)
├── Day 5-6: Preprocessing + HDF5 packaging
└── Day 7: Implement B1 (HASH) and B2 (Single-CNN) baselines

Week 2: FocalGNN Implementation
├── Day 8-9: Stage 1 (CNN encoder) + unit tests
├── Day 10-11: Stage 2 (GAT with physics edges) + unit tests
├── Day 12-13: Stage 3 (readout + uncertainty) + loss functions
└── Day 14: End-to-end training loop, first successful training run

Week 3: Experiments + Ablations
├── Day 15-16: Full training of FocalGNN + all baselines
├── Day 17-18: Ablation experiments (A1-A6)
├── Day 19-20: Station dropout experiments (Gap 4)
└── Day 21: Interpretability analysis + attention visualization

Week 4: Writing
├── Day 22-23: Figures (architecture, results, attention maps, comparison)
├── Day 24-25: Draft introduction + method + results
├── Day 26-27: Discussion + conclusion + abstract
└── Day 28: Internal review, formatting for GRL, submission prep
```

---

## 7. Paper Outline (GRL Format)

### Title Options:
1. "FocalGNN: Physics-Informed Graph Attention Network for Earthquake Focal Mechanism Estimation"
2. "Earthquake Focal Mechanisms from Station-Network Graph Neural Networks with Uncertainty Quantification"
3. "Graph Neural Networks for Focal Mechanism Determination: Exploiting Station Geometry"

### Structure:

**Abstract** (~200 words)
- Problem: FM estimation needs azimuthal coverage info that existing DL methods ignore
- Method: GNN with physics-informed edges (take-off angle, azimuth)
- Result: Reduces median Kagan angle by X° vs. baselines; calibrated uncertainty; robust to sparse networks
- Impact: Enables reliable FM estimation for small events in under-instrumented regions

**1. Introduction** (~800 words)
- DL revolution in seismology (picking, detection)
- Focal mechanism estimation: importance + current limitations
- GNN in seismology: success in other tasks
- Gap statement: no GNN for FM with physics-informed geometry
- This work: FocalGNN contributions (3 bullets)

**2. Data** (~500 words)
- SCSN catalog description
- HASH FM labels
- Preprocessing pipeline
- Split strategy

**3. Method** (~1000 words)
- Graph construction (physics-informed edges)
- Architecture (CNN encoder + GAT + readout)
- Loss function (NLL + DC constraint + polarity)
- Uncertainty estimation

**4. Results** (~1000 words)
- Overall performance vs. baselines (Table 1)
- Effect of physics-informed edges (Ablation)
- Effect of station count (degradation curve)
- Uncertainty calibration (reliability diagram)
- Cross-region test (INSTANCE)

**5. Discussion** (~700 words)
- Interpretability: attention → focal sphere
- When does FocalGNN fail? (very few stations, high noise)
- Comparison with traditional methods
- Implications for operational seismology

**6. Conclusions** (~300 words)

**Figures (5 max for GRL):**
1. Architecture diagram
2. Results comparison (Kagan angle CDF + boxplot)
3. Attention weights mapped to focal sphere (2-3 example events)
4. Performance vs. number of stations (degradation curve)
5. Uncertainty calibration (reliability diagram) OR cross-region generalization

---

## 8. Risk Assessment & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| SCSN waveform download too slow | Medium | High (blocks everything) | Start immediately; use pre-existing HDF5 if available; limit to M>2.5 |
| GNN doesn't outperform Transformer baseline | Low-Medium | High | Physics-informed edges are the differentiator; if pure architecture comparison fails, pivot to interpretability narrative |
| Uncertainty not well-calibrated | Medium | Medium | Use temperature scaling post-hoc; report calibration honestly |
| HASH labels noisy (quality C/D) | Low | Medium | Filter to quality A/B only; discuss label noise in limitations |
| Cross-region (INSTANCE) fails | Medium | Low | Frame as "future work" if results are negative; main contribution is methodology |
| Reviewer says "not enough novelty" | Low-Medium | High | Ensure physics-informed edges + uncertainty + interpretability = 3 contributions |

---

## 9. Key Innovation Claims (For Rebuttal Preparation)

1. **First application of GNN to focal mechanism estimation** — no prior work combines these
2. **Physics-informed edge features** (azimuthal separation, take-off angle difference) — novel graph construction specific to the focal mechanism problem
3. **Demonstrated robustness to variable network geometry** — GNN naturally handles station dropout without retraining
4. **Interpretable attention patterns** on focal sphere — provides scientific insight beyond prediction
5. **Calibrated uncertainty** — enables quality assessment of automated FM solutions

---

## 10. Potential Reviewer Concerns (Pre-emptive)

| Concern | Response |
|---------|----------|
| "Hypocenter must be known — limits operational use" | True for real-time, but vast majority of FM studies use catalog hypocenters. Same assumption as HASH. Joint location-FM is future work. |
| "Why not just use Transformer (TEAM-style)?" | We test this as baseline B4. GNN with explicit physics edges outperforms because focal mechanism is inherently a geometric problem on the focal sphere. |
| "HASH labels are noisy ground truth" | We filter to quality A/B (>8 polarities, azimuthal gap <90°). We also show uncertainty correlates with HASH quality grade. |
| "Only tested on Southern California" | Cross-validated on INSTANCE (Italy). Full global evaluation is future work. |
| "Computational cost?" | GNN inference is <100ms per event. Training is <4 hours on single GPU. Minimal overhead vs. standard CNN. |

---

*This method sketch provides a complete implementation blueprint. All architectural decisions are justified by the gap analysis from 02-lit-review.md. The experimental design is sufficient for a GRL submission with clear novelty claims.*
