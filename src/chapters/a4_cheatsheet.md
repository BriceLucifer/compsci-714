# COMPSCI 714 — A4 Cheatsheet (Print Both Sides)

---

## SIDE 1: FORMULAS + DIAGNOSIS + CONCEPTS

---

### 1. CNN Dimension Formulas (MUST — every exam)

```
Conv output:  floor((n + 2p - f) / s) + 1  × num_filters
Pool output:  floor((n - f) / s) + 1        × same_depth
Flatten:      H × W × C
```

- **Valid padding**: p = 0 (output shrinks)
- **Same padding**: output H,W = input H,W (p chosen automatically)
- **MaxPool vs AvgPool**: same output dimensions, only values differ
- Depth after Conv = number of filters; depth after Pool = unchanged

**Worked example (2025 Q6):**
```
[35,35,3] →Conv(valid,k=7,s=2)→ floor((35-7)/2)+1=15 → [15,15,10]
         →Pool(k=2,s=2)→ floor((15-2)/2)+1=7 → [7,7,10]
         →Conv(same,k=3,s=1)→ same H,W → [7,7,20]
         →Pool(k=2,s=2)→ floor((7-2)/2)+1=3 → [3,3,20]
         →Flatten: 3×3×20 = 180
```

---

### 2. Bias-Variance Diagnosis (MUST — ~20% of marks)

| Symptom | Diagnosis | Name |
|---------|-----------|------|
| Train HIGH, Val HIGH | High bias | Underfitting |
| Train LOW, Val HIGH (gap) | High variance | Overfitting |
| Train LOW, Val LOW | Good fit | — |

**Fixes for OVERFITTING (high variance):**
- More data / data augmentation ✓
- L2 regularisation (penalises large weights) ✓
- Dropout (randomly deactivates neurons) ✓
- Batch normalisation (regularising effect) ✓
- Reduce model size ✓
- Early stopping ✓
- More epochs ✗ (worsens it!)

**Fixes for UNDERFITTING (high bias):**
- Increase model size (more layers/neurons) ✓
- More/better features ✓
- Train longer ✓
- Reduce regularisation ✓
- Dropout ✗ (constrains already limited model!)
- Zero initialisation ✗ (symmetry problem — all neurons learn same thing)

---

### 3. Evaluation Metrics (HIGH)

```
Accuracy  = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)    "of predicted +, how many correct?"
Recall    = TP / (TP + FN)    "of actual +, how many found?"
F1        = 2 × (P × R) / (P + R)
```

**Trap:** High accuracy + low recall → class imbalance. Model predicts majority class.
**Trap:** 100% recall + low precision → model predicts everything as positive.

---

### 4. Learning Rate Curves (HIGH)

| Curve shape | LR | Reason |
|------------|-----|--------|
| Diverges (loss goes up) | Too high (e.g. 0.5) | Big updates overshoot |
| Fast converge → high loss | Slightly high (e.g. 0.1) | Overshoots optimum |
| Fast converge → low loss | Good (e.g. 0.01) | Just right |
| Very slow descent | Too small (e.g. 0.001) | Tiny updates |

**Momentum:** exponentially decaying average of past gradients → smoother updates, faster convergence.

**LR Schedule (e.g. exponential decay):** start high for fast progress, reduce to fine-tune near optimum.

**Adam:** momentum + adaptive per-parameter learning rates.

---

### 5. Activation Functions (MED)

| Function | Output range | Use case |
|----------|-------------|----------|
| ReLU | [0, ∞) | Hidden layers (default) |
| LeakyReLU | (-∞, ∞) | Hidden (fixes dying ReLU) |
| Sigmoid | (0, 1) | Output: binary / **multi-label** |
| Softmax | (0,1) sums to 1 | Output: **multi-class** (one label) |
| Tanh | (-1, 1) | Hidden (zero-centred) |

**Dying ReLU:** negative input → output=0 → no gradient → neuron "dies".
**LeakyReLU fix:** small slope (e.g. 0.01x) for negative inputs → neuron still gets gradient.

**KEY:** Multi-label (multiple outputs ON) → sigmoid. Multi-class (exactly one) → softmax.

---

### 6. Data Preprocessing (MUST)

| Step | Implies about raw data |
|------|----------------------|
| Median imputer | Numerical, has missing values, possibly skewed/outliers |
| Most-frequent imputer | Categorical, has missing values |
| Standardisation | Attributes on different scales |
| Log transform | Heavy-tailed distribution |
| One-hot encoding | Categorical, no ordinal relationship, not too many categories |
| Remove attribute | >99% missing values → imputation creates misleading info |

**When to remove vs impute:**
- Remove: vast majority missing (e.g. 9995/10000)
- Impute: reasonable number missing (e.g. 15/10000)

**Outlier detection:** extreme min/max relative to mean+std → likely outliers

---

## SIDE 2: ARCHITECTURES + ANSWER TEMPLATES

---

### 7. Transformer / Attention (MUST)

**Self-attention:** weighted sum of Values, where weights = relevance between Query and Key.

**Multi-head attention:** multiple attention heads with separate Q/K/V → each focuses on different aspects. Outputs concatenated.

**Masked attention (decoder):** prevents attending to future tokens → preserves autoregressive property during training (predict next token based only on previous).

**Positional encoding:** needed because Transformer processes all tokens in parallel → loses order information. Added to embeddings.

**ViT [CLS] token:** learnable token prepended to patch sequence → aggregates info from all patches via attention → fed to MLP for classification. Advantage: efficient, no need for global pooling.

---

### 8. RNN / LSTM (MED)

**RNN:** h_t = f(W·h_{t-1} + U·x_t + b). Sequential processing.
- Advantage: naturally captures order
- Drawback: can't parallelise → slow for long sequences
- Problem: vanishing gradients (long-range dependencies lost)

**LSTM:** 3 gates (forget, input, output) control information flow → solves vanishing gradient.

**How Transformer fixes RNN drawback:** processes all positions in parallel via embeddings + adds positional encoding for order info.

---

### 9. DNN Training Challenges (MED)

**Why deep nets are hard to train:**
1. Vanishing/exploding gradients
2. More prone to overfitting
3. Longer training time

**Strategies to help:**
- Skip connections / ResNet (y = F(x) + x, gradients flow through shortcut)
- Batch normalisation (normalises activations, keeps gradients healthy)
- Better optimisers (Adam, RMSProp)
- LSTM/GRU for sequences

**Batch Norm effects:** speeds up training, reduces vanishing gradients, regularisation effect, reduces sensitivity to weight initialisation.

---

### 10. Answer Templates

#### "Will this improve validation accuracy?"
```
[YES/NO], [suggestion] is [likely/unlikely] to improve validation accuracy.
The model is currently [overfitting/underfitting], as evidenced by
[train acc X% vs val acc Y%].
[Suggestion] [helps/does not help] because [mechanism].
```

#### "Explain a concept"
```
[Concept] is [one-sentence definition].
It works by [mechanism].
This is [beneficial/important] because [why].
```

#### "Interpret loss curves / metrics"
```
The [curve/metric] shows [observation].
This indicates [diagnosis].
This is because [cause].
```

#### CNN calculation
```
Layer: Input [H,W,C]
  formula: floor((H+2p-f)/s)+1 = ...
  Output: [H',W',C']
→ next layer...
→ Flatten: H×W×C = answer
```

---

### 11. Key English Phrases (copy-paste ready)

| Situation | Write this |
|-----------|-----------|
| Overfitting | "The model is overfitting, as training acc (X%) is much higher than validation acc (Y%)." |
| L2 helps | "L2 regularisation penalises large weights, encouraging a simpler, more generalisable model." |
| Dropout hurts underfitting | "Dropout will NOT help because the model is underfitting — it further constrains an already limited model." |
| More epochs hurts | "More epochs will worsen overfitting as the model continues to memorise training noise." |
| Class imbalance trap | "Despite high accuracy, the model is ineffective due to class imbalance — it achieves accuracy by predicting the majority class." |
| RNN advantage | "RNNs naturally capture sequential order during training." |
| RNN drawback | "Sequential processing prevents parallelisation, making training slow for long sequences." |
| Transformer fix | "The Transformer processes all positions in parallel via self-attention, using positional encoding to retain order information." |

---

### 12. Common Traps to Avoid

- Multi-label ≠ multi-class → sigmoid, NOT softmax
- High recall + low precision = predicting everything positive (not a good model)
- Regularisation fights overfitting, NEVER helps underfitting
- Zero initialisation → symmetry problem → all neurons learn the same
- More epochs → more overfitting, not less
- MaxPool vs AvgPool → same dimensions, different values
- Accuracy alone is misleading with imbalanced classes

### 13. Marks-per-minute priority

```
1. Bias/Variance diagnosis + fixes    ~20%  ← ALWAYS on exam
2. CNN dimension calculation           ~15%  ← ALWAYS on exam
3. Transformer/Attention concepts      ~15%  ← ALWAYS on exam
4. Data preprocessing reasoning        ~15%  ← ALWAYS on exam
5. Learning rate curve matching        ~10%  ← usually on exam
6. Confusion matrix metrics            ~10%  ← usually on exam
7. Activation functions                ~5%
8. RNN vs Transformer                  ~5%
9. Batch Norm / DNN training           ~5%
```
