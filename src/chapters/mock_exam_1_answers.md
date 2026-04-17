# Mock Exam 1 — Answer Key & Detailed Explanations

---

## Question 1: Data Preprocessing [3 marks]

**(a) Most frequent value imputation:**
**YES** for A1 (categorical with 150 missing values). Most frequent value strategy is appropriate for categorical data with a moderate number of missing values.
**NO** need for A4 (binary, no missing values).

**(b) Mean value imputation:**
**Not ideal** — for A2 (30 missing, numerical), imputation is needed but **median** would be better than mean because the max (210.5) is unusually high relative to the mean (45.2), suggesting outliers. Mean is sensitive to outliers. For A5, no missing values so no imputation needed.

**(c) Removing an attribute:**
**YES** for A3 — it has 7,850 out of 8,000 values missing (98.1%). Imputing so many values would create almost entirely fabricated data, which is misleading and unlikely to help the model.

**(d) Standardisation:**
**YES** — A2 has values around 45, while A5 has values around 1,200 with a huge range. Features on different scales should be standardised so no single feature dominates the model.

**(e) Outlier removal:**
**YES** — A5 has mean=1200 but std=8500 (std >> mean), and extremes of 150,000 and -30,000. A2 also has max=210.5 which is ~13.6 standard deviations above the mean (suspicious). These suggest outliers that could distort model training.

---

## Question 2: Bias-Variance and Design Choices [4 marks]

**(a) Diagnosis [1 mark]:**
The model displays **high variance (overfitting)**. The training accuracy (98%) is significantly higher than the validation accuracy (52%), indicating the model has learned to fit the training data very closely but fails to generalise to unseen data. The model is too complex for the amount of data (8 layers, 128 neurons, no regularisation).

**(b) Evaluate suggestions [1 mark each]:**

**Dropout (rate=0.5):**
**YES**, likely to improve validation accuracy. Since the model is overfitting, dropout will randomly deactivate 50% of neurons during each training step. This prevents co-adaptation of neurons and forces the network to learn more robust, distributed representations. It acts as a regularisation technique, reducing the gap between training and validation performance.

**Reducing layers from 8 to 2:**
**YES**, likely to improve validation accuracy. The current model (8 layers, 128 neurons) has very high capacity, which contributes to overfitting. Reducing to 2 layers decreases the model's capacity to memorise training noise. However, it might also reduce the model's ability to learn complex patterns — the optimal size depends on the problem complexity. Given the severe overfitting, reducing complexity is a reasonable first step.

**Training for 1000 epochs:**
**NO**, this will likely make the validation accuracy **worse**. The model is already overfitting at 500 epochs. Training for longer will allow the model to memorise the training data even more closely, further increasing the gap between training and validation accuracy. If anything, earlier stopping would be more beneficial.

---

## Question 3: Evaluation Metrics [3 marks]

**(a) Calculations [1.5 marks]:**

$$\text{Accuracy} = \frac{TP + TN}{Total} = \frac{180 + 1440}{2000} = \frac{1620}{2000} = 0.81 \text{ (81\%)}$$

$$\text{Precision} = \frac{TP}{TP + FP} = \frac{180}{180 + 360} = \frac{180}{540} = 0.333 \text{ (33.3\%)}$$

$$\text{Recall} = \frac{TP}{TP + FN} = \frac{180}{180 + 20} = \frac{180}{200} = 0.90 \text{ (90\%)}$$

**(b) Suitability analysis [1.5 marks]:**

Despite the seemingly good accuracy (81%), the model is **not suitable** for deployment as a spam filter in its current form.

**The problem is precision (33.3%):** Of all emails the model flags as spam, only 1 in 3 actually IS spam. This means 2 out of every 3 "spam" flags are legitimate emails being incorrectly blocked (360 false positives). For a spam filter, this is extremely disruptive — users would miss important emails regularly.

**The recall (90%) is good:** The model catches 90% of actual spam, missing only 20 out of 200 spam emails.

**Recommendation:** In a spam filter, precision is arguably more important than recall — it's better to let some spam through (lower recall) than to block legitimate emails (low precision). The classification threshold should be adjusted to increase precision, even at the cost of some recall. Alternatively, flagged emails could be moved to a "spam folder" rather than deleted, allowing users to review.

---

## Question 4: Learning Rate and Batch Normalisation [4 marks]

**(a) Momentum [2 marks]:**

The momentum mechanism maintains an exponentially decaying running average of past gradients to determine the direction and magnitude of weight updates.

Without momentum, each gradient update depends only on the current mini-batch gradient, which can be noisy — the optimisation path zigzags. With momentum, the update is:

$$v_t = \beta \cdot v_{t-1} + (1 - \beta) \cdot \nabla L$$

The parameter $\beta$ (typically 0.9) controls how much weight is given to past gradients.

**Effects:**
1. **Smoother optimisation:** By averaging past gradients, noisy fluctuations are dampened, leading to more consistent update directions
2. **Faster convergence:** When the gradient consistently points in the same direction, momentum builds up speed (like a ball rolling downhill), accelerating progress
3. **Escaping local minima:** The accumulated momentum can carry the optimisation through shallow local minima that would trap standard gradient descent

**(b) Batch normalisation effects [2 marks]:**

**Effect 1: Speeds up training.** Batch normalisation normalises the activations within each mini-batch to have zero mean and unit variance. This keeps the input distribution to each layer stable throughout training (reduces internal covariate shift), allowing the use of higher learning rates. The activations remain in a range where gradients are meaningful (not too small, not too large), leading to faster convergence.

**Effect 2: Has a regularising effect.** Because normalisation is computed over mini-batches rather than the full dataset, each sample's normalised value depends on which other samples happen to be in the same mini-batch. This introduces noise into the activations, similar to dropout. This noise acts as implicit regularisation, helping prevent overfitting without explicitly adding a regularisation term.

---

## Question 5: Transformers and ViT [3 marks]

**(a) Q, K, V roles [1.5 marks]:**

In the self-attention mechanism:

- **Query (Q):** Represents what each position is "looking for" — it encodes the current position's request for relevant information from other positions. Think of it as a question: "What information do I need?"

- **Key (K):** Represents what each position "contains" or "offers" — it encodes features that other positions can match against. Think of it as a label on a file: "This is what I'm about."

- **Value (V):** Represents the actual information content at each position — once the attention weights are computed (by matching Q with K), the values are combined according to these weights to produce the output.

The attention score between two positions is computed as the dot product of Q and K (how well the query matches the key), scaled by $\sqrt{d_k}$, then softmaxed to get weights. These weights are applied to V to get the final attended output.

**(b) Why multi-head is preferred [1.5 marks]:**

Multi-head attention is preferred because it allows the model to attend to information from different **representation subspaces** simultaneously.

A single attention head computes one set of attention weights, which tends to have an **averaging effect** — it tries to capture all types of relationships (syntactic, semantic, positional) in a single attention distribution. This limits its expressiveness.

Multi-head attention runs $h$ parallel attention operations, each with independently learned $W^Q$, $W^K$, $W^V$ projections. Each head can specialise in different aspects: one head might learn to attend to nearby positions (local syntax), another to semantically related words far away, another to co-reference relationships. The outputs are concatenated and projected, giving the model a much richer representation of the relationships in the input.

---

## Question 6: CNN Architecture [3 marks]

**(a) Answer:** The number of inputs to the fully connected layer is **784**.

**(b) Step-by-step calculations:**

```
Layer: Conv1 (padding = 0, valid)
  Input:  [32, 32, 3]
  Calc:   (32 + 2×0 - 5) / 1 + 1 = 28
  Output: [28, 28, 8]       ← 8 filters

Layer: MaxPool1 (k=2, s=2)
  Input:  [28, 28, 8]
  Calc:   (28 - 2) / 2 + 1 = 14
  Output: [14, 14, 8]       ← depth unchanged

Layer: Conv2 (padding = 1, same)
  Input:  [14, 14, 8]
  Calc:   (14 + 2×1 - 3) / 1 + 1 = 14
  Output: [14, 14, 16]      ← 16 filters

Layer: MaxPool2 (k=2, s=2)
  Input:  [14, 14, 16]
  Calc:   (14 - 2) / 2 + 1 = 7
  Output: [7, 7, 16]        ← depth unchanged

Flatten: 7 × 7 × 16 = 784
```

**Answer: 784** inputs to the fully connected layer.

---

**Scoring Summary:**
| Question | Topic | Marks |
|----------|-------|-------|
| Q1 | Data Preprocessing | 3 |
| Q2 | Bias-Variance | 4 |
| Q3 | Evaluation Metrics | 3 |
| Q4 | LR + Batch Norm | 4 |
| Q5 | Transformers | 3 |
| Q6 | CNN Calculation | 3 |
| **Total** | | **20** |
