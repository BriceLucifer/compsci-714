# ✍️ Output Practice — Express It Yourself

> **How to use this chapter:**
> 1. Pick a topic you just reviewed
> 2. Close all notes
> 3. Write your answer on paper or in a blank document — do NOT type into this page
> 4. Only open the self-check and reference answer after you have finished writing
>
> The goal is not to get it perfect. The goal is to discover what you *think* you know but cannot yet *say*.

---

## A1 — Bias-Variance Tradeoff

### Level 1 — Core Intuition (30 seconds)
**Prompt:** What is overfitting? Explain it without using the word "overfitting."

<details>
<summary>📖 Reference Answer</summary>

The model has learned the training data too closely, including its noise and random patterns, so it performs well on the training set but poorly on unseen data. It has essentially memorised the training examples rather than learning general patterns.

</details>

---

### Level 2 — Exam Paragraph (3 minutes)
**Prompt:** A model achieves 95% training accuracy but only 62% validation accuracy. Diagnose the problem and suggest two solutions. Explain *why* each solution works.

> 🧠 中文思路：95% vs 62% → 差距大 → 过拟合 → 两个解决办法各写一句为什么有效

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Correct diagnosis: high variance / overfitting?
- [ ] Used the train–val gap as evidence?
- [ ] Named at least two specific solutions (dropout, L2, more data, early stopping…)?
- [ ] Explained *why* each solution reduces overfitting — not just named them?
- [ ] Did NOT suggest "add more layers" as a fix?

</details>

<details>
<summary>📖 Reference Answer</summary>

The model displays **high variance (overfitting)**. The large gap between training accuracy (95%) and validation accuracy (62%) indicates that the model has learned to fit the training data very closely but fails to generalise to unseen data. The model is likely too complex relative to the amount of training data available.

**Solution 1: Apply dropout regularisation (e.g., rate = 0.3–0.5).** Dropout randomly deactivates a proportion of neurons during each training step. This prevents co-adaptation of neurons — the network cannot rely on any single neuron — forcing it to learn more robust, distributed representations. This effectively reduces the model's capacity during training without changing the architecture, reducing the gap between training and validation performance.

**Solution 2: Add L2 regularisation.** L2 regularisation adds a penalty term proportional to the squared magnitude of the weights to the loss function. This discourages large weight values and pushes the model towards simpler, smoother decision boundaries. The result is a more generalisable model that is less likely to memorise noise in the training data.

</details>

---

### Level 3 — Analysis (5–7 minutes)
**Prompt:** Your colleague says: "Whenever validation loss rises, just add dropout." Evaluate this advice. When is it correct? When does it backfire?

> 🧠 中文思路：先说什么时候对（过拟合时）→ 再说什么时候错（欠拟合时）→ 用 train/val 数字区分两种情况

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Identified when the advice is valid (overfitting / high variance)?
- [ ] Identified when it backfires (underfitting / high bias)?
- [ ] Used train vs. val accuracy to distinguish the two cases?
- [ ] Explained *why* dropout makes underfitting worse?
- [ ] Suggested what to do instead in the underfitting case?

</details>

<details>
<summary>📖 Reference Answer</summary>

This advice is **partially correct but dangerously incomplete**.

**When it is correct:** If the model is overfitting — high training accuracy but low validation accuracy, and the validation loss starts rising while training loss continues to decrease — then dropout can help. In this case, the rising validation loss indicates the model is memorising training noise. Dropout forces the network to learn more robust features by preventing co-adaptation of neurons, which reduces the train–val gap.

**When it backfires:** If the model is underfitting — both training and validation accuracy are low and close together — then adding dropout would make the situation *worse*. Dropout reduces the effective capacity of the model by randomly deactivating neurons. An underfitting model already lacks sufficient capacity to capture the patterns in the data. Adding dropout would further constrain it, leading to even lower training accuracy and no improvement in validation performance.

**What to do instead for underfitting:** Increase model capacity (more layers, more neurons), train for more epochs, use a higher learning rate, or remove existing regularisation (L2, dropout) that may be over-constraining the model.

The key diagnostic is to always check *both* training and validation metrics before prescribing a solution: overfitting requires regularisation; underfitting requires more capacity.

</details>

---

## A2 — Optimisation & Learning Rate

### Level 1 — Core Intuition (30 seconds)
**Prompt:** What does the learning rate control? Explain it without using a formula.

<details>
<summary>📖 Reference Answer</summary>

The learning rate controls the size of each step the optimiser takes when updating the model's weights. A large learning rate means big steps (fast but may overshoot the optimal point), while a small learning rate means small steps (precise but may be very slow to converge or get stuck).

</details>

---

### Level 2 — Exam Paragraph (3 minutes)
**Prompt:** A training loss curve oscillates wildly and never converges. What is the most likely cause? How would you fix it?

> 🧠 中文思路：loss震荡不收敛 → 学习率太大 → 解释为什么（步子太大跳过最优点）→ 怎么修

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Identified learning rate too high as the cause?
- [ ] Explained the mechanism: large steps overshoot the minimum?
- [ ] Suggested a concrete fix: reduce learning rate, or use a schedule?
- [ ] Mentioned at least one alternative (momentum, Adam) if relevant?

</details>

<details>
<summary>📖 Reference Answer</summary>

The most likely cause is that the **learning rate is too high**. When the learning rate is too large, the gradient updates overshoot the minimum of the loss landscape — the optimiser jumps back and forth across the optimal point without settling down, causing the oscillating behaviour.

**Fix 1:** Reduce the learning rate to a smaller value (e.g., from 0.1 to 0.01 or 0.001). This allows the optimiser to take smaller, more controlled steps towards the minimum.

**Fix 2:** Use a learning rate schedule (e.g., step decay or exponential decay). Start with a relatively high learning rate for fast initial progress, then reduce it over time so the optimiser can make finer adjustments as it approaches the optimum.

**Fix 3:** Use an adaptive optimiser like Adam, which automatically adjusts the effective learning rate per parameter. Parameters with large recent gradients receive smaller updates, which naturally dampens oscillations.

</details>

---

### Level 3 — Analysis (5–7 minutes)
**Prompt:** Compare SGD, SGD with momentum, and Adam. In what situation would you prefer each?

> 🧠 中文思路：三个优化器各写一段 → SGD最简单 → Momentum加了动量 → Adam自适应 → 各说什么时候好用

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Described what plain SGD does (and its weakness: noisy, slow)?
- [ ] Explained momentum as accumulating past gradient direction?
- [ ] Explained Adam as adaptive per-parameter learning rate?
- [ ] Gave a plausible reason to prefer each (e.g. Adam = good default; SGD+momentum = more stable for large-batch training)?
- [ ] Did NOT just list them without comparing?

</details>

<details>
<summary>📖 Reference Answer</summary>

**Plain SGD** computes the gradient on a mini-batch and updates weights in the opposite direction. Its simplicity is its strength, but it has two weaknesses: (1) noisy updates due to mini-batch variance can cause the optimisation path to zigzag, and (2) it uses a single learning rate for all parameters, which may not suit problems where different parameters have different gradient scales.

**SGD with Momentum** improves on plain SGD by maintaining an exponentially decaying average of past gradients. This smooths out noisy fluctuations and accelerates convergence in directions where the gradient is consistently pointing the same way. It is preferred in large-scale training (e.g., ImageNet) where practitioners want fine control over the optimisation process and can afford to tune the learning rate carefully. It often generalises slightly better than Adam.

**Adam** combines momentum (first moment) with RMSProp (second moment — adaptive per-parameter learning rates). Parameters with large recent gradients receive smaller updates, and vice versa. Adam is preferred as a **default choice** because it works well out-of-the-box across a wide range of problems with minimal hyperparameter tuning. It is especially useful when starting a new project or when computational resources for hyperparameter search are limited.

</details>

---

## A3 — Regularisation

### Level 1 — Core Intuition (30 seconds)
**Prompt:** What is L2 regularisation doing to the weights, in plain English?

<details>
<summary>📖 Reference Answer</summary>

L2 regularisation penalises large weight values by adding the sum of squared weights to the loss function. This encourages the model to keep weights small and spread out, resulting in a simpler, smoother model that is less likely to overfit.

</details>

---

### Level 2 — Exam Paragraph (3 minutes)
**Prompt:** Explain two distinct effects of batch normalisation on model training.

> 🧠 中文思路：Batch norm两个效果 → 每个写"做了什么"+"为什么有用" → 不要和dropout搞混

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Named two distinct effects (e.g. faster training / acts as regulariser / reduces internal covariate shift / allows higher lr)?
- [ ] Explained the *mechanism* behind each effect — not just labelled them?
- [ ] Used the word "normalise" correctly (zero mean, unit variance per batch)?
- [ ] Did NOT confuse batch norm with dropout?

</details>

<details>
<summary>📖 Reference Answer</summary>

**Effect 1: Speeds up training and allows higher learning rates.** Batch normalisation normalises the activations within each mini-batch to have zero mean and unit variance. This keeps the input distribution to each layer stable throughout training, reducing internal covariate shift. Because the activations remain in a well-behaved range, gradients are less likely to vanish or explode, allowing the use of higher learning rates and leading to faster convergence.

**Effect 2: Acts as implicit regularisation.** Because the normalisation statistics (mean and variance) are computed per mini-batch rather than over the entire dataset, each sample's normalised value depends on which other samples happen to be in the same mini-batch. This introduces noise into the activations, similar to dropout. This stochastic noise acts as a form of regularisation, helping to prevent overfitting without explicitly adding a regularisation term.

</details>

---

### Level 3 — Analysis (5–7 minutes)
**Prompt:** A model is underfitting (train=55%, val=54%). A teammate suggests adding dropout. Evaluate this suggestion.

> 🧠 中文思路：先判断欠拟合 → 然后说dropout会让情况更糟 → 因为dropout减少了模型容量 → 最后说应该怎么做

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Correctly identified the problem as high bias / underfitting?
- [ ] Clearly stated the suggestion is *wrong* in this case?
- [ ] Explained why: dropout further constrains an already under-powered model?
- [ ] Suggested better alternatives (bigger model, more epochs, remove regularisation, add features)?
- [ ] Structured your answer: diagnose → evaluate suggestion → recommend alternative?

</details>

<details>
<summary>📖 Reference Answer</summary>

The model is **underfitting (high bias)**. Both training accuracy (55%) and validation accuracy (54%) are low and close together, indicating the model is unable to capture the underlying patterns in the data. The problem is insufficient model capacity, not excessive memorisation.

Adding dropout would **make the situation worse**. Dropout is a regularisation technique designed to combat overfitting by randomly deactivating neurons during training. This effectively reduces the model's capacity. Since the model is already struggling to learn the training data, further reducing its capacity would decrease training accuracy even further, with no benefit to validation accuracy.

**Better alternatives:**
- Increase the model size — add more layers and/or more neurons per layer to give the model more representational power.
- Remove or reduce existing regularisation (e.g., if L2 is already applied, reduce or remove it).
- Increase the learning rate or switch to an adaptive optimiser like Adam — the model may be converging too slowly.
- Train for more epochs — the model may not have had enough time to learn.

</details>

---

## A4 — Data Preprocessing

### Level 1 — Core Intuition (30 seconds)
**Prompt:** Why is median imputation preferred over mean imputation when a feature has outliers?

<details>
<summary>📖 Reference Answer</summary>

The mean is sensitive to extreme values — a single outlier can pull the mean far from the typical value. The median is the middle value of the sorted data, so it is robust to outliers and better represents the central tendency of the data.

</details>

---

### Level 2 — Exam Paragraph (3 minutes)
**Prompt:** A preprocessing pipeline contains: median imputer → standard scaler → log transform. What does this tell you about the raw data?

> 🧠 中文思路：从每个pipeline步骤反推原始数据特征 → median说明有异常值 → scaler说明量纲不同 → log说明分布偏

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Median imputer → data has missing values?
- [ ] Standard scaler → features have different scales / not zero-mean?
- [ ] Log transform → distribution is right-skewed / heavy-tailed?
- [ ] Did you reason from each step *back* to the raw data, not forward?

</details>

<details>
<summary>📖 Reference Answer</summary>

- **Median imputer** → The raw data is **numerical with missing values**. The choice of median over mean suggests the data likely has **outliers or a skewed distribution**, since the median is more robust to extreme values than the mean.
- **Standardisation** → The raw data has **features on different scales**. Standardisation (zero mean, unit variance) ensures that all features contribute equally and that no single feature dominates due to its scale.
- **Log transformation** → The distribution of some features is likely **right-skewed or has a heavy tail** (e.g., income, house prices). Log transformation compresses large values and spreads small values, making the distribution closer to normal, which helps many machine learning models perform better.

</details>

---

### Level 3 — Analysis (5–7 minutes)
**Prompt:** You receive a dataset with 3 numerical columns (with outliers and missing values) and 2 categorical columns. Design a full preprocessing pipeline and justify each step.

> 🧠 中文思路：数值和分类分开处理 → 数值：插补→处理异常值→标准化 → 分类：插补→编码 → 每步说为什么

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Handled missing values separately for numerical and categorical?
- [ ] Applied scaling to numerical features?
- [ ] Applied encoding (one-hot or ordinal) to categorical?
- [ ] Addressed outliers (log transform, clipping, or robust scaler)?
- [ ] Justified *why* each step was chosen, not just listed them?

</details>

<details>
<summary>📖 Reference Answer</summary>

**For the 3 numerical columns:**
1. **Impute missing values using median.** Median is preferred over mean because the data contains outliers, and the median is robust to extreme values.
2. **Handle outliers** using clipping (cap values at a percentile, e.g., 1st and 99th) or log transformation if the distribution is right-skewed. This prevents outliers from dominating the model's learning.
3. **Standardise** (zero mean, unit variance) so that all numerical features are on the same scale and no single feature dominates due to magnitude differences.

**For the 2 categorical columns:**
1. **Impute missing values using the most frequent value** (mode). This is the standard strategy for categorical data, as mean/median are not applicable.
2. **Apply one-hot encoding** to convert categories into binary vectors. This is appropriate when there is no natural ordering between categories. If the number of categories is very large, alternative methods like target encoding could be considered.

**Pipeline summary:**
```
Numerical: Median imputer → Outlier handling → Standardisation
Categorical: Mode imputer → One-hot encoding
```

</details>

---

## B1 — MLP & Backpropagation

### Level 1 — Core Intuition (30 seconds)
**Prompt:** Why is ReLU preferred over sigmoid in hidden layers? One sentence.

<details>
<summary>📖 Reference Answer</summary>

ReLU avoids the vanishing gradient problem that plagues sigmoid — for positive inputs, its gradient is always 1, allowing gradients to flow freely through deep networks, whereas sigmoid's gradient is at most 0.25 and approaches 0 for large or small inputs.

</details>

---

### Level 2 — Exam Paragraph (3 minutes)
**Prompt:** Explain the vanishing gradient problem and one technique that mitigates it.

> 🧠 中文思路：先解释梯度消失原因（链式法则乘很多层）→ 再说sigmoid导数最大0.25 → 最后说解决方案

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Explained the cause: gradients are multiplied through many layers via chain rule?
- [ ] Explained the effect: early layers stop learning / receive near-zero gradients?
- [ ] Linked to sigmoid specifically (outputs in 0–1, derivatives always < 0.25)?
- [ ] Named a valid solution: ReLU, skip connections (ResNet), batch norm, LSTM?
- [ ] Explained *why* the solution helps, not just named it?

</details>

<details>
<summary>📖 Reference Answer</summary>

During backpropagation, gradients are computed using the chain rule, which involves multiplying the gradients of each layer together. In a deep network with sigmoid activations, the derivative of sigmoid is at most 0.25 and typically much smaller. When these small values are multiplied across many layers, the gradient decreases **exponentially** — by the time it reaches the early layers, it is effectively zero. As a result, the early layers receive almost no gradient signal and their weights are barely updated, making it extremely difficult for the network to learn features in these layers.

**Mitigation: Use ReLU activation functions.** ReLU outputs 0 for negative inputs and the input itself for positive inputs. For positive values, the gradient is exactly 1, so multiplying gradients across layers does not cause them to shrink. This allows gradients to flow freely through the network, enabling effective training of deep architectures. ReLU is now the default activation for hidden layers in most deep networks.

</details>

---

### Level 3 — Analysis (5–7 minutes)
**Prompt:** You initialise all weights in a network to 0. Describe exactly what happens during training and why this is a problem.

> 🧠 中文思路：全0权重 → 前向传播所有神经元输出一样 → 反向传播梯度一样 → 对称性问题 → 永远学不出不同特征

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Described what happens at forward pass: all neurons output the same value?
- [ ] Described what happens at backward pass: all gradients are identical?
- [ ] Named the problem: symmetry — neurons never differentiate from each other?
- [ ] Explained the consequence: the network behaves like a single neuron regardless of depth?
- [ ] Mentioned the fix: random initialisation (Xavier, He)?

</details>

<details>
<summary>📖 Reference Answer</summary>

If all weights are initialised to 0, every neuron in a given layer will compute the exact same output during the forward pass (since they all apply the same zero weights to the same inputs). During backpropagation, all neurons receive identical gradients, and all weights are updated by the same amount. This means every neuron in a layer remains identical to every other neuron in that layer — they never differentiate from each other.

This is called the **symmetry problem**. Regardless of how many neurons the network has, they all behave as a single neuron because they can never develop different features. The network's effective capacity is reduced to that of a single neuron per layer, making it unable to learn complex patterns.

The solution is to use **random initialisation** (e.g., Xavier initialisation or He initialisation), which breaks the symmetry by giving each neuron different initial weights. This allows neurons to compute different outputs, receive different gradients, and ultimately learn to detect different features.

</details>

---

## B2 — CNN

### Level 1 — Core Intuition (30 seconds)
**Prompt:** What does a convolutional filter detect? One sentence.

<details>
<summary>📖 Reference Answer</summary>

A convolutional filter slides across the input and detects a specific local pattern (such as an edge, texture, or colour gradient) by computing the dot product between its weights and each local region of the input.

</details>

---

### Level 2 — Exam Paragraph (3 minutes)
**Prompt:** Calculate the output dimensions of: Input [32, 32, 3] → Conv layer (32 filters, kernel=3, stride=1, padding=0). Show your working.

> 🧠 中文思路：写公式 → 代入数字 → 算出空间维度 → 深度 = 滤波器数量 → 记住别把滤波器深度和输出深度搞混

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Used the correct formula: output = floor((input + 2p − kernel) / stride) + 1?
- [ ] Got spatial dimensions: (32 + 0 − 3)/1 + 1 = 30 → output [30, 30, 32]?
- [ ] Correctly set depth = number of filters (32)?
- [ ] Did NOT confuse depth of output with depth of filter?

</details>

<details>
<summary>📖 Reference Answer</summary>

Using the formula: $\text{output} = \lfloor\frac{n + 2p - f}{s}\rfloor + 1$

- Input: [32, 32, 3]
- $n = 32$, $p = 0$ (valid padding), $f = 3$ (kernel size), $s = 1$ (stride)
- Output spatial size: $\lfloor(32 + 2 \times 0 - 3) / 1\rfloor + 1 = \lfloor 29 \rfloor + 1 = 30$
- Number of output channels = number of filters = 32

**Output: [30, 30, 32]**

Note: the depth of the filter (3, matching the input channels) does NOT appear in the output — the output depth is determined solely by the number of filters.

</details>

---

### Level 3 — Analysis (5–7 minutes)
**Prompt:** Why are CNNs more suitable than fully connected MLPs for image data? Give at least two structural reasons.

> 🧠 中文思路：两个核心优势 → 参数共享（同一个滤波器全图共用）→ 局部连接（只看周围像素）→ 用参数数量对比说明

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Mentioned parameter sharing: the same filter is reused across all positions?
- [ ] Mentioned local connectivity: each neuron only sees a local patch, not all pixels?
- [ ] Mentioned translation invariance or equivariance?
- [ ] Gave a rough parameter count comparison to illustrate the efficiency gain?
- [ ] Did NOT just say "CNN is better at images" without explaining the mechanism?

</details>

<details>
<summary>📖 Reference Answer</summary>

**1. Local connectivity (sparse connections).** In an MLP, every neuron is connected to every input pixel, which ignores the spatial structure of images. In a CNN, each neuron only connects to a small local region (the receptive field). This is appropriate for images because relevant features (edges, textures) are local — a pixel's meaning depends primarily on its neighbours, not on distant pixels. This drastically reduces the number of parameters.

**2. Parameter sharing.** A convolutional filter uses the same set of weights at every spatial position in the input. This means a filter that detects a vertical edge in the top-left corner can also detect it in the bottom-right corner, without needing separate weights for each position. In contrast, an MLP would need separate weights for each spatial position. For a 224×224×3 input with 64 filters of size 3×3: CNN needs 64×3×3×3 = 1,728 weights, while an MLP with 64 hidden neurons would need 224×224×3×64 = 9,633,792 weights.

**3. Translation equivariance.** Because the same filter is applied at every position, CNNs naturally detect features regardless of where they appear in the image. A cat in the top-left produces the same feature activations as a cat in the bottom-right (shifted accordingly). This built-in property means CNNs do not need to learn the same pattern separately for every possible position.

</details>

---

## B3 — RNN / LSTM / GRU

### Level 1 — Core Intuition (30 seconds)
**Prompt:** Why do vanilla RNNs struggle with long sequences? One sentence.

<details>
<summary>📖 Reference Answer</summary>

Because gradients are multiplied through many time steps during backpropagation, they shrink exponentially (vanishing gradients), making it nearly impossible for the network to learn that early inputs in a sequence are relevant to later outputs.

</details>

---

### Level 2 — Exam Paragraph (3 minutes)
**Prompt:** Explain sequential processing as *both* an advantage and a disadvantage of RNNs.

> 🧠 中文思路：优点→自然捕捉顺序 | 缺点→不能并行 → 实际影响：长序列训练很慢 → 对比Transformer

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Advantage: naturally captures word order / temporal structure?
- [ ] Disadvantage: cannot parallelise — each step depends on previous hidden state?
- [ ] Mentioned the practical consequence: slow training on long sequences?
- [ ] Contrast with Transformer if possible (processed in parallel)?

</details>

<details>
<summary>📖 Reference Answer</summary>

**Advantage:** Sequential processing naturally captures the temporal order of the data. Because the RNN processes each element one after another, updating its hidden state at each step, it implicitly encodes the ordering information. This is appropriate for sequential data like text or time series, where the meaning depends on the order of elements — "dog bites man" is different from "man bites dog."

**Disadvantage:** Sequential processing means each time step depends on the output of the previous step, so the computations **cannot be parallelised**. For a sequence of length $T$, the RNN must perform $T$ sequential operations. This leads to slow training, especially for long sequences, because modern GPUs are optimised for parallel computation. In contrast, the Transformer architecture processes all positions simultaneously using self-attention, allowing full parallelisation and much faster training on long sequences.

</details>

---

### Level 3 — Analysis (5–7 minutes)
**Prompt:** Compare RNNs and Transformers. In what scenario would you still choose an RNN over a Transformer in 2024?

> 🧠 中文思路：Transformer强在并行+远程依赖 → RNN什么时候还有用？→ 资源有限的设备、流式数据、短序列小数据

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Identified Transformer's strengths: parallelism, long-range dependencies?
- [ ] Identified RNN's niche: low-resource environments, streaming/online inference, very short sequences?
- [ ] Mentioned compute cost: Transformer is O(n²) in sequence length due to attention?
- [ ] Was specific — did NOT just say "RNN is older and worse in all ways"?

</details>

<details>
<summary>📖 Reference Answer</summary>

**Transformers excel** in most sequence modelling tasks because: (1) self-attention creates direct connections between any two positions, solving the long-range dependency problem; (2) all positions are processed in parallel, enabling much faster training; (3) they have been shown to achieve state-of-the-art results across NLP, vision, and other domains.

**However, RNNs may still be preferred in specific scenarios:**

1. **Resource-constrained environments (edge devices, mobile).** RNNs have a constant memory footprint during inference — they only maintain a fixed-size hidden state. Transformers require memory proportional to sequence length squared ($O(n^2)$) for the attention matrix, which can be prohibitive for long sequences on devices with limited memory.

2. **Streaming / online inference.** RNNs naturally process data one element at a time, making them suitable for real-time streaming applications (e.g., sensor data, live audio). Transformers typically require the full sequence to be available before processing, although recent work on causal/streaming Transformers is closing this gap.

3. **Very short sequences with limited training data.** Transformers have fewer inductive biases than RNNs — they need large datasets to learn sequential patterns from scratch. For small datasets with short sequences, an RNN's built-in sequential bias may lead to better performance with less data.

</details>

---

## B4 — Transformer & Attention

### Level 1 — Core Intuition (30 seconds)
**Prompt:** Explain Query, Key, and Value — one sentence each, using an analogy if possible.

<details>
<summary>📖 Reference Answer</summary>

- **Query:** What the current position is "looking for" — like a search query you type into a search engine.
- **Key:** What each position "advertises" about itself — like the title or label on a document that the search engine matches against.
- **Value:** The actual content at each position — once the search finds relevant documents (by matching Query to Key), the Value is the information that gets retrieved and combined.

</details>

---

### Level 2 — Exam Paragraph (3 minutes)
**Prompt:** Why does a Transformer need positional encoding? What happens if you remove it?

> 🧠 中文思路：attention是排列不变的（不管顺序）→ 所以需要位置编码 → 否则"狗咬人"="人咬狗" → 怎么加的？

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Explained that attention is permutation-invariant (doesn't care about order)?
- [ ] Explained positional encoding injects order information?
- [ ] Described what happens without it: "dog bites man" = "man bites dog"?
- [ ] Mentioned that encoding is *added* to the embedding, not concatenated?

</details>

<details>
<summary>📖 Reference Answer</summary>

The self-attention mechanism computes attention weights based on the content of each position (via Q, K, V), but it has **no inherent notion of order** — it treats the input as a set, not a sequence. The attention score between two tokens depends only on their content, not on their positions. This means that without positional encoding, the sentences "dog bites man" and "man bites dog" would produce identical representations, because the same set of tokens would generate the same attention weights.

Positional encoding solves this by **adding** a unique signal to each position's embedding vector before it enters the Transformer. These signals use sinusoidal functions of different frequencies (or learned vectors), giving each position a distinct "fingerprint" that the model can use to reason about order and relative distance. The encoding is added element-wise to the token embedding, not concatenated.

Without positional encoding, the Transformer would be unable to distinguish between different orderings of the same tokens, making it useless for any task where word order matters.

</details>

---

### Level 3 — Analysis (5–7 minutes)
**Prompt:** What is the architectural difference between a Transformer encoder and decoder? Why does the decoder need masked self-attention?

> 🧠 中文思路：encoder双向注意力 → decoder有遮蔽+交叉注意力 → 为什么遮蔽？训练时防止看到未来答案

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Encoder: bidirectional attention, sees the full input?
- [ ] Decoder: has two attention blocks — masked self-attention + cross-attention to encoder output?
- [ ] Masked self-attention: prevents each position attending to future positions?
- [ ] Explained *why* masking is needed: during training, future tokens would "leak" the answer?
- [ ] Mentioned BERT (encoder-only) and GPT (decoder-only) as examples?

</details>

<details>
<summary>📖 Reference Answer</summary>

**Encoder:** Uses standard (bidirectional) self-attention — each position can attend to all other positions in the input, including those that come after it. This gives the encoder full context of the input sequence. BERT is an example of an encoder-only model.

**Decoder:** Has two attention modules per layer:
1. **Masked self-attention** — the decoder attends to its own previously generated outputs, but with a mask that prevents each position from attending to future positions.
2. **Cross-attention** — the decoder attends to the encoder's output, allowing it to incorporate information from the input sequence.

**Why masking is necessary:** During training, the decoder receives the entire target sequence at once (for efficiency — this is called "teacher forcing"). Without masking, position $t$ could directly see the token at position $t+1$, which is the very token it is supposed to predict. This would be information leakage — the model would simply copy the next token instead of learning to predict it. The mask ensures that predictions for position $t$ can only depend on known outputs at positions before $t$, preserving the autoregressive property: each token is predicted based only on the preceding tokens.

GPT is an example of a decoder-only model that uses masked self-attention throughout.

</details>

---

## B5 — Vision Transformer (ViT)

### Level 1 — Core Intuition (30 seconds)
**Prompt:** Why does ViT split images into patches instead of processing individual pixels?

<details>
<summary>📖 Reference Answer</summary>

Self-attention has $O(n^2)$ complexity where $n$ is the sequence length. A 224×224 image has 50,176 pixels — computing attention between all pairs would be computationally infeasible. Splitting into 16×16 patches reduces the sequence to 196 tokens, making attention tractable while still capturing meaningful spatial information within each patch.

</details>

---

### Level 2 — Exam Paragraph (3 minutes)
**Prompt:** Describe the full ViT pipeline: how does a 224×224 image become a class prediction? Include the role of the [CLS] token.

> 🧠 中文思路：6步pipeline → 切patch→投影→加CLS→加位置编码→Transformer编码→CLS输出分类

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Split image into patches (e.g., 16×16 → 196 patches)?
- [ ] Linear projection of each patch to an embedding vector?
- [ ] Prepend [CLS] token (→ 197 tokens)?
- [ ] Add positional embeddings?
- [ ] Pass through Transformer encoder?
- [ ] [CLS] output → MLP head → class prediction?
- [ ] Mentioned that [CLS] aggregates information from all patches via attention?

</details>

<details>
<summary>📖 Reference Answer</summary>

1. **Patch extraction:** The 224×224×3 image is split into non-overlapping patches of size 16×16, producing $\frac{224}{16} \times \frac{224}{16} = 196$ patches.
2. **Linear projection:** Each 16×16×3 patch is flattened into a vector of length 768 and linearly projected into an embedding of dimension $D$ (e.g., 768). This creates 196 patch embedding vectors.
3. **Prepend [CLS] token:** An extra learnable embedding (the [CLS] token) is prepended to the sequence, making it 197 tokens. This token serves as a global summary of the image.
4. **Add positional embeddings:** Learnable positional embeddings are added element-wise to all 197 tokens to encode spatial position information.
5. **Transformer encoder:** The 197 tokens are processed through multiple Transformer encoder layers (self-attention + feed-forward). Through attention, the [CLS] token attends to all patches and aggregates information from the entire image.
6. **Classification head:** The output of the [CLS] token is passed through an MLP head (linear layers) to produce the final class prediction.

The [CLS] token acts as an efficient aggregation mechanism — rather than pooling over all 196 patch outputs, the model learns to summarise the entire image into a single token during training.

</details>

---

### Level 3 — Analysis (5–7 minutes)
**Prompt:** Compare ViT and CNN for image classification. When would you prefer each? Discuss the role of inductive bias and dataset size.

> 🧠 中文思路：CNN有归纳偏置（局部性+平移不变性）→ ViT没有 → 小数据CNN好 → 大数据ViT好 → 原因是什么

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] CNN has strong inductive bias: locality + translation invariance?
- [ ] ViT has weak inductive bias: no built-in spatial assumptions?
- [ ] Small dataset → CNN better (inductive bias compensates for limited data)?
- [ ] Large dataset → ViT better (more flexible, fewer assumptions)?
- [ ] ViT is typically pre-trained on large data then fine-tuned?
- [ ] ViT sees global context from layer 1 (full attention), CNN only in deep layers?

</details>

<details>
<summary>📖 Reference Answer</summary>

**CNNs** have strong inductive biases built into their architecture: **locality** (each neuron only connects to a local region) and **translation equivariance** (the same filter is shared across all positions). These biases encode prior knowledge about images — that nearby pixels are related and that patterns can appear anywhere. This makes CNNs data-efficient; they perform well even with relatively small datasets because the architecture itself encodes useful assumptions.

**ViTs** have much weaker inductive biases. Self-attention operates globally from the first layer — there is no built-in notion of locality or spatial hierarchy. This gives ViTs more flexibility but also means they need more data to learn spatial patterns that CNNs get "for free" from their architecture.

**When to prefer each:**
- **Small to medium datasets:** Prefer CNN. The strong inductive biases compensate for limited data, leading to better performance without extensive pre-training.
- **Large datasets or with pre-training:** Prefer ViT. When trained on massive datasets (e.g., ImageNet-21K or JFT-300M), ViTs can outperform CNNs because they are not constrained by the assumptions of locality — they can discover patterns that CNNs' architecture would not capture. In practice, ViTs are typically pre-trained on very large data and then fine-tuned on the target task.

</details>

---

## B6 — Activation Functions (2025 Q3)

### Level 1 — Core Intuition (30 seconds)
**Prompt:** What is the dying ReLU problem? One sentence.

<details>
<summary>📖 Reference Answer</summary>

When a neuron's input is consistently negative, ReLU outputs 0 with a gradient of 0, so the neuron's weights never get updated and it permanently stops contributing to the network — it "dies."

</details>

---

### Level 2 — Exam Paragraph (3 minutes)
**Prompt:** A manufacturing quality system needs to detect multiple anomaly types simultaneously in a single image. Which output activation function should be used — sigmoid or softmax? Explain why.

> 🧠 中文思路：判断多标签问题 → sigmoid（独立概率）→ softmax不行（概率和为1互相压制）

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Identified this as a multi-label problem (multiple anomalies can co-exist)?
- [ ] Chose sigmoid as the correct activation?
- [ ] Explained why softmax is wrong: forces outputs to sum to 1, so detecting one anomaly reduces the probability of another?
- [ ] Explained why sigmoid works: each output is independent, between 0 and 1?

</details>

<details>
<summary>📖 Reference Answer</summary>

**Sigmoid** should be used. Since a single image can contain multiple anomaly types simultaneously, this is a **multi-label classification problem**. Each anomaly type must be predicted independently.

Sigmoid outputs a probability between 0 and 1 for each output node **independently**. Multiple outputs can be high at the same time — for example, the model can simultaneously predict "scratch: 0.95" and "dent: 0.87" for the same product image.

**Softmax would not work** because it creates a probability distribution that sums to 1 across all output nodes. This means increasing the probability of one anomaly type would automatically decrease the probabilities of others. If a product has both a scratch and a dent, softmax would suppress one prediction to boost the other, making it impossible to correctly detect both anomalies. Softmax is designed for mutually exclusive classes, but anomaly types are not mutually exclusive.

</details>

---

### Level 3 — Analysis (5–7 minutes)
**Prompt:** Compare ReLU, LeakyReLU, and sigmoid as hidden layer activations. When would you use each, and what are the risks?

> 🧠 中文思路：三个激活函数各写一段 → ReLU默认好但有死亡问题 → Leaky修复 → Sigmoid只适合门控/输出层

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] ReLU: fast, simple, avoids vanishing gradients (gradient=1 for positive inputs)?
- [ ] ReLU risk: dying neurons (gradient=0 for negative inputs, permanently dead)?
- [ ] LeakyReLU: small slope for negatives prevents dying neurons?
- [ ] Sigmoid: outputs in (0,1), useful for gating/probabilities, but causes vanishing gradients (max derivative=0.25)?
- [ ] Did NOT recommend sigmoid for hidden layers in deep networks?

</details>

<details>
<summary>📖 Reference Answer</summary>

**ReLU** ($f(x) = \max(0, x)$): The default choice for hidden layers. Its gradient is 1 for positive inputs, which avoids the vanishing gradient problem and allows deep networks to train effectively. It is computationally efficient (simple thresholding). **Risk:** The dying ReLU problem — neurons that receive consistently negative inputs output 0 with gradient 0, so they stop learning permanently.

**LeakyReLU** ($f(x) = x$ if $x > 0$, $\alpha x$ if $x \leq 0$): Addresses the dying ReLU problem by allowing a small, non-zero gradient ($\alpha$, typically 0.01) for negative inputs. This ensures that neurons can always receive gradient signal and potentially recover. **Use when:** You suspect dying neurons are an issue (e.g., observing many dead neurons during training). **Risk:** The small negative slope introduces a minor additional hyperparameter, and in practice the improvement over ReLU is not always significant.

**Sigmoid** ($f(x) = 1/(1+e^{-x})$): Outputs values between 0 and 1, which is useful for gating mechanisms (e.g., inside LSTM cells) and for output layers in binary/multi-label classification. **Risk:** Not suitable for hidden layers in deep networks because its maximum gradient is only 0.25, causing severe vanishing gradients when stacking many layers. Also, its outputs are not zero-centred, which can slow down training.

</details>

---

## B7 — Batch Normalisation (Practice Q5)

### Level 1 — Core Intuition (30 seconds)
**Prompt:** What does batch normalisation do to the activations? One sentence.

<details>
<summary>📖 Reference Answer</summary>

Batch normalisation normalises the activations within each mini-batch to have zero mean and unit variance, then applies learned scale and shift parameters to allow the network to undo the normalisation if needed.

</details>

---

### Level 2 — Exam Paragraph (3 minutes)
**Prompt:** Explain two distinct effects of batch normalisation on model training. For each, describe the mechanism.

> 🧠 中文思路：两个不同的效果 → 加速训练（梯度健康→可用大学习率）→ 正则化（batch统计引入噪声）

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Named two distinct effects from: speeds training / reduces vanishing gradients / regularisation effect / reduces init sensitivity?
- [ ] Explained the mechanism behind each effect — not just labelled them?
- [ ] Mentioned that normalisation is per mini-batch (zero mean, unit variance)?
- [ ] Did NOT confuse batch norm with dropout?
- [ ] Mentioned learnable parameters γ and β?

</details>

<details>
<summary>📖 Reference Answer</summary>

**Effect 1: Speeds up training by allowing higher learning rates.** Batch normalisation normalises activations to zero mean and unit variance within each mini-batch, keeping the input distribution to each layer stable. This reduces internal covariate shift — the phenomenon where each layer's input distribution changes as the parameters of previous layers are updated. With stable input distributions, gradients remain well-scaled (not too large, not too small), so higher learning rates can be used without causing instability. This leads to faster convergence.

**Effect 2: Provides implicit regularisation.** Because the normalisation statistics (mean and variance) are computed per mini-batch rather than over the entire dataset, each sample's normalised value depends on the other samples in the same mini-batch. This introduces stochastic noise into the activations — each time a sample appears in a different mini-batch, its normalised value is slightly different. This noise is similar in effect to dropout and helps prevent overfitting, acting as a form of regularisation without requiring an explicit regularisation term.

</details>

---

### Level 3 — Analysis (5–7 minutes)
**Prompt:** Your colleague says "Batch norm replaces dropout — we don't need both." Evaluate this claim.

> 🧠 中文思路：部分对但不完全对 → BN的正则化效果比dropout弱 → BN主要是训练稳定 → 实际上很多模型两个都用

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Acknowledged batch norm does have a regularising effect (mini-batch noise)?
- [ ] Explained this effect is typically weaker than dropout?
- [ ] Noted that batch norm's primary purpose is training stability, not regularisation?
- [ ] Identified scenarios where both are useful (large models, limited data)?
- [ ] Mentioned that in practice, many architectures do use both?

</details>

<details>
<summary>📖 Reference Answer</summary>

This claim is **partially true but oversimplified**.

Batch normalisation does have a regularising effect due to the noise introduced by computing statistics over mini-batches. However, this regularisation effect is typically **weaker and less controllable** than dropout. The primary purpose of batch normalisation is to stabilise training and enable higher learning rates — regularisation is a secondary benefit.

Dropout provides **explicit, tunable regularisation** by randomly deactivating neurons with a configurable probability. This allows practitioners to directly control the strength of regularisation based on the degree of overfitting observed.

In practice, many successful architectures use both batch normalisation and dropout — batch norm for training stability and dropout for additional regularisation. Whether dropout is needed alongside batch norm depends on the specific problem: for large models trained on small datasets, the additional regularisation from dropout can be critical; for smaller models on large datasets, batch norm's implicit regularisation alone may be sufficient.

Therefore, the decision should be based on empirical observation: if the model overfits even with batch normalisation, adding dropout is a valid and common approach.

</details>

---

## E1 — Evaluation Metrics

### Level 1 — Core Intuition (30 seconds)
**Prompt:** What does recall measure, in plain English? (No formula — just what it means.)

<details>
<summary>📖 Reference Answer</summary>

Recall measures how good the model is at *finding* all the positive cases — of all the instances that are truly positive, what proportion did the model correctly identify? A recall of 80% means the model found 80% of the real positives and missed the other 20%.

</details>

---

### Level 2 — Exam Paragraph (3 minutes)
**Prompt:** A fraud detection model has 99% accuracy but only 10% recall. Is this a good model? Explain your reasoning.

> 🧠 中文思路：类别不平衡 → 99%准确率没用（全预测阴性就有99%）→ recall才是关键（漏了90%的欺诈）

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Identified class imbalance as the reason accuracy is misleading?
- [ ] Explained what 10% recall means: the model misses 90% of actual fraud cases?
- [ ] Stated clearly: this model is NOT good for fraud detection?
- [ ] Mentioned that the cost of false negatives (missed fraud) is very high in this domain?
- [ ] Suggested a better metric (recall, F1, AUC-ROC, precision-recall curve)?

</details>

<details>
<summary>📖 Reference Answer</summary>

**No, this is not a good model** for fraud detection, despite the impressive-sounding 99% accuracy.

The high accuracy is **misleading due to class imbalance**. In fraud detection, the vast majority of transactions are legitimate — if only 1% of transactions are fraudulent, a model that predicts every single transaction as "legitimate" would achieve 99% accuracy without detecting any fraud at all. The 99% accuracy tells us almost nothing about the model's ability to detect fraud.

The **recall of only 10%** is the critical failure. This means the model only detects 10% of actual fraudulent transactions — it **misses 90% of all fraud**. In a fraud detection system, false negatives (missed fraud) can result in significant financial losses for the bank and its customers. A model that misses 9 out of 10 fraudulent transactions is essentially useless for its intended purpose.

For this application, recall should be the primary metric — the model needs to catch as many fraudulent transactions as possible. F1 score or the area under the precision-recall curve (PR-AUC) would be more appropriate evaluation metrics than accuracy for this imbalanced problem.

</details>

---

### Level 3 — Analysis (5–7 minutes)
**Prompt:** You are building a cancer screening model. The dataset has 95% negative cases and 5% positive cases. Design an evaluation strategy. Which metrics do you prioritise and why?

> 🧠 中文思路：类别不平衡 → 准确率没用 → recall最重要（漏诊比误诊更危险）→ 用PR-AUC不用ROC → 设低阈值

<details>
<summary>✅ Self-check (open AFTER writing)</summary>

- [ ] Identified the class imbalance problem explicitly?
- [ ] Argued for recall/sensitivity as the primary metric (missing a cancer is worse than a false alarm)?
- [ ] Mentioned precision-recall tradeoff?
- [ ] Considered using AUC-ROC or PR-AUC for threshold-independent evaluation?
- [ ] Did NOT rely on accuracy as the main metric?
- [ ] Discussed the human cost of each error type (false positive vs. false negative)?

</details>

<details>
<summary>📖 Reference Answer</summary>

**The class imbalance problem:** With 95% negative and 5% positive cases, a naive model predicting "negative" for everything achieves 95% accuracy. Accuracy is therefore not a useful metric for this problem.

**Primary metric: Recall (sensitivity).** In cancer screening, a false negative means a patient with cancer is told they are healthy — they would not receive treatment, potentially leading to disease progression or death. This is the most dangerous error. We must prioritise **high recall** to ensure that as few cancer cases as possible are missed. A target recall of ≥ 95% is typical for screening applications.

**Secondary metric: Precision.** A false positive means a healthy patient is told they might have cancer, leading to unnecessary anxiety, follow-up tests (biopsies, imaging), and medical costs. While less dangerous than a false negative, a very high false positive rate (very low precision) undermines trust in the screening system and wastes medical resources. We should monitor precision to ensure it stays at an acceptable level.

**Threshold-independent metrics:** Since precision and recall depend on the classification threshold, we should also evaluate using threshold-independent metrics:
- **PR-AUC (Precision-Recall Area Under Curve):** More informative than ROC-AUC for imbalanced datasets, as it focuses on the positive class.
- **AUC-ROC:** Useful for overall model comparison, but can give an overly optimistic picture when the dataset is heavily imbalanced.

**Practical approach:** Set the classification threshold low enough to achieve the target recall, then report the corresponding precision. Use the F1 score (or Fβ with β > 1 to weight recall more heavily) as a single summary metric for model comparison.

</details>
