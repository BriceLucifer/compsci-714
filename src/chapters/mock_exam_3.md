# Mock Exam 3 — 20 Marks (2025 Format)

> **Instructions:** 60 minutes total. 5 minutes reading + 55 minutes writing.
> Double-sided handwritten cheat sheet allowed. No calculators.
> Attempt ALL questions. Be concise and clear.

| Question | Topic | Out of |
|----------|-------|--------|
| 1 | Dataset cleaning | 2 |
| 2 | Design choices | 3 |
| 3 | Evaluation & Confusion Matrix | 4 |
| 4 | Activation functions | 3 |
| 5 | Learning rate & optimisers | 4 |
| 6 | CNNs | 4 |
| **TOTAL** | | **20** |

---

## Question 1: Dataset cleaning [2 marks]

Consider the following summary of a dataset containing 5 attributes and 6,000 samples. The table gives the type and number of missing values for each attribute, as well as the mean, standard deviation, minimum and maximum value for each numerical attribute.

| Attribute | Type | Missing Values | Mean | Std Dev | Max | Min |
|-----------|------|---------------|------|---------|-----|-----|
| Attribute 1 | Numerical | 40 | 320.0 | 85.0 | 620.0 | 10.0 |
| Attribute 2 | Categorical | 5 | / | / | / | / |
| Attribute 3 | Numerical | 5,980 | 0.5 | 0.1 | 1.0 | 0.0 |
| Attribute 4 | Numerical | 0 | 50.0 | 4200.0 | 90000.0 | -85000.0 |
| Attribute 5 | Binary | 0 | / | / | / | / |

For each of the following cleaning steps, explain if it makes sense to apply it to this dataset. Briefly justify your answers. [0.5 mark per step]

- (a) Missing value replacement based on most frequent value.
- (b) Missing value replacement based on median value.
- (c) Removing an attribute.
- (d) Outlier removal.

---

## Question 2: Design choices [3 marks]

You trained a neural network with the following settings: 2 hidden layers with ReLU units, 16 neurons per layer, Xavier initialisation, trained for 200 epochs with a learning rate of 0.001 and L2 regularisation. The training accuracy is 58% and the validation accuracy is 56%. You know that state-of-the-art models achieve 94% on the same problem.

For each of the following suggestions, explain if it is likely to improve the validation accuracy and why. [1 mark per suggestion]

- (a) Adding dropout (rate=0.3) to each hidden layer.
- (b) Increasing the model to 5 layers with 128 neurons per layer and removing the L2 regularisation.
- (c) Using a learning rate schedule that starts at 0.01 and decays over time.

---

## Question 3: Evaluation & Confusion Matrix [4 marks]

### Part A [2 marks]

A fraud detection model is evaluated on a dataset of 10,000 transactions (100 fraudulent, 9,900 legitimate). The confusion matrix is:

|  | Actually Fraud | Actually Legitimate |
|--|---|---|
| **Predicted Fraud** | 80 | 990 |
| **Predicted Legitimate** | 20 | 8910 |

(a) Calculate the accuracy, precision, and recall. [1 mark]

(b) The bank is considering deploying this model to automatically block fraudulent transactions. Discuss whether this model is suitable for this purpose. Consider what each type of error means in this context. [1 mark]

### Part B [2 marks]

A different team builds a second fraud detection model, evaluated on the same dataset. The confusion matrix is:

|  | Actually Fraud | Actually Legitimate |
|--|---|---|
| **Predicted Fraud** | 95 | 50 |
| **Predicted Legitimate** | 5 | 9850 |

(c) Calculate the accuracy, precision, and recall for Model B. [1 mark]

(d) Compare Model A and Model B. Which model would you recommend for the bank's fraud detection system? Justify your answer. [1 mark]

---

## Question 4: Activation functions [3 marks]

(a) ReLU is the most commonly used activation function in hidden layers of deep neural networks. Explain one problem that can arise when using ReLU, and how LeakyReLU mitigates it. [1 mark]

(b) A hospital is building a neural network to screen X-ray images. The model should detect whether each of the following conditions is present: fracture, pneumonia, tumour. A single X-ray image may show multiple conditions at the same time.

What activation function would you choose for the output layer? Justify your choice by explaining why another common choice would not work here. [2 marks]

---

## Question 5: Learning rate & optimisers [4 marks]

(a) Explain in your own words what batch normalisation does and give two effects it has on the training of a neural network. [2 marks]

(b) The Adam optimiser is often described as combining the benefits of two other optimisation techniques. Name these two techniques and briefly explain what each contributes to Adam. [2 marks]

---

## Question 6: CNNs [4 marks]

Consider the following CNN architecture:

- Input images' shape: [40, 40, 3]
- Convolutional layer 1: 16 filters with kernel size = 5, stride = 2 and padding = 0 (valid).
- Max pooling layer 1: kernel size = 2, stride = 2.
- Convolutional layer 2: 32 filters with kernel size = 3, stride = 1 and padding = 1 (same).
- Max pooling layer 2: kernel size = 2, stride = 2.
- Fully connected layer 1: **?** inputs and 10 outputs.

(a) What is the number of inputs to the fully connected layer? Choose 1 answer. [1 mark]
  - i. 128
  - ii. 512
  - iii. 800
  - iv. 1152
  - v. 2048

(b) Show your workings for each layer. [3 marks]

---

**END OF MOCK EXAM 3**
