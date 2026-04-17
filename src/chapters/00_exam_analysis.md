# Exam Question-by-Question Analysis

> Source: 2025 S1 Test + 2024 S1 Test + Practice Test (with official answers)

---

## 2025 S1 Mid-Semester Test (20 marks, 6 questions)

### Q1: Dataset Cleaning [2 marks]
| Field | Detail |
|-------|--------|
| Type | Data table analysis → justify 4 cleaning steps |
| Module | A: Data Preprocessing |
| Difficulty | ★☆☆ |
| Keywords | missing values, median imputation, attribute removal, outlier detection |
| Intent | Can you read dataset statistics and make cleaning decisions? |

**The Trick:** Attribute 4 has 9995/10000 missing values → remove entirely. Attribute 2 has extreme min/max relative to mean → outliers exist. No missing values in categorical/binary → no need for most-frequent imputation.

---

### Q2: Evaluation and Design Choices [3 marks]
| Field | Detail |
|-------|--------|
| Type | (a) Interpret loss curves → diagnose bias/variance (b) Suggest 2 improvements |
| Module | A: Bias-Variance |
| Difficulty | ★★☆ |
| Keywords | overfitting, high variance, high bias, regularisation, data augmentation |
| Intent | Can you read training curves and prescribe fixes? |

**The Trick:** Gap between training and validation = high variance (overfitting). Training loss still relatively high = possible high bias too. Each suggestion must target a DIFFERENT aspect.

---

### Q3: Activation Functions [3 marks]
| Field | Detail |
|-------|--------|
| Type | (a) Explain dying ReLU + LeakyReLU fix (b) Choose output activation for multi-label |
| Module | B: MLP / Activation Functions |
| Difficulty | ★★☆ |
| Keywords | ReLU, LeakyReLU, dying neurons, sigmoid, multi-label vs multi-class |
| Intent | Do you understand activation function failure modes and design choices? |

**The Trick:** Multi-label (multiple anomalies per image) = sigmoid (independent per output). NOT softmax (which forces probabilities to sum to 1).

---

### Q4: Learning Rate [4 marks]
| Field | Detail |
|-------|--------|
| Type | Match 4 loss curves to 4 learning rates |
| Module | A: Optimization |
| Difficulty | ★★☆ |
| Keywords | divergence, convergence, overshooting, learning rate |
| Intent | Can you visually identify learning rate effects? |

**The Trick:** Diverging (loss goes up) = 0.5. Slow descent = 0.001. Fast convergence to HIGH loss = 0.1 (overshoots optimum). Best convergence to LOW loss = 0.01.

---

### Q5: Transformers [4 marks]
| Field | Detail |
|-------|--------|
| Type | (a) Explain masked attention in decoder (b) Explain ViT class token |
| Module | B: Transformer |
| Difficulty | ★★★ |
| Keywords | masked attention, autoregressive, ViT, [CLS] token, classification |
| Intent | Deep understanding of Transformer variants |

**The Trick:** (a) Mask prevents looking at future tokens → preserves autoregressive property during training. (b) [CLS] token aggregates info from all patches → efficient classification without processing all embeddings separately.

---

### Q6: CNNs [4 marks]
| Field | Detail |
|-------|--------|
| Type | (a) Multiple choice: FC layer inputs (b) Show calculation |
| Module | B: CNN |
| Difficulty | ★★☆ |
| Keywords | valid padding, same padding, convolution, max pooling, flatten |
| Intent | Can you compute dimensions through a CNN pipeline? |

**Answer: 180.** Pipeline: [35,35,3] → Conv1(valid,k=7,s=2) → [15,15,10] → Pool1(k=2,s=2) → [7,7,10] → Conv2(same,k=3,s=1) → [7,7,20] → Pool2(k=2,s=2) → [3,3,20] → Flatten = 180.

---

## 2024 S1 Mid-Semester Test (30 marks, 7 questions)

### Q1: Data Preprocessing [4 marks]
| Field | Detail |
|-------|--------|
| Type | Infer data characteristics from preprocessing pipeline |
| Module | A: Data Preprocessing |
| Difficulty | ★★☆ |
| Intent | Can you reverse-engineer what raw data looks like from the pipeline? |

**Pipeline 1** (median imputer → standardisation → log transform): Numerical data, missing values, different scales, heavy-tailed distribution.

**Pipeline 2** (most-frequent imputer → one-hot encoding): Categorical data, missing values, no ordinal relationship, not too many categories.

---

### Q2: Design Choices [6 marks] — HIGHEST VALUE QUESTION
| Field | Detail |
|-------|--------|
| Type | Overfitting scenario (train=95%, val=60%), evaluate 3 fixes |
| Module | A: Bias-Variance |
| Difficulty | ★★☆ |

- **More epochs:** NO — worsens overfitting
- **Larger dataset:** YES — more diverse data helps generalise
- **L2 regularisation:** YES — penalises large weights, promotes simpler model

---

### Q3: Evaluation [4 marks]
| Field | Detail |
|-------|--------|
| Type | Confusion matrix → calculate metrics → interpret |
| Module | E: Metrics |

**Results:** Accuracy=60%, Recall=100%, Precision=56%. The model predicts almost everything as positive. Looks like it catches all positives (perfect recall) but actually just labels everything positive (terrible precision).

---

### Q4: Learning Rate and Optimisers [4 marks]
| Field | Detail |
|-------|--------|
| Type | (1) LR schedule example + benefit (2) Explain momentum |

**Key answers:** (1) Exponential decay — fast at start, fine-tune near optimum. (2) Momentum = exponentially decaying average of past gradients → smoother updates, speeds up convergence.

---

### Q5: RNN and Transformer [4 marks]
| Field | Detail |
|-------|--------|
| Type | (1) Sequential processing: advantage AND drawback (2) How Transformer fixes it |

**Key:** (1) Advantage: naturally captures order. Drawback: can't parallelise → slow for long sequences. (2) Transformer: processes all tokens in parallel via embeddings + adds positional encoding for order.

---

### Q6: CNN Feature Map [4 marks]
| Field | Detail |
|-------|--------|
| Type | Calculate dimensions after conv and pooling layers |

**Answers:** Conv: ((50+0-5)/3)+1 = 16 → [16,16,10]. AvgPool: ((50-5)/5)+1 = 10 → [10,10,5]. MaxPool: same dimensions (only values differ).

---

### Q7: DNN Training [4 marks]
| Field | Detail |
|-------|--------|
| Type | (1) Why deep nets are hard to train (2) Two strategies to help |

**Key:** (1) Vanishing/exploding gradients + overfitting + longer training. (2) Batch norm, skip connections (ResNet), better optimisers (Adam), LSTM/GRU.

---

## Practice Test (~32 marks, 7 questions)

### Q1: Data Pre-processing [5 marks]
Two approaches to missing data + when to use each. Remove attribute (when mostly missing) or impute values (when reasonable amount missing).

### Q2: DNN and Generalisation [5 marks]
High bias → underfitting → increase model, add data, transfer learning. High variance → overfitting → regularisation, more data, reduce model.

### Q3: Design Choices [6 marks]
**Underfitting** scenario (train=val=50%). Increase size = YES. Zero init = NO (symmetry problem). Dropout = NO (regularisation doesn't help underfitting).

### Q4: Evaluation [3 marks]
Accuracy=70%, Recall=33%. Accuracy misleading due to class imbalance — model bad at finding positives.

### Q5: Batch Normalisation [5 marks]
Effects: speeds up training, reduces vanishing gradients, regularisation effect, reduces weight init sensitivity.

### Q6: Attention and Transformers [4 marks]
Multi-head attention = stacks multiple attention heads with separate Q/K/V. Benefit: focuses on different aspects simultaneously.

### Q7: CNNs [5 marks]
Reverse-engineer hyperparameters from diagram. Early layers = edge detectors (low-level features), deeper layers = complex features.
