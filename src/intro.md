# COMPSCI 714 — AI Architecture and Design: Exam Killer Book

## How to Get an A in One Day (Feynman Method)

This book is reverse-engineered from **every past exam** (2024, 2025, Practice) with official marking schemes. Every concept is ranked by exam frequency.

---

## Your One-Day Battle Plan (Feynman Whiteboard Method)

> **The Feynman Technique:** Grab a blank sheet. Write the topic. Explain it out loud as if teaching a 12-year-old. When you get stuck, that's your gap. Go back, learn it, explain again.

### Morning (3 hrs) — Build Understanding

| Time | Action | What to Do |
|------|--------|-----------|
| 9:00-9:30 | Read Part 0 | Skim exam analysis + frequency map. Know what's coming. |
| 9:30-10:30 | **Whiteboard Session 1** | For each MUST topic, read only the Feynman Draft. Close book. Grab paper. **Talk out loud.** Draw diagrams. Write what you know. Find your gaps. |
| 10:30-11:30 | **Whiteboard Session 2** | Read formal sections for your gaps. Close book. Re-explain. Repeat until you can explain CNN calculations, bias-variance diagnosis, and transformer architecture from memory. |
| 11:30-12:00 | **CNN Drill** | Do 3 CNN dimension calculations by hand. This WILL be on the exam. |

### Afternoon (3 hrs) — Practice Exam Questions

| Time | Action | What to Do |
|------|--------|-----------|
| 13:00-13:55 | **Mock Exam 1** | Time yourself. 55 minutes. No book. Simulate real conditions. |
| 13:55-14:30 | Check answers | Compare with answer key. Mark your weak spots. |
| 14:30-15:25 | **Mock Exam 2** | Another timed attempt. |
| 15:25-16:00 | Review gaps | Re-read chapters for any remaining weak spots. |

### Evening (2 hrs) — Cheat Sheet + Final Review

| Time | Action | What to Do |
|------|--------|-----------|
| 19:00-20:00 | **Make cheat sheet** | Double-sided A4 handwritten (exam allows this!) |
| 20:00-21:00 | **Final Feynman pass** | Walk around. Explain each MUST topic out loud. No notes. |

---

## What to Put on Your Cheat Sheet

**Side 1 — Formulas & Calculations:**
```
CNN CONV output:  floor((n + 2p - f) / s) + 1
CNN POOL output:  floor((n - f) / s) + 1
Valid padding: p = 0    Same padding: output = input size

Accuracy  = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)
F1        = 2 * P * R / (P + R)
```

**Side 2 — Decision Trees & Key Points:**
```
DIAGNOSIS FLOWCHART:
Train HIGH, Val LOW  → Overfitting (high variance)
  → Fix: regularisation, more data, data augmentation, smaller model
Train LOW, Val LOW   → Underfitting (high bias)
  → Fix: bigger model, more features, train longer, remove regularisation
Train HIGH, Val HIGH → Good fit!

OUTPUT ACTIVATION:
Multi-class (one label)    → Softmax
Multi-label (many labels)  → Sigmoid
Regression                 → Linear (no activation)

BATCH NORM EFFECTS: faster training, reduce vanishing gradients, 
regularisation effect, less sensitive to weight init
```

---

## Exam Format

| Detail | 2025 | 2024 |
|--------|------|------|
| Time | 60 min (5 read + 55 write) | 60 min (5 read + 55 write) |
| Marks | 20 | 30 |
| Questions | 6 short-answer | 7 short-answer |
| Allowed | Double-sided **handwritten** notes | Double-sided page of notes |

**Golden rule:** "Quality over quantity" — be concise. A 3-sentence precise answer beats a full-page ramble.

---

## 考前心理建设（Mental Preparation）

> 作为中国留学生，你的 ML 概念理解可能比很多本地学生都强。你唯一需要练的是：
> 1. **先说结论**（不要铺垫）
> 2. **用题目的数字**（不要泛泛而谈）
> 3. **连接词**（because, therefore, however — 让逻辑清晰）
> 4. **不要怕犯语法错误**（内容正确比语法完美重要100倍）
>
> 记住：考官打分看的是你**理解不理解**，不是你英语好不好。
> 一个有小语法错误但逻辑清晰的答案 >> 一个语法完美但空洞的答案。
