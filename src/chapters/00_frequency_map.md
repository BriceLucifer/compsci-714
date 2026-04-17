# Exam Topic Frequency Map

---

## The Heat Map: What WILL Be on Your Exam

| Topic | 2025 | 2024 | Practice | Count | Priority |
|-------|------|------|----------|-------|----------|
| **Bias-Variance / Design Choices** | Q2 (3m) | Q2 (6m) | Q2+Q3 (11m) | **4** | **MUST** |
| **CNN Calculations** | Q6 (4m) | Q6 (4m) | Q7 (5m) | **3** | **MUST** |
| **Transformer / Attention** | Q5 (4m) | Q5 (4m) | Q6 (4m) | **3** | **MUST** |
| **Data Preprocessing** | Q1 (2m) | Q1 (4m) | Q1 (5m) | **3** | **MUST** |
| **Learning Rate / Optimizers** | Q4 (4m) | Q4 (4m) | — | **2** | HIGH |
| **Confusion Matrix Metrics** | — | Q3 (4m) | Q4 (3m) | **2** | HIGH |
| **Activation Functions** | Q3 (3m) | — | — | **1** | MED |
| **RNN vs Transformer** | — | Q5 (4m) | — | **1** | MED |
| **DNN Training Challenges** | — | Q7 (4m) | — | **1** | MED |
| **Batch Normalisation** | — | — | Q5 (5m) | **1** | MED |

---

## Priority Guide

| Priority | Rule | Your Action |
|----------|------|-------------|
| **MUST** | Every exam, >= 3 appearances | Master completely. Can explain on whiteboard from memory. |
| **HIGH** | 2 out of 3 exams | Understand well. Can calculate and explain. |
| **MED** | 1 out of 3 exams | Know key points. Can write 3-4 sentences if asked. |

---

## The 80/20 Rule: 4 Topics = ~65% of All Marks

### 1. Bias-Variance + Design Choices (~20% of all marks)
- Diagnose overfitting vs underfitting from numbers/curves
- For each fix: say YES/NO + link to the specific diagnosis
- **Never confuse:** regularisation fights overfitting, NOT underfitting

### 2. CNN Calculations (~15% of all marks)
- Two formulas: conv output + pool output
- Practice multi-layer pipeline calculations
- Know valid vs same padding

### 3. Transformer / Attention (~15% of all marks)
- Masked attention = prevent seeing future tokens
- Multi-head attention = multiple perspectives simultaneously
- ViT: patches → embeddings → [CLS] token → classification

### 4. Data Preprocessing (~15% of all marks)
- Which imputation for which data type
- When to remove attribute vs impute
- Read pipeline → infer data characteristics

### + 2 More for Safety (~20% more marks)

5. **Learning Rate** — curve shapes, momentum, LR schedules
6. **Confusion Matrix** — calculate accuracy/precision/recall, spot class imbalance traps

---

## Total Marks by Topic (All Exams Combined)

```
Bias-Variance/DC    ████████████████████  20 marks
CNN                 █████████████         13 marks
Transformer         ████████████          12 marks
Data Preprocessing  ███████████           11 marks
Learning Rate       ████████              8 marks
Eval Metrics        ███████               7 marks
Batch Norm          █████                 5 marks
DNN Training        ████                  4 marks
RNN                 ████                  4 marks
Activation Func     ███                   3 marks
```
