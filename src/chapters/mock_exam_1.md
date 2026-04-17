# Mock Exam 1 — 20 Marks (2025 Format)

> **Instructions:** 60 minutes total. 5 minutes reading + 55 minutes writing.
> Double-sided handwritten cheat sheet allowed. No calculators.
> Attempt ALL questions. Be concise and clear.

---

## Question 1: Data Preprocessing [3 marks]

Consider the following dataset summary with 8,000 samples:

| Attribute | Type | Missing Values | Mean | Std Dev | Max | Min |
|-----------|------|---------------|------|---------|-----|-----|
| A1 | Categorical | 150 | / | / | / | / |
| A2 | Numerical | 30 | 45.2 | 12.1 | 210.5 | -5.0 |
| A3 | Numerical | 7,850 | 3.0 | 0.5 | 4.0 | 2.0 |
| A4 | Binary | 0 | / | / | / | / |
| A5 | Numerical | 0 | 1200 | 8500 | 150000 | -30000 |

For each of the following cleaning steps, explain whether it makes sense to apply it to this dataset. Briefly justify your answers. [0.5 mark per step, + 0.5 for overall justification]

- (a) Missing value replacement based on most frequent value.
- (b) Missing value replacement based on mean value.
- (c) Removing an attribute.
- (d) Standardisation.
- (e) Outlier removal.

---

## Question 2: Bias-Variance and Design Choices [4 marks]

You trained a neural network with the following settings: 8 hidden layers with ReLU units, 128 neurons per layer, trained for 500 epochs with a batch size of 32 and no regularisation. After training, the training accuracy is 98% and the validation accuracy is 52%.

(a) Diagnose the model's performance in terms of bias and variance. [1 mark]

(b) For each of the following suggestions, explain whether it is likely to improve the validation accuracy and why. [1 mark per suggestion]
- Adding dropout (rate=0.5) to each hidden layer.
- Reducing the number of hidden layers from 8 to 2.
- Training for 1000 epochs instead of 500.

---

## Question 3: Evaluation Metrics [3 marks]

A spam detection model is evaluated on a test set of 2,000 emails (200 spam, 1,800 not spam). The confusion matrix is:

|  | Actually Spam | Actually Not Spam |
|--|---|---|
| **Predicted Spam** | 180 | 360 |
| **Predicted Not Spam** | 20 | 1440 |

(a) Calculate the accuracy, precision, and recall. [1.5 marks]

(b) Is this model suitable for deployment as a spam filter? Explain your reasoning, considering what each metric means in this context. [1.5 marks]

---

## Question 4: Learning Rate and Batch Normalisation [4 marks]

(a) Explain in your own words what is the momentum mechanism in gradient descent optimisation, and describe its effect on training. [2 marks]

(b) Give two effects of batch normalisation on the training of a neural network. For each effect, briefly explain the mechanism behind it. [2 marks]

---

## Question 5: Transformers and ViT [3 marks]

(a) In a Transformer model, the self-attention mechanism computes Query (Q), Key (K), and Value (V) matrices. Explain what role each plays in the attention computation. [1.5 marks]

(b) Explain why multi-head attention is preferred over a single attention head in Transformer models. [1.5 marks]

---

## Question 6: CNN Architecture [3 marks]

Consider the following CNN architecture:
- Input: [32, 32, 3]
- Conv1: 8 filters, kernel size = 5, stride = 1, padding = 0 (valid)
- MaxPool1: kernel size = 2, stride = 2
- Conv2: 16 filters, kernel size = 3, stride = 1, padding = 1 (same)
- MaxPool2: kernel size = 2, stride = 2
- Fully connected layer: **?** inputs → 10 outputs

(a) What is the number of inputs to the fully connected layer? [1 mark]

(b) Show your calculation steps for each layer. [2 marks]

---

**END OF MOCK EXAM 1**
