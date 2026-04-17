# English Expression Guide for the Exam

> This exam is written and answered in English. These templates help you write clear, precise, high-scoring answers.

---

## Universal Answer Structures

### Structure 1: "Evaluate a Suggestion" (most common question type)

```
[YES/NO], [suggestion] is [likely/unlikely] to improve validation accuracy.

This is because the current model is [overfitting/underfitting], as evidenced by 
[training accuracy being much higher/lower than validation accuracy].

[Suggestion] works by [mechanism], which [helps/does not help] with 
[overfitting/underfitting] because [specific reason].
```

**Example:**
"Yes, L2 regularisation is likely to improve validation accuracy. The current model is overfitting, as the training accuracy (95%) is much higher than the validation accuracy (60%). L2 regularisation penalises large weights, encouraging the model to learn a simpler, more generalisable representation, which helps reduce overfitting."

### Structure 2: "Explain Concept X" 

```
[Concept] is [one-sentence definition].

It works by [mechanism in 1-2 sentences].

This is beneficial/important because [why it matters].
```

### Structure 3: "Interpret Model Performance"

```
The [metric] is [value], which indicates [what this means].

However, [other metric] reveals that [deeper insight].

This is because [explanation of model behavior, e.g., class imbalance, 
predicting everything as one class].
```

### Structure 4: "Compare A and B"

```
While [A] [feature of A], [B] [feature of B].

The key advantage of [A] is [advantage], whereas [B] excels at [advantage].

However, [A]'s main drawback is [drawback], which [B] addresses by [solution].
```

---

## Topic-Specific Sentence Templates

### Data Preprocessing（数据预处理 — 考察你能否从pipeline步骤反推数据特征）
- "The use of [median/most frequent] imputation suggests the data is [numerical/categorical] with missing values."
- "The standardisation step indicates that features are on different scales."
- "The log transformation suggests the data has a heavy-tailed distribution."
- "Removing the attribute is justified because [X]% of values are missing, and imputation would create misleading information."
- "Outlier removal is appropriate because the maximum value ([X]) is significantly larger than expected given the mean ([Y]) and standard deviation ([Z])."

### Bias-Variance（偏差-方差 — 考察你能否从train/val数字诊断问题并给出建议）
- "The model displays high variance, as there is a clear gap between the training and validation [accuracy/loss]."
- "This indicates overfitting, where the model fits the training data too closely but fails to generalise."
- "The model appears to have high bias, as both training and validation accuracies are low."
- "This suggests underfitting — the model is not complex enough to capture the underlying patterns."
- "Applying regularisation can help reduce overfitting by limiting the complexity of the model."
- "Increasing the model size may help address underfitting by giving the model more capacity to learn."

### CNN（卷积神经网络 — 考察维度计算和结构优势解释）
- "The output dimensions of the convolutional layer are calculated as: floor((n + 2p - f) / s) + 1."
- "With valid padding (p=0), the spatial dimensions of the output will be smaller than the input."
- "With same padding, the output spatial dimensions match the input spatial dimensions when stride is 1."
- "The depth of the output equals the number of filters applied."
- "Pooling reduces the spatial dimensions while preserving the depth."
- "Max pooling and average pooling produce output with the same dimensions; only the values differ."

### Transformer & Attention（注意力机制 — 考察位置编码、遮蔽、多头注意力的作用）
- "The masking in the decoder prevents each position from attending to future tokens."
- "This preserves the autoregressive property, ensuring that predictions depend only on previously generated tokens."
- "Multi-head attention runs several attention functions in parallel, each with its own learned weight matrices."
- "This allows the model to focus on different aspects of the input simultaneously."
- "The [CLS] token in ViT aggregates information from all image patches for the final classification."
- "Positional encoding is necessary because the Transformer processes all positions in parallel, losing inherent ordering."

### Learning Rate & Optimizers（学习率与优化器 — 考察loss曲线诊断和优化器选择）
- "A diverging loss curve indicates a learning rate that is too high, causing the optimisation to overshoot."
- "A very slowly decreasing loss suggests the learning rate is too small."
- "Learning rate scheduling, such as exponential decay, allows faster initial convergence while avoiding overshooting near the optimum."
- "The momentum mechanism maintains an exponentially decaying average of past gradients, smoothing the optimisation trajectory."

### Evaluation Metrics（评估指标 — 考察混淆矩阵计算和类别不平衡下的指标选择）
- "The accuracy is calculated as (TP + TN) / (TP + TN + FP + FN) = ..."
- "Despite the seemingly acceptable accuracy, the model performs poorly at identifying positive instances."
- "The high recall but low precision indicates the model predicts most instances as positive."
- "This discrepancy highlights the importance of examining metrics beyond accuracy, particularly with imbalanced datasets."

### Activation Functions（激活函数 — 考察sigmoid/softmax/ReLU的选择和死亡ReLU问题）
- "The dying ReLU problem occurs when neurons consistently receive negative inputs, causing them to output zero and stop learning."
- "LeakyReLU mitigates this by introducing a small positive slope for negative inputs."
- "For multi-label classification, sigmoid is the appropriate output activation because each output is treated independently."
- "Softmax is unsuitable for multi-label problems because it forces all outputs to sum to 1."

### Batch Normalisation（批量归一化 — 考察BN的两个效果：加速训练+正则化）
- "Batch normalisation speeds up training by normalising activations within each mini-batch."
- "It reduces the risk of vanishing and exploding gradients by keeping activations in a healthy range."
- "The normalisation over mini-batches introduces noise, which has a regularising effect."
- "It also reduces sensitivity to weight initialisation by automatically adjusting activation distributions."

### Regularisation (L1, L2, Dropout, Early Stopping)（正则化 — 考察过拟合时的解决方案及其机制）
- "L2 regularisation penalises large weights, encouraging the model to learn a simpler, more generalisable representation."
- "L1 regularisation drives some weights to exactly zero, performing automatic feature selection."
- "Dropout randomly deactivates neurons during training, forcing the network to learn redundant, distributed representations."
- "This prevents co-adaptation, where specific neurons become overly reliant on each other."
- "Early stopping halts training when validation loss stops improving, preventing the model from memorising training noise."
- "Regularisation constrains model complexity, which helps when the model is overfitting but worsens underfitting."

### RNN / LSTM / GRU（循环神经网络 — 考察顺序处理优缺点和梯度消失的解决）
- "RNNs process tokens sequentially, naturally capturing temporal order without additional mechanisms."
- "However, sequential processing prevents parallelisation, making training slow for long sequences."
- "Vanilla RNNs suffer from vanishing gradients because gradients are multiplied through many time steps."
- "LSTM mitigates this by introducing a cell state and gating mechanisms (forget, input, output gates) that control information flow."
- "The forget gate decides what information to discard, while the input gate controls what new information to store."
- "GRU simplifies LSTM by combining the forget and input gates into a single update gate, reducing the number of parameters."

---

## 逻辑连接词完整指南（Logic Connectors for Exam Answers）

> 中国学生最常犯的逻辑问题不是内容错误，而是句子之间缺少逻辑连接。下面的连接词能让你的答案读起来像母语者写的。

### 因果关系（Cause & Effect）
| 中文逻辑 | 英文表达 | 用法示例 |
|---|---|---|
| 因为...所以... | **This is because... As a result, ...** | "This is because the learning rate is too high. As a result, the loss diverges." |
| 由于... | **Due to... / Owing to...** | "Due to class imbalance, accuracy is misleading." |
| 导致了... | **This leads to... / This causes...** | "This leads to vanishing gradients in early layers." |
| ...的原因是... | **The reason [X] is that...** | "The reason overfitting occurs is that the model has too many parameters relative to the data." |

### 转折关系（Contrast & Concession）
| 中文逻辑 | 英文表达 | 用法示例 |
|---|---|---|
| 但是/然而 | **However, ... / Nevertheless, ...** | "However, this approach fails when the model is underfitting." |
| 虽然...但是... | **Although/While [X], [Y]** | "While accuracy appears high at 70%, the recall of only 33% reveals poor performance." |
| 相反 | **In contrast, ... / Conversely, ...** | "In contrast, the Transformer processes all positions in parallel." |
| 尽管如此 | **Despite this, ...** | "Despite the high accuracy, the model performs poorly on the minority class." |

### 递进关系（Addition & Elaboration）
| 中文逻辑 | 英文表达 | 用法示例 |
|---|---|---|
| 而且/此外 | **Furthermore, ... / Moreover, ... / Additionally, ...** | "Furthermore, batch normalisation has a regularising effect." |
| 具体来说 | **Specifically, ... / In particular, ...** | "Specifically, dropout randomly deactivates neurons during training." |
| 换句话说 | **In other words, ... / That is, ...** | "In other words, the model has memorised the training noise." |

### 总结关系（Conclusion & Summary）
| 中文逻辑 | 英文表达 | 用法示例 |
|---|---|---|
| 因此/所以 | **Therefore, ... / Thus, ... / Hence, ...** | "Therefore, L2 regularisation is likely to improve validation accuracy." |
| 总之 | **In summary, ... / Overall, ...** | "Overall, the model is overfitting and would benefit from regularisation." |
| 综上所述 | **Based on the above analysis, ...** | "Based on the above analysis, the suggestion is unlikely to help." |

---

## Common Mistakes in English Writing

| Wrong | Right | Why |
|-------|-------|-----|
| "The model has a good performance" | "The model performs well" | More natural |
| "It can help to improve the accuracy" | "It is likely to improve the accuracy" | More academic |
| "The reason is because..." | "This is because..." | Redundant construction |
| "More bigger model" | "A larger model" | Comparative form |
| "The data have..." | "The data have..." or "The dataset has..." | Both acceptable |
| "Prevent to overfit" | "Prevent overfitting" | Gerund after "prevent" |
| "It will for sure improve" | "It is likely to improve" | Hedge appropriately |

---

## Power Words for High-Scoring Answers

| Instead of | Use |
|-----------|-----|
| "better" | "more generalisable", "more robust" |
| "bad" | "suboptimal", "poor", "degraded" |
| "the gap" | "the discrepancy between training and validation" |
| "too good at training data" | "fits the training data too closely" |
| "learns too much" | "memorises noise in the training data" |
| "doesn't work well" | "fails to generalise to unseen data" |
| "makes the model simpler" | "constrains model complexity" |
| "helps with overfitting" | "has a regularising effect" |
