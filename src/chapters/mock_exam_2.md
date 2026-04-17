# Mock Exam 2 — 30 Marks (2024 Format)

> **Instructions:** 60 minutes total. 5 minutes reading + 55 minutes writing.
> Double-sided page of notes allowed. No calculators.
> Attempt ALL 7 questions. Be concise and clear.

---

## Question 1: Data Preprocessing Pipeline [4 marks]

Consider the following 2 preprocessing pipelines. For each pipeline, describe the likely characteristics of the input raw data and explain how you can derive them from the preprocessing steps. [2 marks per pipeline]

**Pipeline 1:**
```
Raw data → Min-Max Normalisation → PCA (dimensionality reduction) → Pre-processed data
```

**Pipeline 2:**
```
Raw data → Imputer (median value) → Standardisation → Polynomial Feature Expansion → Pre-processed data
```

---

## Question 2: Design Choices [6 marks]

You trained a neural network with the following settings: 3 hidden layers with ReLU units, 64 neurons per layer, Xavier initialisation, trained for 300 epochs with a learning rate of 0.01. The training accuracy is 55% and the validation accuracy is 53%. You know that state-of-the-art models achieve 92% on the same problem.

For each of the following suggestions, explain if it is likely to improve the validation accuracy and why. [2 marks per suggestion]

- (a) Using L2 regularisation with $\lambda = 0.01$.
- (b) Increasing the model to 6 layers with 256 neurons per layer.
- (c) Using data augmentation techniques relevant to the problem domain.

---

## Question 3: Evaluation [4 marks]

A medical diagnostic model is evaluated on 500 patients (100 have the disease, 400 do not). The results are:

|  | Has Disease | No Disease |
|--|---|---|
| **Predicted Positive** | 70 | 30 |
| **Predicted Negative** | 30 | 370 |

(a) Calculate the accuracy, precision, recall, and F1 score. [2 marks]

(b) In a medical context, discuss whether this model's performance is acceptable. Consider the implications of each type of error. [2 marks]

---

## Question 4: Learning Rate [4 marks]

(a) Give an example of a learning rate schedule. Explain how it works and why it might be beneficial when training a neural network. [2 marks]

(b) The Adam optimiser is often described as combining the benefits of two other optimisation techniques. Name these two techniques and briefly explain what each contributes to Adam. [2 marks]

---

## Question 5: RNN and Transformer [4 marks]

(a) Explain the vanishing gradient problem in the context of RNNs. Why does it make learning long-range dependencies difficult? [2 marks]

(b) Describe two mechanisms that the Transformer architecture uses to handle sequential data, and explain the purpose of each. [2 marks]

---

## Question 6: CNN [4 marks]

Consider the following CNN architecture:

- Input: [64, 64, 1] (grayscale images)
- Conv1: 32 filters, kernel size = 3, stride = 1, padding = 1 (same)
- MaxPool1: kernel size = 2, stride = 2
- Conv2: 64 filters, kernel size = 3, stride = 2, padding = 0 (valid)
- Conv3: 128 filters, kernel size = 3, stride = 1, padding = 1 (same)
- MaxPool2: kernel size = 2, stride = 2
- Fully connected layer: **?** inputs → 256 → 10 outputs

(a) Calculate the number of inputs to the fully connected layer. Show your workings for each layer. [3 marks]

(b) If you were to visualise what the filters in Conv1 have learned, what types of patterns would you expect to see? What about Conv3? Explain the difference. [1 mark]

---

## Question 7: Activation Functions and DNN [4 marks]

(a) Explain the difference between sigmoid and softmax activation functions. Give a scenario where each would be the most appropriate choice for the output layer. [2 marks]

(b) Explain two different strategies that help mitigate the challenges of training very deep neural networks (e.g., 50+ layers). For each strategy, explain the mechanism and why it helps. [2 marks]

---

**END OF MOCK EXAM 2**
