# Mock Exam 3 — Answer Key & Detailed Explanations

---

## Question 1: Dataset cleaning [2 marks]

**(0.5 mark per step)**

**(a) Most frequent value imputation:**

**Yes**, for Attribute 2 (categorical, 5 missing values). Most frequent value is the standard strategy for categorical data with missing values. It is not applicable to numerical or binary attributes here (Attribute 5 has no missing values).

**(b) Median value imputation:**

**Yes**, for Attribute 1 (numerical, 40 missing values out of 6,000 — a reasonable amount). Median is preferred over mean because the max (620) is relatively far from the mean (320), and Attribute 4's extreme values (std=4200 >> mean=50) also suggest the data may contain outliers. Median is more robust to outliers than mean.

**(c) Removing an attribute:**

**Yes**, for Attribute 3 — it has 5,980 out of 6,000 values missing (99.7%). Imputing this many values would create almost entirely fabricated data, which is misleading and unlikely to help the model. It makes sense to remove this attribute completely.

**(d) Outlier removal:**

**Yes**, for Attribute 4 — the standard deviation (4,200) is much larger than the mean (50), and the range is extreme (from -85,000 to 90,000). This strongly suggests the presence of outliers that could distort model training. Outlier removal or clipping should be considered.

---

## Question 2: Design choices [3 marks]

**Diagnosis:** The model is **underfitting** (high bias). Both training (58%) and validation (56%) accuracies are low and close together, while 94% is achievable. The model lacks the capacity to capture the patterns in the data.

**(a) Adding dropout (rate=0.3):** [1 mark]

**No**, this is unlikely to improve validation accuracy. Dropout is a regularisation technique that reduces overfitting by randomly deactivating neurons during training. Since the model is already underfitting (not fitting even the training data well), adding more regularisation would further constrain the model's capacity, potentially making the underfitting worse. The model already has L2 regularisation — adding dropout on top of that would make it even harder to learn.

**(b) Increasing to 5 layers with 128 neurons and removing L2:** [1 mark]

**Yes**, this is likely to improve validation accuracy. The current model (2 layers, 16 neurons) has very limited capacity, which is the likely cause of underfitting. Increasing the number of layers and neurons gives the model more representational power to learn complex patterns. Removing L2 regularisation also makes sense because the model needs more freedom to fit the data, not less. However, after increasing capacity, overfitting should be monitored — regularisation may need to be re-introduced later if overfitting occurs.

**(c) Learning rate schedule starting at 0.01 with decay:** [1 mark]

**Yes**, this could help improve validation accuracy. The current learning rate (0.001) may be too small, causing the optimisation to converge slowly or get stuck in a poor local minimum. Starting with a higher learning rate (0.01) allows the optimiser to make larger updates and explore the loss landscape more effectively. The decay then helps the optimiser settle into a good minimum as training progresses, avoiding overshooting. This is a reasonable change for an underfitting model where slow convergence may be part of the problem.

---

## Question 3: Evaluation & Confusion Matrix [4 marks]

### Part A [2 marks]

**(a) Calculations for Model A:** [1 mark]

$$Accuracy = \frac{TP + TN}{Total} = \frac{80 + 8910}{10000} = \frac{8990}{10000} = 0.899 \text{ (89.9\%)}$$

$$Precision = \frac{TP}{TP + FP} = \frac{80}{80 + 990} = \frac{80}{1070} \approx 0.075 \text{ (7.5\%)}$$

$$Recall = \frac{TP}{TP + FN} = \frac{80}{80 + 20} = \frac{80}{100} = 0.80 \text{ (80\%)}$$

**(b) Suitability analysis for Model A:** [1 mark]

Despite the seemingly good accuracy (89.9%), this model is **not suitable** for automatically blocking fraudulent transactions.

The critical problem is the **extremely low precision (7.5%)**. Of every 1,070 transactions the model flags as fraud, only 80 are actually fraudulent — meaning **92.5% of blocked transactions are legitimate**. This would cause massive disruption: customers would have their legitimate purchases blocked constantly, leading to poor user experience and potential loss of business.

The recall (80%) is reasonable — the model catches 80% of actual fraud. But the cost of the low precision (blocking 990 legitimate transactions to catch 80 fraudulent ones) is too high for automatic blocking. The model could be used for flagging transactions for human review instead.

### Part B [2 marks]

**(c) Calculations for Model B:** [1 mark]

$$Accuracy = \frac{TP + TN}{Total} = \frac{95 + 9850}{10000} = \frac{9945}{10000} = 0.9945 \text{ (99.45\%)}$$

$$Precision = \frac{TP}{TP + FP} = \frac{95}{95 + 50} = \frac{95}{145} \approx 0.655 \text{ (65.5\%)}$$

$$Recall = \frac{TP}{TP + FN} = \frac{95}{95 + 5} = \frac{95}{100} = 0.95 \text{ (95\%)}$$

**(d) Comparison and recommendation:** [1 mark]

**Model B is clearly better** and should be recommended for the bank's fraud detection system.

| Metric | Model A | Model B | Winner |
|--------|---------|---------|--------|
| Accuracy | 89.9% | 99.45% | Model B |
| Precision | 7.5% | 65.5% | Model B |
| Recall | 80% | 95% | Model B |

Model B is superior in every metric:

- **Higher recall (95% vs 80%):** Model B catches 95 out of 100 fraudulent transactions, missing only 5. In fraud detection, high recall is critical because each missed fraud can mean significant financial loss.
- **Much higher precision (65.5% vs 7.5%):** Model B produces far fewer false alarms. Only about 1 in 3 flagged transactions is a false positive, compared to Model A where 12 out of 13 flags are false positives. This means fewer legitimate customers are impacted.
- **Higher accuracy (99.45% vs 89.9%):** Model B correctly classifies almost all transactions.

Model A's low precision makes it unusable for automatic blocking. Model B, while not perfect (its precision could still be improved), strikes a much better balance and is a viable candidate for deployment, potentially with human review for flagged transactions.

---

## Question 4: Activation functions [3 marks]

**(a) ReLU problem and LeakyReLU [1 mark]:**

A potential problem with ReLU is the **dying ReLU problem**. When a neuron's input is negative, ReLU outputs exactly 0, and the gradient is also 0. If a neuron consistently receives negative inputs (e.g., due to a large negative bias or an unfortunate weight update), it will always output 0 and its weights will never be updated — the neuron effectively "dies" and stops contributing to the network. (0.5 mark)

LeakyReLU mitigates this by replacing the zero output for negative inputs with a small slope ($\alpha x$, where $\alpha$ is typically 0.01–0.3). This ensures that even when the input is negative, there is still a small, non-zero gradient flowing back. The neuron can still receive gradient signal and recover, preventing it from dying permanently. (0.5 mark)

**(b) Output activation function for multi-label X-ray classification [2 marks]:**

The appropriate activation function is **sigmoid**. (1 mark)

Since a single X-ray can show multiple conditions simultaneously (e.g., both a fracture AND pneumonia), this is a **multi-label classification problem**. Each condition must be predicted independently — the presence of one condition does not affect the prediction of another.

**Sigmoid** outputs a probability between 0 and 1 for each output node **independently**. Each output can be interpreted as "the probability that this specific condition is present", and multiple outputs can be high at the same time.

**Softmax would not work** because softmax creates a probability distribution that sums to 1 across all outputs. This means increasing the probability of one condition would decrease the probabilities of others. If a patient has both fracture and pneumonia, softmax would suppress one to boost the other — making it impossible to correctly predict both conditions simultaneously. Softmax is designed for mutually exclusive classes, but medical conditions are not mutually exclusive. (1 mark)

---

## Question 5: Learning rate & optimisers [4 marks]

**(a) Batch normalisation [2 marks]:**

Batch normalisation normalises the activations at each layer within a mini-batch to have zero mean and unit variance, then applies learned scale ($\gamma$) and shift ($\beta$) parameters.

**Effect 1: Speeds up training / allows higher learning rates.** (1 mark)
By keeping the input distribution to each layer stable throughout training, batch normalisation reduces internal covariate shift. The activations remain in a range where gradients are meaningful (not too small for sigmoid/tanh, not too large to explode). This allows the use of higher learning rates, leading to faster convergence.

**Effect 2: Has a regularising effect.** (1 mark)
Because normalisation statistics (mean and variance) are computed per mini-batch rather than over the full dataset, each sample's normalised value depends on which other samples happen to be in the same batch. This introduces noise into the activations, similar to dropout. This noise acts as implicit regularisation, helping to prevent overfitting without explicitly adding a regularisation term.

**(b) Adam's two components [2 marks]:**

Adam combines:

**1. Momentum (from SGD with Momentum):** (1 mark)
Adam maintains an exponentially decaying average of past gradients (first moment estimate, $m_t$). This smooths the optimisation trajectory by averaging out noisy gradient fluctuations, and accelerates convergence in directions where the gradient is consistent. It helps the optimiser build up speed in consistent directions, like a ball rolling downhill.

**2. RMSProp:** (1 mark)
Adam maintains an exponentially decaying average of past squared gradients (second moment estimate, $v_t$). This provides **per-parameter adaptive learning rates**. Parameters that have had large recent gradients get smaller learning rates (prevents overshooting), while parameters with small gradients get larger learning rates (speeds up learning in flat regions of the loss landscape). This adaptation makes Adam robust across different architectures.

---

## Question 6: CNNs [4 marks]

**(a) Answer: ii. 512** [1 mark]

**(b) Step-by-step calculations:** [3 marks]

Output size of convolution: $\left\lfloor\frac{n_H + 2p - f}{s} + 1\right\rfloor \times \left\lfloor\frac{n_W + 2p - f}{s} + 1\right\rfloor \times n'_C$

Output size of pooling: $\left\lfloor\frac{n_H - f}{s} + 1\right\rfloor \times \left\lfloor\frac{n_W - f}{s} + 1\right\rfloor \times n_C$

```
Layer: Conv1 (padding = 0, stride = 2, kernel = 5)
  Input:  [40, 40, 3]
  Calc:   floor((40 + 2×0 - 5) / 2) + 1 = floor(35/2) + 1 = 17 + 1 = 18
  Output: [18, 18, 16]       ← 16 filters

Layer: MaxPool1 (kernel = 2, stride = 2)
  Input:  [18, 18, 16]
  Calc:   floor((18 - 2) / 2) + 1 = floor(16/2) + 1 = 8 + 1 = 9
  Output: [9, 9, 16]         ← depth unchanged

Layer: Conv2 (padding = 1, stride = 1, kernel = 3, same)
  Input:  [9, 9, 16]
  Calc:   floor((9 + 2×1 - 3) / 1) + 1 = floor(8) + 1 = 9
  Output: [9, 9, 32]         ← 32 filters

Layer: MaxPool2 (kernel = 2, stride = 2)
  Input:  [9, 9, 32]
  Calc:   floor((9 - 2) / 2) + 1 = floor(7/2) + 1 = 3 + 1 = 4
  Output: [4, 4, 32]         ← depth unchanged

Flatten: 4 × 4 × 32 = 512
```

**Answer: The fully connected layer has 512 inputs.**

---

**Scoring Summary:**
| Question | Topic | Marks |
|----------|-------|-------|
| Q1 | Dataset cleaning | 2 |
| Q2 | Design choices | 3 |
| Q3 | Evaluation & Confusion Matrix | 4 |
| Q4 | Activation functions | 3 |
| Q5 | Learning rate & optimisers | 4 |
| Q6 | CNN calculation | 4 |
| **Total** | | **20** |

---

## 📝 Confusion Matrix 完整答题手册

---

### 零、拿到题目怎么分析（思维流程）

拿到一道 Confusion Matrix 题，脑子里按这个顺序跑一遍：

#### Step 0：读题，搞清楚"Positive 是什么"

> 这是最容易搞混的地方。题目说的 Positive 到底是谁？

| 题目场景 | Positive 是 | Negative 是 |
|---------|-----------|-----------|
| 垃圾邮件 | Spam | Legitimate email |
| 欺诈检测 | Fraud | Legitimate transaction |
| 疾病诊断 | Has disease | Healthy |
| 质检 | Defective product | Good product |

> 确认好 Positive 之后，再去对应 Confusion Matrix 的四个格子。

#### Step 1：算完数字之后，先看三个信号

**信号 1 — 数据是否 imbalanced？**

看 Positive 和 Negative 的总数比例：
- Positive 总数 = TP + FN（实际为正的那一列加起来）
- Negative 总数 = FP + TN（实际为负的那一列加起来）

> 如果比例严重失衡（比如 1:99），accuracy 就不可信了。
> 判断方法：算一下"如果模型全猜 Negative，accuracy 是多少？" 如果这个 baseline accuracy 已经很高（比如 99%），说明 accuracy 没有参考价值。

**信号 2 — Precision 和 Recall 谁高谁低？**

| 情况 | 说明 | 模型的"性格" |
|------|------|-----------|
| Recall 高，Precision 低 | 模型很"激进"，什么都预测为 Positive | 误报多，但漏报少 |
| Precision 高，Recall 低 | 模型很"保守"，只有很确定才预测 Positive | 漏报多，但误报少 |
| 两者都高 | 模型表现好 | 理想状态 |
| 两者都低 | 模型很差 | 需要大改 |

> 考试英文：
> - 激进型："The model appears to be very sensitive (low threshold), predicting most instances as positive. This results in high recall but very low precision."
> - 保守型："The model appears to be very conservative, only predicting positive when highly confident. This results in high precision but low recall."

**信号 3 — FP 和 FN 各有多少？哪个更致命？**

这一步要结合题目场景：
- 看 FP 的数量 → 想象这些"冤枉"的后果
- 看 FN 的数量 → 想象这些"放过"的后果
- 哪个后果更严重 → 那个对应的 metric 就更重要

> 口诀：**FP 多 → Precision 差 → 误报严重；FN 多 → Recall 差 → 漏报严重**

#### Step 2：用真题示例走一遍完整分析

**示例：2024 真题 Q3（1000 instances）**

```
                Positive    Negative
Predicted +       500         400
Predicted -         0         100
```

**分析流程：**

1. **Positive 是什么？** 题目没给具体场景，只需要通用分析
2. **数据 imbalanced 吗？** Positive 总数 = 500+0 = 500，Negative 总数 = 400+100 = 500。比例 1:1，不 imbalanced
3. **算数：**
   - Accuracy = (500+100)/1000 = 60%
   - Precision = 500/(500+400) = 500/900 ≈ 55.6%
   - Recall = 500/(500+0) = 100%
4. **信号判断：** Recall=100% 但 Precision=55.6% → 模型是"激进型"
5. **具体分析：** FN=0（没有漏报），FP=400（大量误报）。模型把几乎所有东西都预测成 Positive，所以当然不会漏掉任何真正的 Positive（recall=100%），但代价是把 400 个 Negative 也错误地标成了 Positive
6. **结论（真题标答原文）：** "The model is very good at classifying true examples, but it does poorly at classifying negative examples. The model seems to be very sensitive (positive prediction threshold very low) and ends up predicting most examples as positive."

**示例：Practice Test Q4（100 instances）**

```
                Positive    Negative
Predicted +         5          20
Predicted -        10          65
```

**分析流程：**

1. **数据 imbalanced 吗？** Positive=15，Negative=85。有一定 imbalance（15:85）
2. **算数：**
   - Accuracy = (5+65)/100 = 70%
   - Recall = 5/(5+10) = 5/15 = 33.3%
3. **信号判断：** Accuracy 70% 看起来还行，但 Recall 只有 33.3%
4. **分析（标答原文）：** "The accuracy is relatively high (70%) but the recall is quite low (33%). This shows that even if the model seems to perform relatively well globally, it is not very good at predicting the positive class. This comes from class imbalance, with the positive class being the minority class here. If we care about maximising the true positives, we should consider that this model does not perform well."

#### Step 3：判断"适不适合部署"的决策树

```
题目问 "Is this model suitable?"
           │
           ▼
   有没有 class imbalance？
      │              │
     有              没有
      │              │
      ▼              ▼
  Accuracy 可信吗？   直接看 Accuracy
  （算 baseline）    是否达标
      │
      ▼
  看 Precision 和 Recall
      │
      ▼
  场景中 FP 和 FN 哪个更致命？
      │              │
   FN 更致命         FP 更致命
   (医学/欺诈)       (垃圾邮件/封号)
      │              │
      ▼              ▼
  Recall 够高吗？   Precision 够高吗？
      │              │
   够 → 可以部署     够 → 可以部署
   不够 → 不适合     不够 → 不适合
```

---

### 一、定位四个格子

```
                   Actually Positive      Actually Negative
Predicted +            TP (真阳性)             FP (假阳性 / 误报)
Predicted -            FN (假阴性 / 漏报)       TN (真阴性)
```

> 记忆口诀：**对角线是对的**（TP, TN），**反对角线是错的**（FP, FN）
> 第二个字母看"实际"：P = 实际是 Positive，N = 实际是 Negative
> 第一个字母看"对错"：T = 猜对了，F = 猜错了

---

### 二、公式速查表

| Metric | Formula | 一句话含义 | 考试英文表达 |
|--------|---------|---------|-----------|
| **Accuracy** | (TP+TN) / Total | 整体猜对了多少 | "The proportion of all predictions that are correct." |
| **Precision** | TP / (TP+FP) | 说"是"的里面，真的有多少 | "Of all instances predicted as positive, how many are actually positive." |
| **Recall** | TP / (TP+FN) | 真正"是"的里面，找到了多少 | "Of all actual positive instances, how many are correctly identified." |
| **F1** | 2PR / (P+R) | P 和 R 的调和平均 | "The harmonic mean of precision and recall, balancing both metrics." |

---

### 三、场景分析万能句式

#### A. 判断模型是否适合部署（开头句）

> "Despite the seemingly high accuracy of X%, the model is **not suitable / suitable** for deployment because..."

> "The accuracy alone is misleading in this context. The more informative metrics are precision and recall."

> "To evaluate this model, we need to consider what each type of error means in practice."

#### B. 解释 False Positive 的后果（误报）

通用模板：
> "A false positive means the model incorrectly predicts [事件] when it is actually [正常]. In this context, this would result in [具体后果]."

| 场景 | 英文表达 |
|------|--------|
| **垃圾邮件** | "A false positive means a legitimate email is incorrectly flagged as spam. The user would miss important emails, which could have serious consequences." |
| **欺诈检测** | "A false positive means a legitimate transaction is blocked. This causes customer frustration and potential loss of business." |
| **疾病筛查** | "A false positive means a healthy patient is told they may have the disease. This leads to unnecessary anxiety, follow-up tests, and medical costs." |
| **自动驾驶** | "A false positive means the system detects an obstacle that does not exist, causing unnecessary braking or swerving." |
| **工厂质检** | "A false positive means a good product is rejected, leading to waste and reduced efficiency." |

#### C. 解释 False Negative 的后果（漏报）

通用模板：
> "A false negative means the model fails to detect [事件] when it is actually present. In this context, this could lead to [具体后果]."

| 场景 | 英文表达 |
|------|--------|
| **垃圾邮件** | "A false negative means a spam email reaches the inbox. This is annoying but generally less harmful than blocking a legitimate email." |
| **欺诈检测** | "A false negative means a fraudulent transaction goes undetected, resulting in direct financial loss for the bank or customer." |
| **疾病筛查** | "A false negative means a sick patient is told they are healthy. They would not receive treatment, potentially leading to worsening condition or death." |
| **自动驾驶** | "A false negative means the system fails to detect a real obstacle, which could result in a collision — a life-threatening situation." |
| **工厂质检** | "A false negative means a defective product passes inspection and reaches customers, damaging brand reputation." |

#### D. 说明哪个 metric 更重要

**Recall 更重要时（漏报代价 >> 误报代价）：**
> "In this scenario, the cost of a false negative is much higher than the cost of a false positive. Therefore, **recall is the more critical metric** — we need to ensure that as few positive cases as possible are missed, even if it means accepting more false alarms."

> "A high recall is essential because missing a [positive case] could result in [严重后果], whereas a false positive only leads to [轻微后果]."

适用场景：疾病筛查、欺诈检测、安全系统、自动驾驶障碍检测

**Precision 更重要时（误报代价 >> 漏报代价）：**
> "In this scenario, the cost of a false positive is higher than the cost of a false negative. Therefore, **precision is the more critical metric** — we need to ensure that when the model predicts positive, it is very likely to be correct."

> "A high precision is essential because incorrectly flagging a [negative case] as positive would result in [严重后果], whereas missing a [positive case] only leads to [可接受后果]."

适用场景：垃圾邮件过滤、自动封号/封禁、推荐系统（宁缺毋滥）

**两者都重要时：**
> "In this application, both false positives and false negatives have significant consequences. Therefore, the F1 score, which balances precision and recall, is the most appropriate metric."

#### E. Accuracy 陷阱（Class Imbalance）

> "Although the accuracy appears high at X%, this is **misleading due to class imbalance**. The dataset contains [N positive] out of [Total] instances ([比例]). A naive model that simply predicts every instance as negative would achieve [Y%] accuracy without detecting any positive cases at all. Therefore, accuracy is not a reliable metric here — precision and recall provide a much more meaningful evaluation."

具体套用示例（以本题 Q3 Part A 为例）：
> "The accuracy is 89.9%, but this is misleading because the dataset is heavily imbalanced (only 100 fraud cases out of 10,000 transactions, or 1%). A model that predicts every transaction as legitimate would already achieve 99% accuracy. The precision of 7.5% reveals the real problem: the model flags too many legitimate transactions as fraud."

#### F. 模型对比句式

> "Model B outperforms Model A across all metrics: higher accuracy (X% vs Y%), higher precision (X% vs Y%), and higher recall (X% vs Y%)."

> "While Model A has higher recall, Model B has significantly better precision. Given that [场景分析], Model B is the better choice because..."

> "There is a trade-off between the two models: Model A prioritises recall ([X%]) at the expense of precision ([Y%]), while Model B achieves better precision ([X%]) with slightly lower recall ([Y%]). For this application, [选择] is more appropriate because..."

#### G. 提出改进建议

> "To improve this model, the classification threshold could be adjusted. Lowering the threshold would increase recall (catching more positive cases) but decrease precision (more false alarms). Raising the threshold would have the opposite effect."

> "One practical solution is to use the model for **flagging rather than automatic action**. Flagged cases can be reviewed by a human, combining the model's detection ability with human judgment to reduce false positives."

> "The model could be retrained with **class weighting** or **oversampling** of the minority class to improve its sensitivity to positive cases."

---

### 四、答题模板（完整结构）

遇到 Confusion Matrix 题，按这个顺序写：

```
Step 1: 算数（写公式 + 代入 + 结果）
  Accuracy = (TP + TN) / Total = ... = X%
  Precision = TP / (TP + FP) = ... = X%
  Recall = TP / (TP + FN) = ... = X%

Step 2: 判断整体表现（一句话）
  "The model has high/low accuracy/precision/recall."

Step 3: 场景分析（这才是得分关键）
  "In this context, a false [positive/negative] means..."
  "Therefore, [precision/recall] is the more critical metric."

Step 4: 结论
  "This model is / is not suitable for deployment because..."
  "To improve, we could..."
```
