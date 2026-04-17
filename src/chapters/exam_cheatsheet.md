# 考场速查卡 — 从中文思维到英文输出

> **用法：** 脑子想到中文 → 找到对应英文零件 → 用万能连接词拼起来。不需要翻译，只需要组装。

---

## 万能连接词（只需要这 5 个）

| 你脑子里想说的 | 直接写 |
|---|---|
| 因为... | **This is because...** |
| 所以... | **As a result, ...** / **This leads to...** |
| 但是... | **However, ...** |
| 相比之下... | **Unlike [A], [B]...** / **While [A]..., [B]...** |
| 我建议... | **I would suggest... because...** |

---

## 答题公式（每种题型一个模板）

### 题型 1："这个建议能不能改善模型？"

```
[YES/NO], [建议] is likely to [improve/not improve] validation accuracy.

The model is currently [overfitting/underfitting], as evidenced by
[说出你看到的证据].

[建议] [helps/does not help] because [一句话机制].
```

**实战例子（你脑子里想的 → 写出来的）：**

| 中文思维 | 英文输出 |
|---|---|
| 过拟合了，train高val低 | "The model is overfitting, as the training accuracy (95%) is much higher than the validation accuracy (60%)." |
| 加正则化能帮忙 | "L2 regularisation is likely to help because it penalises large weights, constraining model complexity." |
| 欠拟合不能加dropout | "Dropout will NOT help because the model is underfitting — dropout further constrains an already limited model." |
| 多训练几轮会更差 | "More epochs will worsen overfitting because the model will continue to memorise training noise." |

---

### 题型 2："解释一个概念"

```
[概念] is [一句话定义].

It works by [机制].

This is [beneficial/important] because [为什么有用].
```

**高频概念直接背：**

| 中文 | 英文零件（直接写） |
|---|---|
| 注意力机制 | "Attention computes a weighted sum of values, where weights reflect the relevance of each input position." |
| 遮蔽注意力 | "Masking prevents each position from attending to future tokens, preserving the autoregressive property." |
| 多头注意力 | "Multi-head attention runs several attention functions in parallel, each focusing on different aspects of the input." |
| 位置编码 | "Positional encoding is needed because the Transformer processes all positions in parallel, losing inherent ordering." |
| [CLS] token | "[CLS] is a learnable token that aggregates information from all patches via attention for classification." |
| Dropout | "Dropout randomly deactivates neurons during training, forcing the network to learn redundant representations." |
| Batch Norm | "Batch normalisation normalises activations within each mini-batch, keeping gradients in a healthy range." |
| L2 正则化 | "L2 regularisation penalises large weights, encouraging simpler and more generalisable models." |
| 梯度消失 | "Gradients are multiplied through many layers. With sigmoid (max derivative 0.25), they shrink to near zero." |
| 死亡ReLU | "If a neuron consistently receives negative inputs, ReLU outputs zero and the neuron stops learning permanently." |
| 动量 | "Momentum maintains a running average of past gradients, smoothing updates and accelerating convergence." |
| Adam优化器 | "Adam combines momentum (past gradient direction) with adaptive per-parameter learning rates, making it effective for deep networks." |
| RNN隐藏状态 | "Each time step takes the current input AND the previous hidden state: h_t = f(W·h_{t-1} + U·x_t + b)." |
| LSTM门控 | "LSTM uses three gates (forget, input, output) to control information flow, solving the vanishing gradient problem." |
| 残差连接 | "Skip connections add the input directly to the output: y = F(x) + x, allowing gradients to flow through the shortcut." |

---

### 题型 3："看图说话（loss curves / metrics）"

```
The [loss curve / metric] shows that [你看到了什么].

This indicates [诊断].

[建议/解释] because [原因].
```

| 中文思维 | 英文零件 |
|---|---|
| loss在震荡 | "The loss curve oscillates and fails to converge." |
| loss发散了 | "The loss diverges, increasing over epochs." |
| train和val之间有gap | "There is a significant gap between training and validation loss." |
| 两条线都很高 | "Both training and validation loss remain high." |
| 学习率太大 | "This indicates the learning rate is too high, causing the optimisation to overshoot the minimum." |
| 学习率太小 | "This suggests the learning rate is too small, resulting in very slow convergence." |
| 准确率高但recall低 | "Despite high accuracy, the low recall indicates the model fails to identify most positive instances." |
| 类别不平衡 | "This is due to class imbalance — the model achieves high accuracy by simply predicting the majority class." |

---

### 题型 4："CNN 计算"

不需要造句，只需要写步骤。模板：

```
Conv layer:
  Input: [H, W, C]
  Output: [floor((H + 2p - f) / s) + 1, same for W, num_filters]

Pool layer:
  Input: [H, W, C]
  Output: [floor((H - f) / s) + 1, same for W, C]  (depth unchanged)

Flatten: H × W × C = [answer]
```

---

### 题型 5："对比 A 和 B"

```
While [A] [A的特点], [B] [B的特点].

The key advantage of [A] is [优势].

However, [A]'s limitation is [缺点], which [B] addresses by [B的解决方式].
```

| 中文思维 | 英文零件 |
|---|---|
| RNN按顺序处理 | "RNNs process tokens sequentially, naturally capturing order." |
| Transformer并行 | "Transformers process all positions in parallel using self-attention." |
| RNN不能并行是缺点 | "Sequential processing prevents parallelisation, making training slow for long sequences." |
| Transformer用位置编码补顺序 | "The Transformer compensates for the loss of order information by adding positional encoding." |
| CNN有局部性 | "CNNs have a strong inductive bias towards locality and translation invariance." |
| ViT更灵活但需要大数据 | "ViT makes fewer assumptions, offering more flexibility, but requires large-scale pretraining data." |

---

## 高频 Chinglish 修正（只改这几个就够）

| 你可能会写 | 改成 |
|---|---|
| "The model performance is not good" | "The model performs poorly on validation data" |
| "It can make the model more better" | "It is likely to improve generalisation" |
| "The reason is because..." | "This is because..." |
| "prevent to overfit" | "prevent overfitting" |
| "the accuracy is high so the model is good" | "despite high accuracy, the model may be ineffective due to class imbalance" |
| "add more regularisation to make it good" | "applying regularisation constrains model complexity, reducing overfitting" |

---

## 最终检查：写完每道题看一眼

- [ ] 有没有写 YES/NO 然后接 because？
- [ ] 关键术语拼对了没？（regularisation, overfitting, gradient, convergence）
- [ ] 有没有用具体数字（"95% vs 60%"）而不是模糊描述（"high vs low"）？

---

## 逻辑答题万能框架（Universal Answer Logic Framework）

### 所有 "评价建议" 题的万能思路：
```
第一步（诊断）：看 train acc 和 val acc → 判断过拟合/欠拟合
第二步（判断）：这个建议能不能解决诊断出的问题？
第三步（输出）：YES/NO + 用英文写原因
```

### 答题逻辑链模板（每道题都能用）：
```
观察 → 诊断 → 建议 → 原因
Observe → Diagnose → Suggest → Explain

"The training accuracy is [X]% while validation accuracy is [Y]%."  （观察）
→ "This indicates [overfitting/underfitting]."                      （诊断）
→ "[Suggestion] is [likely/unlikely] to help."                      （建议）
→ "This is because [mechanism]."                                     （原因）
```

### 答题字数控制：
| 分值 | 目标字数 | 结构 |
|------|---------|------|
| 1 分 | 1-2 句 | 结论 |
| 2 分 | 2-3 句 | 结论 + 原因 |
| 3-4 分 | 4-6 句 | 结论 + 诊断 + 原因 + 机制 |
| 5-6 分 | 1-2 段 | 完整分析（每个要点 2-3 句） |
