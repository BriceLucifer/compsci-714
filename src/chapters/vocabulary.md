# Professional Vocabulary Quick Reference

---

## Frequently Confused Terms

| Term A | Term B | Key Difference |
|--------|--------|---------------|
| **Parameter** | **Hyperparameter** | Parameters are learned during training (weights, biases). Hyperparameters are set BEFORE training (learning rate, batch size, number of layers). |
| **Overfitting** | **Underfitting** | Overfitting = model too complex (memorises noise). Underfitting = model too simple (can't capture patterns). |
| **Bias (statistical)** | **Bias (in neurons)** | Statistical bias = systematic error from simplifying assumptions. Neuron bias = a constant term added before activation. |
| **Multi-class** | **Multi-label** | Multi-class = exactly ONE class per input (softmax). Multi-label = MULTIPLE classes per input possible (sigmoid). |
| **Validation set** | **Test set** | Validation = used during training to tune hyperparameters. Test = used ONCE at the end to evaluate final performance. |
| **Epoch** | **Batch** | Epoch = one complete pass through ALL training data. Batch = a subset of data processed before one weight update. |
| **Regularisation** | **Normalisation** | Regularisation = technique to prevent overfitting (L1, L2, dropout). Normalisation = scaling data or activations (batch norm, standardisation). |
| **Feature map** | **Filter/Kernel** | Filter = the small weight matrix that slides across input. Feature map = the OUTPUT produced after applying a filter. |
| **Stride** | **Padding** | Stride = how many pixels the filter moves each step. Padding = adding zeros around the input border. |
| **Valid padding** | **Same padding** | Valid = no padding (output shrinks). Same = pad so output spatial dimensions = input. |
| **Encoder** | **Decoder** | Encoder = processes input into representation. Decoder = generates output from representation. |
| **Self-attention** | **Cross-attention** | Self-attention = input attends to itself. Cross-attention = one sequence attends to another (e.g., decoder attends to encoder). |
| **Precision** | **Recall** | Precision = of predicted positives, how many are correct. Recall = of actual positives, how many did we find. |

---

## Key Terms by Topic

### Data Preprocessing
| Term | Chinese | Definition |
|------|---------|-----------|
| Imputation | 填补/插补 | Replacing missing values with estimated values |
| Standardisation | 标准化 | Transform to mean=0, std=1: (x-μ)/σ |
| Normalisation | 归一化 | Scale to range [0,1]: (x-min)/(max-min) |
| One-hot encoding | 独热编码 | Binary vector representation for categories |
| Outlier | 异常值/离群值 | Data point far from the rest of the distribution |
| Feature engineering | 特征工程 | Creating new features from raw data |

### Neural Networks
| Term | Chinese | Definition |
|------|---------|-----------|
| Activation function | 激活函数 | Non-linear function applied after linear transformation |
| Backpropagation | 反向传播 | Algorithm to compute gradients by chain rule |
| Gradient descent | 梯度下降 | Iterative optimisation by following negative gradient |
| Learning rate | 学习率 | Step size for gradient descent updates |
| Loss function | 损失函数 | Measures how wrong the model's predictions are |
| Weight initialisation | 权重初始化 | Setting initial values for model parameters |
| Vanishing gradient | 梯度消失 | Gradients become extremely small in deep networks |
| Exploding gradient | 梯度爆炸 | Gradients become extremely large in deep networks |

### CNN
| Term | Chinese | Definition |
|------|---------|-----------|
| Convolution | 卷积 | Sliding a filter across input to produce feature map |
| Pooling | 池化 | Downsampling feature maps (max or average) |
| Kernel/Filter | 卷积核/滤波器 | Small weight matrix that detects patterns |
| Stride | 步幅 | Number of pixels the filter moves each step |
| Padding | 填充 | Adding zeros around input borders |
| Feature map | 特征图 | Output of applying a filter to input |
| Receptive field | 感受野 | Region of input that affects a particular output neuron |

### Transformer
| Term | Chinese | Definition |
|------|---------|-----------|
| Self-attention | 自注意力 | Each position attends to all other positions in the sequence |
| Multi-head attention | 多头注意力 | Multiple parallel attention functions with different projections |
| Positional encoding | 位置编码 | Signal added to embeddings to encode sequence order |
| Masked attention | 掩码注意力 | Prevents attending to future positions in decoder |
| Query (Q) | 查询 | "What am I looking for?" |
| Key (K) | 键 | "What do I contain?" |
| Value (V) | 值 | "What information do I provide?" |
| [CLS] token | 分类标记 | Special token in ViT that aggregates information for classification |

### Regularisation & Training
| Term | Chinese | Definition |
|------|---------|-----------|
| L1 regularisation (Lasso) | L1正则化 | Adds |weight| penalty → drives some weights to exactly 0 (sparsity) |
| L2 regularisation (Ridge) | L2正则化 | Adds weight² penalty → shrinks all weights toward 0 |
| Dropout | 随机失活 | Randomly deactivates neurons during training to prevent co-adaptation |
| Early stopping | 提前停止 | Stop training when validation loss stops improving |
| Batch normalisation | 批量归一化 | Normalises activations per mini-batch (zero mean, unit variance) |
| Weight decay | 权重衰减 | Equivalent to L2 regularisation in most optimisers |

### Optimisation
| Term | Chinese | Definition |
|------|---------|-----------|
| SGD | 随机梯度下降 | Updates weights using gradient of a random mini-batch |
| Momentum | 动量 | Accumulates past gradients to smooth and accelerate updates |
| Adam | 自适应矩估计 | Adaptive per-parameter learning rate using 1st and 2nd moment estimates |
| Learning rate schedule | 学习率调度 | Changing learning rate during training (e.g., exponential decay) |
| Convergence | 收敛 | When the loss reaches a stable minimum value |
| Gradient clipping | 梯度裁剪 | Caps gradient magnitude to prevent exploding gradients |

### RNN / Sequence Models
| Term | Chinese | Definition |
|------|---------|-----------|
| Hidden state | 隐藏状态 | Internal memory vector passed between time steps in RNN |
| LSTM | 长短时记忆网络 | RNN variant with gates (forget, input, output) to control information flow |
| GRU | 门控循环单元 | Simplified LSTM with 2 gates (reset, update) instead of 3 |
| Forget gate | 遗忘门 | Decides what information to discard from cell state |
| Sequential processing | 顺序处理 | Processing tokens one at a time (advantage: captures order; drawback: can't parallelise) |
| Teacher forcing | 教师强迫 | Using ground truth as decoder input during training instead of previous predictions |

### Evaluation
| Term | Chinese | Definition |
|------|---------|-----------|
| Confusion matrix | 混淆矩阵 | Table showing TP, TN, FP, FN counts |
| True Positive (TP) | 真阳性 | Correctly predicted as positive |
| False Positive (FP) | 假阳性 | Incorrectly predicted as positive (Type I error) |
| False Negative (FN) | 假阴性 | Incorrectly predicted as negative (Type II error) |
| True Negative (TN) | 真阴性 | Correctly predicted as negative |
| Class imbalance | 类别不平衡 | Unequal distribution of classes in dataset |

---

## Commonly Misspelled Words

| Wrong | Correct |
|-------|---------|
| ~~regularization~~ | **regularisation** (NZ/UK spelling used in exam) |
| ~~optimzation~~ | **optimisation** |
| ~~occured~~ | **occurred** |
| ~~seperately~~ | **separately** |
| ~~convultion~~ | **convolution** |
| ~~parallelise~~ | correct as-is (NZ spelling) |
| ~~acheive~~ | **achieve** |
| ~~independant~~ | **independent** |
| ~~artifical~~ | **artificial** |

Note: This is a New Zealand university — British/NZ spelling is expected (regularisation, normalisation, optimisation), not American spelling.

---

## 考试高频搭配（Collocations for Exams）

> 英文不是一个词一个词写的，是一组一组搭配着用的。背搭配比背单词更有效。

### 动词 + 名词 搭配
| 中文 | 正确搭配 | 错误搭配 |
|------|---------|---------|
| 应用正则化 | **apply** regularisation | ~~use regularisation~~ (可以但不够学术) |
| 计算梯度 | **compute** the gradient | ~~calculate the gradient~~ (也对，但 compute 更常用) |
| 训练模型 | **train** the model | ~~learn the model~~ |
| 调整超参数 | **tune** hyperparameters | ~~adjust hyperparameters~~ (也对但 tune 更地道) |
| 提取特征 | **extract** features | ~~get features~~ |
| 缓解过拟合 | **mitigate** overfitting | ~~reduce the overfit~~ |
| 收敛到最优值 | **converge** to the optimum | ~~reach to the optimum~~ |
| 惩罚大权重 | **penalise** large weights | ~~punish big weights~~ |
| 丢弃信息 | **discard** information | ~~throw away the information~~ |
| 执行特征选择 | **perform** feature selection | ~~do feature selection~~ |

### 形容词 + 名词 搭配
| 中文 | 正确搭配 | 不太好的说法 |
|------|---------|-------------|
| 类别不平衡 | **class imbalance** | ~~unbalanced classes~~ |
| 过拟合的模型 | model that **overfits** | ~~overfitted model~~ (也对但动词形式更常用) |
| 自适应学习率 | **adaptive** learning rate | ~~automatic learning rate~~ |
| 稀疏表示 | **sparse** representation | ~~few-value representation~~ |
| 鲁棒的 | **robust** to outliers | ~~strong against outliers~~ |
| 可泛化的 | **generalisable** | ~~can be generalised~~ (形容词更简洁) |

### 常用介词搭配
| 中文 | 正确搭配 | 常见错误 |
|------|---------|---------|
| 在验证集上表现好 | perform well **on** the validation set | ~~in the validation set~~ |
| 对异常值鲁棒 | robust **to** outliers | ~~robust for outliers~~ |
| 收敛到一个值 | converge **to** a value | ~~converge at a value~~ |
| 在...方面优于 | outperform [X] **in** terms of | ~~outperform [X] at~~ |
| 防止过拟合 | prevent **overfitting** (动名词) | ~~prevent to overfit~~ |
| 有助于泛化 | help **with** generalisation | ~~help to generalise~~ (两者都对) |
