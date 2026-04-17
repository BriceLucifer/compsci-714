# CLAUDE.md — AI Design & Architecture Exam Preparation System

## 项目概述 / Project Overview

本项目使用 **mdBook**（Rust）构建一套完整的 AI Design & Architecture 考试备考知识库。
Claude Code 的任务是：分析 `input/` 中的历年真题 → 识别考察规律 → 生成 `src/` 中结构化的 mdBook 章节。

```
project/
├── CLAUDE.md          ← 本文件，指令中枢
├── input/             ← 历年真题（只读，仅用于分析）
│   └── *.pdf / *.txt / *.md
├── src/               ← mdBook 内容目录（写入目标）
│   ├── SUMMARY.md     ← mdBook 目录（必须维护）
│   └── chapters/      ← 各章节 .md 文件
└── book.toml          ← mdBook 配置文件
```

---

## 第一阶段：真题分析（Analysis Phase）

### 任务 1 — 扫描所有真题

读取 `input/` 下的全部文件，对每道题执行以下分析，并输出 `src/chapters/00_exam_analysis.md`：

```
对每道题标注：
- 题号 / 年份 / 题型（选择/简答/论述/计算/设计题）
- 核心考点（一句话）
- 涉及的知识模块（见下方模块列表）
- 难度估计（★☆☆ / ★★☆ / ★★★）
- 关键词（用于后续检索）
- 命题意图（老师想考察什么能力？）
```

### 任务 2 — 生成频率热力图报告

统计每个知识模块被考察的次数，输出 Markdown 表格，格式：

| 知识模块 | 出现频次 | 占比 | 优先级 |
|---------|---------|------|--------|
| Neural Network Architectures | 8 | 32% | 🔴 必考 |
| ... | ... | ... | ... |

优先级判定：
- 🔴 必考（频次 ≥ 全题 15% 或近三年必出）
- 🟠 高频（频次 10–14%）
- 🟡 中频（频次 5–9%）
- 🟢 低频（频次 < 5%）

### 任务 3 — 命题风格分析

识别该老师的出题偏好并写入分析报告：
- 偏好理论推导 / 工程实现 / 对比分析 / 案例设计？
- 常用句式模式（"Explain the trade-off between..."、"Design a system that..."）
- 哪些概念经常被放在一起考（共现分析）
- 常见陷阱题型（易混淆概念）

---

## 第二阶段：知识模块定义

### 核心知识模块（AI Design & Architecture）

以下为考试核心模块，分析时按此分类，写作时每模块对应一个章节：

#### Module A — Foundational ML Concepts
- Supervised / Unsupervised / Reinforcement Learning 定义与边界
- Bias-Variance Tradeoff（偏差-方差权衡）
- Overfitting / Underfitting 及解决方案（Regularization, Dropout, Early Stopping）
- Cross-validation 策略（k-fold, stratified）
- Loss functions 选择逻辑（MSE, Cross-Entropy, Hinge, etc.）
- Gradient Descent 变体（SGD, Adam, RMSProp, Momentum）

#### Module B — Neural Network Architectures
- MLP（多层感知机）前向/反向传播推导
- CNN（卷积神经网络）：卷积层、池化层、感受野计算
- RNN / LSTM / GRU：序列建模、梯度消失问题
- Attention Mechanism（注意力机制）原理
- Transformer 架构：Self-Attention, Multi-Head Attention, Positional Encoding
- BERT / GPT 系列架构差异
- ResNet / VGG / EfficientNet 等经典 CV 架构

#### Module C — System Design & Architecture
- AI System Design 流程（需求 → 数据 → 模型 → 部署 → 监控）
- Model Serving 架构（REST API, gRPC, batch inference, streaming）
- Scalability 设计（水平扩展、负载均衡、缓存策略）
- Data Pipeline 设计（ETL, Feature Store, Data Versioning）
- MLOps 概念（CI/CD for ML, model registry, A/B testing）
- Microservices vs Monolithic 在 AI 系统中的取舍
- Latency vs Throughput 权衡

#### Module D — Training Infrastructure
- Distributed Training（数据并行 vs 模型并行）
- GPU/TPU 架构基础与内存管理
- Mixed Precision Training（FP16/BF16）
- Gradient Accumulation / Checkpointing
- Hyperparameter Tuning（Grid Search, Random Search, Bayesian Optimization）

#### Module E — Model Evaluation & Deployment
- Metrics 体系：Accuracy, Precision, Recall, F1, AUC-ROC, mAP
- Confusion Matrix 解读
- Model Compression（Pruning, Quantization, Knowledge Distillation）
- A/B Testing 设计与统计显著性
- Concept Drift / Data Drift 检测与应对
- Shadow Deployment / Canary Release
- Responsible AI：Fairness, Explainability（SHAP, LIME）, Privacy

#### Module F — Specialized Domains
- NLP Pipeline（Tokenization, Embedding, Fine-tuning）
- Computer Vision Pipeline（Augmentation, Transfer Learning）
- Recommendation Systems（Collaborative Filtering, Content-Based, Hybrid）
- Reinforcement Learning 基础（MDP, Q-Learning, Policy Gradient）
- GAN 架构与训练技巧
- Multimodal Models 基本概念

---

## 第三阶段：内容生成规则（Writing Rules）

### 每个章节必须包含以下结构

~~~markdown
# [章节标题]

## 🎯 考试重要度
[优先级标签] | 历年出现 [N] 次

## 📖 核心概念（Core Concepts）
[英文术语 + 中文对照 + 一句话定义]

## 🧠 费曼草稿（Feynman Draft）
[用最简单的语言解释，假装对一个完全不懂的人讲解]
[使用类比、比喻、具体例子]
[避免一开始使用术语，先建立直觉]

## 📐 正式定义（Formal Definition）
[精确的学术定义，包含数学公式（如适用）]

## 🔄 机制与推导（How It Works）
[分步骤解释工作原理]
[关键公式推导过程]

## ⚖️ 权衡分析（Trade-offs & Comparisons）
[与相关概念的对比表格]
[适用场景 vs 不适用场景]

## 🏗️ 设计题答题框架
[如果老师出设计题，标准答题结构是什么]
[用 WHAT → WHY → HOW → TRADE-OFF → EXAMPLE 框架]

## 📝 历年真题示例
[从 input/ 中找到的相关真题，附标准答题思路]

## 🌐 英语表达要点（English Expression）
[考试中描述此概念的常用句式]
[易错表达 / 易混淆词汇]
[高分答题用词建议]

## ✅ 自测检查清单
- [ ] 能用英文一句话定义此概念？
- [ ] 能画出结构图/流程图？
- [ ] 知道至少一个实际应用案例？
- [ ] 能解释其优缺点？
- [ ] 能与相关概念区分开？
~~~

### 费曼学习法执行标准

在"费曼草稿"部分，严格遵守：

1. **第一句话必须是比喻**
   - 错误：「Attention mechanism is a component that...」
   - 正确：「Imagine you are reading a long book and trying to answer a question. You don't re-read every word — you skim for relevant parts. Attention works exactly like that.」

2. **使用日常词汇建立直觉**，再引入术语

3. **每个抽象概念配一个具体数字例子**（小 toy example）

4. **主动暴露常见误解**：
   ```
   ⚠️ Common Misconception: Many students think [X], but actually [Y] because [Z].
   ```

5. **结尾用一句话总结核心直觉**：
   ```
   💡 Core Intuition: [一句话，不超过25词]
   ```

---

## 第四阶段：英语写作专项支持

> 针对非母语考生，在每个章节额外生成此部分，并汇总写入 `src/chapters/english_expressions.md`

### 考试英语表达模板库

#### 解释类题目句式
```
- "[Concept] refers to the process of..."
- "In essence, [X] is a mechanism that enables..."
- "The key idea behind [X] is that..."
- "To put it simply, [X] allows a model to..."
```

#### 对比分析句式
```
- "While [A] focuses on..., [B] is designed to..."
- "The fundamental difference between [A] and [B] lies in..."
- "Unlike [A], which requires..., [B] operates by..."
- "[A] tends to excel when..., whereas [B] is preferred when..."
```

#### 设计题答题句式
```
- "I would design this system by first..."
- "The rationale for choosing [X] over [Y] is..."
- "A key trade-off to consider here is..."
- "This approach scales well because..."
- "One potential limitation is..., which can be mitigated by..."
```

#### 因果推理句式
```
- "This leads to [problem] because..."
- "As a result of [X], we observe that..."
- "The reason [X] outperforms [Y] in this scenario is..."
```

#### 高频易错词汇对照
为每个模块列出：
- 易拼错的专业词汇
- 英文中常被混淆的近义词（如 parameter vs hyperparameter）
- 中文直译易出错的表达

---

## 第五阶段：mdBook 文件结构要求

### `src/SUMMARY.md` 结构模板

每次新增章节后，**必须同步更新 SUMMARY.md**：

~~~markdown
# Summary

[Introduction](./intro.md)

# 📊 Part 0 — Exam Analysis
- [真题分析报告](./chapters/00_exam_analysis.md)
- [考点频率分布](./chapters/00_frequency_map.md)
- [命题风格分析](./chapters/00_teacher_style.md)

# 🧱 Part A — Foundational ML Concepts
- [Overview](./chapters/A_overview.md)
- [Bias-Variance Tradeoff](./chapters/A_bias_variance.md)
- [Optimization & Gradient Descent](./chapters/A_optimization.md)
- [Regularization Techniques](./chapters/A_regularization.md)

# 🏛️ Part B — Neural Network Architectures
- [Overview](./chapters/B_overview.md)
- [MLP & Backpropagation](./chapters/B_mlp.md)
- [CNN](./chapters/B_cnn.md)
- [RNN / LSTM / GRU](./chapters/B_rnn.md)
- [Transformer & Attention](./chapters/B_transformer.md)
- [Modern LLM Architectures](./chapters/B_llm.md)

# 🏗️ Part C — System Design & Architecture
- [Overview](./chapters/C_overview.md)
- [AI System Design Framework](./chapters/C_design_framework.md)
- [Model Serving](./chapters/C_serving.md)
- [MLOps](./chapters/C_mlops.md)
- [Scalability Patterns](./chapters/C_scalability.md)

# ⚙️ Part D — Training Infrastructure
- [Overview](./chapters/D_overview.md)
- [Distributed Training](./chapters/D_distributed.md)
- [Hardware Basics](./chapters/D_hardware.md)

# 📏 Part E — Evaluation & Deployment
- [Overview](./chapters/E_overview.md)
- [Metrics Deep Dive](./chapters/E_metrics.md)
- [Model Compression](./chapters/E_compression.md)
- [Responsible AI](./chapters/E_responsible_ai.md)

# 🎯 Part F — Specialized Domains
- [NLP Pipeline](./chapters/F_nlp.md)
- [Computer Vision Pipeline](./chapters/F_cv.md)

# 🌐 English Expression Guide
- [通用句式模板](./chapters/english_expressions.md)
- [专业词汇速查](./chapters/vocabulary.md)
- [答题格式规范](./chapters/exam_writing_format.md)

# 🧪 Mock Exams
- [模拟题 1（按真题格式）](./chapters/mock_exam_1.md)
- [模拟题答案与解析](./chapters/mock_exam_1_answers.md)
~~~

### 文件命名规范
- 全部小写，下划线分隔
- 前缀为模块字母（A_, B_, C_...）
- 描述性名称，不超过 30 字符

---

## 第六阶段：模拟题生成规则

分析完真题后，在 `src/chapters/mock_exam_*.md` 中生成模拟题：

### 模拟题生成标准

1. **严格模仿真题格式**（题型分布、分值比例）
2. **覆盖所有 🔴 必考 和 🟠 高频 模块**
3. **每道设计题附标准答题框架**（不直接给答案，给思路骨架）
4. **包含"易错提示"**：标注历年考生常犯的错误
5. **英语难度与真题匹配**：不简化词汇，但提供关键词提示

模拟题格式：

~~~markdown
## Question [N] ([分值] marks)

[题目原文，英文]

---
### 💡 Answer Framework (for self-assessment)

**Key concepts to address:**
- Point 1: ...
- Point 2: ...

**Structure your answer as:**
1. Define [X]
2. Explain mechanism
3. Discuss trade-offs
4. Give example

**Common mistakes to avoid:**
- ❌ Don't confuse [A] with [B]
- ❌ Don't forget to mention [C]

**Scoring rubric (estimated):**
- Definition (2 pts): ...
- Mechanism (3 pts): ...
- Example (2 pts): ...
~~~

---

## 执行顺序（Claude Code 应按此顺序操作）

```
Step 1: 读取所有 input/ 文件，执行分析
Step 2: 生成 00_exam_analysis.md（真题详细分析）
Step 3: 生成 00_frequency_map.md（频率热力图）
Step 4: 生成 00_teacher_style.md（命题风格）
Step 5: 按优先级从高到低，依次生成各模块章节
         （先生成 🔴 必考模块，再生成 🟠🟡🟢）
Step 6: 生成 english_expressions.md 和 vocabulary.md
Step 7: 生成至少 2 套模拟题
Step 8: 最后更新 SUMMARY.md，确保所有文件已链接
Step 9: 验证所有 src/ 中的内链接有效
```

---

## 质量检查清单（每个章节完成后自检）

- [ ] 费曼草稿以比喻开头？
- [ ] 有具体数字 toy example？
- [ ] 标注了 Common Misconception？
- [ ] 有设计题答题框架？
- [ ] 有英语表达模板？
- [ ] SUMMARY.md 已更新？
- [ ] 文件命名符合规范？
- [ ] 历年真题中相关题目已引用？
- [ ] 知识点与模块分类一致？

---

## 特别说明（对 Claude Code 的提示）

1. **保持英文章节主体内容为英文**，批注/提示可用中文，方便非母语读者
2. **所有专业术语首次出现时标注中文**，格式：`Attention Mechanism（注意力机制）`
3. **数学公式使用 MathJax 兼容格式**：行内 `$ $`，独立公式 `$$ $$`
4. **图示用 ASCII art 或 Mermaid 代码块**（mdBook 支持 Mermaid）
5. **如遇真题不清晰**，在分析报告中标注 `[UNCLEAR]` 并给出最合理的推断
6. **考试是英文考试**：所有答题模板、模拟题答案框架必须用英文写
7. **假设读者有 CS 基础但没学过 ML**：解释不要过于简单，也不要跳步骤
8. **保证读者带着思考学习，强化读者的学习思路**

---

*运行日志（Claude Code 每次执行后追加）：*
