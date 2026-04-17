# Mock Exam 2 — Answer Key & Detailed Explanations

---

## Question 1: Data Preprocessing Pipeline [4 marks]

**Pipeline 1:** Raw data → Min-Max Normalisation → PCA → Pre-processed data

- The data is **numerical** because Min-Max normalisation operates on numerical values, scaling them to a fixed range (typically [0,1]).
- The **features may have different scales**, which is why normalisation is applied first — PCA is sensitive to feature scaling, so normalisation ensures all features contribute equally.
- The data likely has a **large number of features (high dimensionality)** because PCA (Principal Component Analysis) is used to reduce dimensionality. This suggests the dataset has many correlated features, and PCA extracts the most informative combinations while reducing noise and computational cost.

**Pipeline 2:** Raw data → Imputer (median) → Standardisation → Polynomial Feature Expansion

- The data is **numerical with missing values** since median imputation is used. The choice of median over mean suggests the data may have **outliers or a skewed distribution**, as the median is more robust to extreme values.
- **Features are on different scales**, hence standardisation (z-score normalisation to mean=0, std=1) is applied.
- The **relationship between features and the target may be non-linear**, which is why polynomial feature expansion is used. This creates new features by combining existing ones (e.g., $x_1^2$, $x_1 \cdot x_2$), allowing a linear model to capture non-linear patterns.

---

## Question 2: Design Choices [6 marks]

**Diagnosis:** The model is **underfitting** (high bias). Both training (55%) and validation (53%) accuracies are low and close together, while 92% is achievable. The model is not complex enough to capture the patterns in the data.

**(a) L2 regularisation:**
**NO**, this is unlikely to improve validation accuracy. L2 regularisation constrains the model by penalising large weights, effectively reducing the model's effective capacity. Since the model is already underfitting (not fitting even the training data well), adding regularisation would further constrain it, potentially making the underfitting worse. Regularisation is a remedy for overfitting, not underfitting.

**(b) Increasing to 6 layers, 256 neurons:**
**YES**, this is likely to improve validation accuracy. Since the model is underfitting, it likely lacks the capacity to represent the complexity of the data. Increasing the number of layers (from 3 to 6) and neurons per layer (from 64 to 256) gives the model more representational power. With more parameters, the model can learn more complex decision boundaries. However, this should be done carefully — too much capacity without enough data could lead to overfitting in subsequent iterations.

**(c) Data augmentation:**
**YES**, this could help improve validation accuracy. Data augmentation increases the effective size and diversity of the training set by applying transformations (rotations, flips, noise, etc.). For an underfitting model, more diverse data can help the model learn more general and robust patterns. Additionally, if the model is underfitting partly due to insufficient training data (not enough examples to learn from), augmentation addresses this directly. Note: the augmentation must be relevant to the domain — irrelevant augmentation could hurt performance.

---

## Question 3: Evaluation [4 marks]

**(a) Metric calculations [2 marks]:**

$$\text{Accuracy} = \frac{TP + TN}{Total} = \frac{70 + 370}{500} = \frac{440}{500} = 0.88 \text{ (88\%)}$$

$$\text{Precision} = \frac{TP}{TP + FP} = \frac{70}{70 + 30} = \frac{70}{100} = 0.70 \text{ (70\%)}$$

$$\text{Recall} = \frac{TP}{TP + FN} = \frac{70}{70 + 30} = \frac{70}{100} = 0.70 \text{ (70\%)}$$

$$\text{F1} = \frac{2 \times 0.70 \times 0.70}{0.70 + 0.70} = \frac{0.98}{1.40} = 0.70 \text{ (70\%)}$$

**(b) Medical context analysis [2 marks]:**

In a medical diagnostic context, this model's 88% accuracy appears good, but the critical concern is the **30 false negatives** — these are patients who HAVE the disease but the model says they don't. In medicine, missing a real disease (false negative) can be life-threatening, as these patients won't receive treatment.

The **recall of 70%** means the model only detects 70% of actual disease cases, **missing 30% of sick patients**. In a screening context, this is often unacceptable — a good screening test should have high recall (>95%) to avoid missing cases.

The **precision of 70%** means 30% of positive predictions are false alarms. While false positives are inconvenient (unnecessary follow-up tests), they are generally less dangerous than false negatives in medical contexts.

**Conclusion:** For a high-stakes medical application, this model needs improvement, particularly in recall. The threshold could be lowered to catch more true positives (increasing recall), accepting more false positives (lower precision) — because the cost of missing a disease is much higher than the cost of an extra test.

---

## Question 4: Learning Rate [4 marks]

**(a) Learning rate schedule [2 marks]:**

**Example: Step Decay** — the learning rate is reduced by a factor (e.g., halved) every N epochs.

$$lr_t = lr_0 \times \gamma^{\lfloor t / N \rfloor}$$

For example, starting with lr=0.01, reducing by factor 0.5 every 50 epochs:
- Epochs 1-50: lr = 0.01
- Epochs 51-100: lr = 0.005
- Epochs 101-150: lr = 0.0025

**Why beneficial:** A high initial learning rate allows the optimiser to make large updates and quickly approach a good region of the loss landscape. As training progresses and the model approaches an optimum, the large learning rate would cause overshooting — oscillating around the minimum without converging precisely. By reducing the learning rate over time, the optimiser can make finer adjustments near the optimum, leading to better final performance.

**(b) Adam's components [2 marks]:**

Adam combines:

1. **Momentum (from SGD with Momentum):** Adam maintains an exponentially decaying average of past gradients (first moment estimate). This smooths the optimisation trajectory, reduces oscillations, and accelerates convergence in consistent gradient directions.

2. **RMSProp:** Adam also maintains an exponentially decaying average of past squared gradients (second moment estimate). This provides per-parameter adaptive learning rates — parameters with large recent gradients get smaller learning rates (prevents overshooting), while parameters with small gradients get larger learning rates (speeds up learning in flat regions).

By combining both, Adam provides momentum-like acceleration AND per-parameter adaptation, making it robust across a wide range of architectures and problems, which is why it's the most popular default optimiser.

---

## Question 5: RNN and Transformer [4 marks]

**(a) Vanishing gradient problem [2 marks]:**

In RNNs, during backpropagation through time (BPTT), the gradient of the loss with respect to earlier time steps requires multiplying gradients across many time steps:

$$\frac{\partial L}{\partial h_1} = \frac{\partial L}{\partial h_T} \cdot \prod_{t=2}^{T} \frac{\partial h_t}{\partial h_{t-1}}$$

Each factor $\frac{\partial h_t}{\partial h_{t-1}}$ involves the recurrent weight matrix and the derivative of the activation function. If these factors are consistently less than 1, their product decreases **exponentially** with sequence length. For a sequence of length 100, the gradient at step 1 might be $0.9^{100} \approx 0.00003$ of the gradient at step 100.

This makes it extremely difficult for the model to learn that early inputs in a sequence are relevant to later outputs — the gradient signal is too weak for the optimiser to update the weights meaningfully. For example, in a sentence like "The man who lived in the big house near the river that runs through the valley **was** happy", the RNN struggles to connect "man" (position 2) with "was" (position 17) because the gradient vanishes over those 15 steps.

**(b) Two Transformer mechanisms [2 marks]:**

**1. Self-Attention Mechanism:** The Transformer computes attention scores between ALL pairs of positions in the sequence simultaneously. Each position creates Query, Key, and Value vectors; the attention weight between any two positions is the softmax-normalised dot product of their Q and K vectors. This creates **direct connections** between any two positions regardless of distance — solving the long-range dependency problem without sequential processing. Crucially, all attention computations are matrix multiplications that can be done **in parallel**.

**2. Positional Encoding:** Since the Transformer processes all positions simultaneously (no sequential structure), it has no inherent notion of order — "dog bites man" and "man bites dog" would produce the same attention scores. Positional encoding adds a unique signal to each position's embedding using sinusoidal functions of different frequencies (or learned embeddings). This allows the model to distinguish and reason about the order of elements in the sequence while still processing them in parallel.

---

## Question 6: CNN [4 marks]

**(a) Calculation [3 marks]:**

```
Layer: Conv1 (padding = 1, same)
  Input:  [64, 64, 1]
  Calc:   (64 + 2×1 - 3) / 1 + 1 = 64
  Output: [64, 64, 32]       ← 32 filters

Layer: MaxPool1 (k=2, s=2)
  Input:  [64, 64, 32]
  Calc:   (64 - 2) / 2 + 1 = 32
  Output: [32, 32, 32]       ← depth unchanged

Layer: Conv2 (padding = 0, valid)
  Input:  [32, 32, 32]
  Calc:   (32 + 2×0 - 3) / 2 + 1 = 29/2 + 1 = 15.5 → floor = 15
  Output: [15, 15, 64]       ← 64 filters

Layer: Conv3 (padding = 1, same)
  Input:  [15, 15, 64]
  Calc:   (15 + 2×1 - 3) / 1 + 1 = 15
  Output: [15, 15, 128]      ← 128 filters

Layer: MaxPool2 (k=2, s=2)
  Input:  [15, 15, 128]
  Calc:   (15 - 2) / 2 + 1 = 13/2 + 1 = 7.5 → floor = 7
  Output: [7, 7, 128]        ← depth unchanged

Flatten: 7 × 7 × 128 = 6272
```

**Answer:** The fully connected layer has **6,272 inputs**.

**(b) Filter visualisation [1 mark]:**

**Conv1 filters** (close to input): Would detect **low-level features** such as edges (horizontal, vertical, diagonal), simple textures, and basic colour gradients. These are the building blocks of visual recognition.

**Conv3 filters** (deeper): Would detect **higher-level features** that combine the patterns from earlier layers — such as corners, shapes, parts of objects, or more complex textures. These represent more abstract, semantically meaningful features.

The difference is due to **hierarchical feature learning**: each layer builds increasingly complex representations by combining patterns detected by the previous layer. Early layers = simple edges → middle layers = shapes and patterns → deep layers = object parts and complex structures.

---

## Question 7: Activation Functions and DNN [4 marks]

**(a) Sigmoid vs Softmax [2 marks]:**

**Sigmoid:** Outputs a value between 0 and 1 for each neuron **independently**. Each output can be interpreted as the probability of a binary event, without any relationship to other outputs.
- **Best for:** Multi-label classification (e.g., image tagging where a photo can be both "sunset" AND "beach" AND "ocean"). Each label is predicted independently.

**Softmax:** Outputs values between 0 and 1 that **sum to 1** across all output neurons. Creates a probability distribution over classes.
- **Best for:** Multi-class classification (e.g., classifying an image as exactly one of "cat", "dog", or "bird"). The classes are mutually exclusive.

**Key difference:** Sigmoid treats each output independently; softmax creates competition between outputs (increasing one probability decreases others). Using softmax for multi-label tasks would be wrong because detecting one label would suppress detection of other labels.

**(b) Two strategies for very deep networks [2 marks]:**

**1. Skip/Residual Connections (as in ResNet):**
Instead of learning the full mapping $H(x) = F(x)$, the network learns the **residual** $F(x) = H(x) - x$, and the output becomes $F(x) + x$. The $+x$ shortcut connection creates a direct gradient path from later layers to earlier layers, bypassing the many intermediate multiplications that cause gradients to vanish. Even if $F(x)$ has vanishing gradients, the gradient flows through the skip connection unimpeded. This allows training of networks with 100+ layers, whereas without skip connections, training degrades beyond ~20 layers.

**2. Batch Normalisation:**
Normalises activations at each layer to have zero mean and unit variance (computed per mini-batch), then applies learned scale and shift parameters. This addresses two key deep learning challenges:
- **Vanishing/exploding gradients:** By keeping activations in a controlled range, gradients remain well-scaled throughout the network
- **Internal covariate shift:** Each layer's input distribution remains stable during training, allowing higher learning rates and faster convergence

Together, these techniques have enabled the training of networks with hundreds of layers (e.g., ResNet-152, ResNet-1001) that were previously impossible to optimise.

---

**Scoring Summary:**
| Question | Topic | Marks |
|----------|-------|-------|
| Q1 | Data Preprocessing | 4 |
| Q2 | Design Choices | 6 |
| Q3 | Evaluation | 4 |
| Q4 | Learning Rate | 4 |
| Q5 | RNN & Transformer | 4 |
| Q6 | CNN | 4 |
| Q7 | Activation + DNN | 4 |
| **Total** | | **30** |
