# Teacher's Exam Style Analysis

---

## Core Philosophy

> "We privilege quality over quantity" — concise, clear, correct.

The teacher tests **applied understanding**, not memorisation. Every question gives a scenario and asks you to reason about it.

---

## Question Patterns That Repeat Every Exam

### Pattern 1: "Evaluate These Suggestions" (EVERY EXAM)

**Format:** Given model settings + results, evaluate 2-3 suggestions.

**How to nail it:**
1. FIRST: diagnose the problem (overfitting or underfitting?)
2. THEN: for each suggestion, say YES/NO
3. THEN: explain WHY by connecting to your diagnosis

**Scoring:** 2 marks each (1 for answer, 1 for reasoning connected to scenario)

| Scenario | Diagnosis | What Helps | What Doesn't |
|----------|-----------|------------|-------------|
| Train HIGH, Val LOW | Overfitting | Regularisation, more data, data aug | More epochs, bigger model |
| Train LOW, Val LOW | Underfitting | Bigger model, more features | Regularisation, dropout |

---

### Pattern 2: CNN Dimension Calculation (EVERY EXAM)

**Format:** Given architecture spec → compute output at each layer → find FC input size.

**How to nail it:** Write this for EVERY layer:
```
[Layer Name]
  Input:  [H, W, C]
  Formula: ((H + 2p - f) / s) + 1
  Output: [H', W', C']
```

---

### Pattern 3: Transformer Two-Part Question (EVERY EXAM)

**Format:** (a) Explain mechanism X. (b) Why is it useful?

**How to nail it:** Part (a) = WHAT it does. Part (b) = WHY it matters (concrete benefit).

---

### Pattern 4: Loss Curve / Metric Interpretation (2/3 EXAMS)

**Format:** Given graph or numbers → diagnose + suggest fix.

---

## Traps the Teacher Sets (And How to Avoid Them)

| Trap | What Students Do Wrong | Correct Answer |
|------|----------------------|----------------|
| Underfitting + regularisation | "Use dropout to improve!" | NO — dropout fights overfitting, this is underfitting |
| Multi-label output activation | "Use softmax" | NO — sigmoid (independent per output) |
| Zero weight initialisation | "Smaller weights = better" | NO — zero creates symmetry, neurons can't differentiate |
| More epochs when overfitting | "Train longer to learn more" | NO — worsens overfitting |
| High accuracy with imbalanced data | "70% accuracy = good model" | Check precision/recall — might just predict majority class |
| Max vs Avg pooling output size | "Different pooling = different size" | SAME size, only values differ |

---

## Sentence Patterns in Questions → What They Want

| Question Says | They Actually Want |
|---|---|
| "Explain if it is likely to improve..." | YES/NO + reasoning linked to the specific scenario |
| "Describe performance in terms of bias and variance" | Identify overfitting/underfitting from curves |
| "Briefly justify" | 2-3 sentences MAX with the key reason |
| "Show your calculation steps" | Formula → numbers → result (at each layer) |
| "What do you think about this model?" | Go BEYOND numbers — what is the model actually doing? |
| "Explain in your own words" | Show understanding, not textbook recitation |

---

## Concepts That Always Appear Together

```
Bias-Variance ←→ Regularisation ←→ Design Choices
(one question covers all three — master the connections)

CNN Dimensions ←→ Valid/Same Padding ←→ FC Layer Size
(pipeline calculation from start to end)

Transformer ←→ Masked Attention ←→ Positional Encoding ←→ ViT
(mechanism + why it exists)

Loss Curves ←→ Learning Rate ←→ Optimizers
(visual diagnosis skill)

Confusion Matrix ←→ Class Imbalance ←→ Misleading Accuracy
(numbers game — always check precision AND recall)
```
