# Exam Writing Format & Strategy

---

## Exam Rules Recap

| Detail | 2025 Format | 2024 Format |
|--------|-------------|-------------|
| Duration | 60 min (5 reading + 55 writing) | 60 min (5 reading + 55 writing) |
| Total marks | 20 | 30 |
| Questions | 6 | 7 |
| Allowed | Double-sided **handwritten** A4 | Double-sided page of notes |
| Devices | NO calculators, NO phones | Same |

**Time management:**
- 2025: ~20 marks in 55 min = ~2.75 min per mark
- 2024: ~30 marks in 55 min = ~1.83 min per mark
- **Rule of thumb:** 1 mark ≈ 2-3 minutes. If a question is worth 2 marks, spend ~5 minutes max.

---

## The 5-Minute Reading Period Strategy

During the 5-minute reading time (no writing allowed):

1. **Scan ALL questions** — count marks, identify topics
2. **Identify the calculation question** (CNN dimensions) — mentally plan the steps
3. **Identify the diagnosis question** (bias/variance from curves) — start forming your answer
4. **Plan your time allocation** — more time on high-mark questions
5. **Identify what you need from your cheat sheet** — locate formulas you'll need

---

## Answer Formatting Rules

### Rule 1: Lead with the Answer

> 💡 中文思维习惯："先铺垫再给结论"。英文学术写作相反：先给结论，再解释原因。这是中国学生最需要改变的习惯。

```
❌ "There are many factors to consider. First, we need to think about..."
✅ "No, training for 2000 epochs will not help because the model is already overfitting."
```

### Rule 2: Be Concise — Quality Over Quantity

> 💡 不要写"废话"凑字数。老师明确说了 "quality over quantity"。用3句精确的话比写半页模糊的要好。

```
❌ (half page of vague general knowledge)
✅ "This is an overfitting scenario (train 95%, val 60%). L2 regularisation will help 
    because it penalises large weights, promoting a simpler model that generalises better."
```

### Rule 3: Link to the Specific Scenario

> 💡 不要只写"正则化能防止过拟合"这种教科书式的回答。必须引用题目给的具体数字（如 train=95%, val=60%）来支撑你的判断。

```
❌ "Regularisation helps prevent overfitting." (too generic)
✅ "Since the training accuracy (95%) is much higher than validation (60%), 
    indicating overfitting, L2 regularisation is likely to help by constraining 
    model complexity." (linked to given numbers)
```

### Rule 4: Show Calculation Steps

> 💡 计算题一定要写出公式和代入过程，不能只写最终答案。即使算错了，步骤正确也能拿部分分。

```
❌ "The output is 16x16x10"
✅ "Conv output: ((50 + 2×0 - 5) / 3) + 1 = (45/3) + 1 = 15 + 1 = 16
    Output: [16, 16, 10] (10 from number of filters)"
```

### Rule 5: For "What Do You Think?" — Go Beyond Numbers

> 💡 "你怎么看"这类题不能只算数字，要解释数字背后的含义。模型到底在做什么？为什么会这样？

```
❌ "Accuracy is 60% and recall is 100%."
✅ "The accuracy is 60% and recall is 100%. This means the model predicts almost 
    everything as positive — it catches all actual positives (perfect recall) but 
    at the cost of many false positives (precision only 56%). The model appears 
    to be performing well at detecting positives, but is actually just classifying 
    nearly everything as positive."
```

---

## Answer Templates by Question Type

### Type: "Evaluate This Suggestion" (2 marks each)

```
[YES/NO — 1 mark]
[Reasoning connected to scenario — 1 mark]
```

Template:
```
[Yes/No], [suggestion] is [likely/unlikely] to improve the validation accuracy. 
The model is currently [overfitting/underfitting] (training accuracy [X]%, 
validation accuracy [Y]%). [Suggestion] [mechanism: e.g., "penalises large weights" / 
"adds more training data"] which [helps/does not help] with [overfitting/underfitting] 
because [specific reason].
```

### Type: "Calculate + Interpret" (Confusion Matrix)

```
Step 1: State formulas
Step 2: Plug in numbers
Step 3: Give result
Step 4: Interpret (what does the model actually DO?)
Step 5: Explain WHY (class imbalance? threshold too low?)
```

### Type: "Explain Concept" (2-4 marks)

```
Paragraph 1: WHAT it is (definition)
Paragraph 2: HOW it works (mechanism)
Paragraph 3: WHY it matters (benefit/purpose)
```

### Type: CNN Calculation (show workings)

```
For each layer:
  Input:   [H, W, C]
  Formula: ((H + 2p - f) / s) + 1 = ...
  Output:  [H', W', C']

Final: Flatten = H' × W' × C' = [number]
```

---

## Time Allocation Guide

### For a 20-mark exam (2025 format):
| Question | Marks | Time | Topic |
|----------|-------|------|-------|
| Q1 | 2 | 5 min | Data cleaning |
| Q2 | 3 | 8 min | Bias-variance + curves |
| Q3 | 3 | 8 min | Activation functions |
| Q4 | 4 | 10 min | Learning rate curves |
| Q5 | 4 | 12 min | Transformers |
| Q6 | 4 | 12 min | CNN calculation |

### For a 30-mark exam (2024 format):
| Question | Marks | Time | Topic |
|----------|-------|------|-------|
| Q1 | 4 | 7 min | Data preprocessing |
| Q2 | 6 | 11 min | Design choices |
| Q3 | 4 | 7 min | Confusion matrix |
| Q4 | 4 | 7 min | LR + optimisers |
| Q5 | 4 | 8 min | RNN vs Transformer |
| Q6 | 4 | 8 min | CNN calculation |
| Q7 | 4 | 7 min | DNN training |

---

## Last-Minute Reminders

1. **Read the scenario carefully** — the numbers matter (train acc, val acc, missing values count)
2. **Diagnose BEFORE prescribing** — always state overfitting/underfitting first
3. **Show your work** on calculations — partial marks are possible
4. **Cross out wrong work** — the exam says "cross out work you don't want assessed"
5. **Write clearly** — illegible answers get 0 marks
6. **Use overflow pages** if needed, but note which question on the original page

---

## 中国学生考试写作常见问题（Common Issues for Chinese Students）

### 问题 1：先写"背景"再给"结论"
```
❌ 中文习惯："首先，正则化是一种技术……它的作用是……所以我认为……"
✅ 英文习惯："Yes, L2 regularisation will help. This is because..."
```
→ 英文考试要求：**第一句话就给结论**，然后解释原因。

### 问题 2：过度使用 "can"
```
❌ "Regularisation can help to improve the model."
✅ "Regularisation is likely to improve validation accuracy by constraining model complexity."
```
→ "can" 太弱。用 "is likely to" 或 "will" 更果断、更学术。

### 问题 3：缺少因果连接
```
❌ "The model is overfitting. We should use dropout."（两句话之间没有逻辑连接）
✅ "The model is overfitting, as evidenced by the gap between training and validation accuracy. Therefore, applying dropout is likely to help by reducing co-adaptation."
```
→ 用 "as evidenced by"、"therefore"、"because" 把句子连起来。

### 问题 4：用中文直译
```
❌ "The model learned too good on the training data"
✅ "The model fits the training data too closely"

❌ "The performance is not good enough"
✅ "The model fails to generalise to unseen data"

❌ "We can use a more big model"  
✅ "Increasing the model size would help"
```

### 问题 5：不敢下判断
```
❌ "Maybe this suggestion could possibly help..."
✅ "Yes, this suggestion is likely to improve validation accuracy."
```
→ 考试要明确 YES/NO。模糊的回答拿不到分。
