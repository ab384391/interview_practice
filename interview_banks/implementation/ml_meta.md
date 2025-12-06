# ML Coding Interview Question Bank for Meta & OpenAI

**200 Implementation-Style Questions** | Compiled November 2025

---

## Overview

This comprehensive question bank contains 200 carefully curated ML coding interview questions in the style asked at **Meta** and **OpenAI**. These companies are known for asking candidates to implement algorithms, neural network components, and ML systems from scratch within 45-60 minutes.

### Key Statistics
| Metric | Count |
|--------|-------|
| Total Questions | 200 |
| Critical Importance | 15 |
| High Importance | 66 |
| Medium Importance | 103 |
| Low Importance | 16 |

### Distribution by Difficulty
- **Easy**: 49 questions (24.5%)
- **Medium**: 88 questions (44%)
- **Hard**: 63 questions (31.5%)

### Distribution by Company Focus
- **Both Companies**: 140 questions (70%)
- **OpenAI-Specific**: 44 questions (22%)
- **Meta-Specific**: 16 questions (8%)

---

## Category 1: Neural Network Fundamentals (25 Questions)

### Critical Priority
1. **Implement backpropagation for a simple 2-layer neural network** [Both, Hard]
2. **Implement a Transformer block from scratch (Multi-Head Attention + FFN)** [OpenAI, Hard]
3. **Implement self-attention mechanism from scratch** [OpenAI, Hard]
4. **Implement a 2D convolutional layer from scratch** [Meta, Hard]

### High Priority
5. Implement scaled dot-product attention [OpenAI, Medium]
6. Implement multi-head attention layer [OpenAI, Hard]
7. Implement a basic RNN cell from scratch [Both, Medium]
8. Implement LSTM cell with forget, input, and output gates [Both, Hard]
9. Implement a 2D convolutional filter/kernel operation [Meta, Medium]
10. Implement batch normalization forward and backward pass [Both, Hard]
11. Implement layer normalization [OpenAI, Medium]
12. Implement softmax function with numerical stability [Both, Medium]
13. Implement cross-entropy loss function [Both, Medium]
14. Implement forward pass of a fully connected layer [Both, Easy]
15. Implement backward pass (gradient computation) for fully connected layer [Both, Medium]
16. Implement embedding layer with lookup table [Both, Easy]

### Medium Priority
17. Implement positional encoding for transformers [OpenAI, Medium]
18. Implement GRU cell from scratch [Both, Hard]
19. Implement max pooling and average pooling layers [Both, Easy]
20. Implement dropout with training and inference modes [Both, Easy]
21. Implement binary cross-entropy loss [Both, Easy]
22. Implement ReLU, Leaky ReLU, and GELU activation functions [Both, Easy]
23. Implement sigmoid and tanh activation functions with gradients [Both, Easy]
24. Implement weight initialization (Xavier, He) [Both, Easy]
25. Implement depthwise separable convolution [Meta, Hard]

---

## Category 2: ML Algorithms from Scratch (18 Questions)

### Critical Priority
26. **Implement K-Means clustering algorithm from scratch** [Both, Medium]
27. **Implement logistic regression with gradient descent** [Both, Medium]

### High Priority
28. Implement K-Nearest Neighbors (KNN) classifier [Both, Medium]
29. Implement linear regression with closed-form solution [Both, Easy]
30. Implement linear regression with gradient descent [Both, Medium]
31. Implement decision tree (ID3/CART) from scratch [Both, Hard]
32. Implement Principal Component Analysis (PCA) from scratch [Both, Medium]

### Medium Priority
33. Implement Naive Bayes classifier [Both, Medium]
34. Implement Support Vector Machine (SVM) with hinge loss [Both, Hard]
35. Implement Singular Value Decomposition (SVD) [Both, Hard]
36. Implement Random Forest ensemble method [Both, Hard]
37. Implement Gradient Boosting algorithm [Both, Hard]
38. Implement Gaussian Mixture Model with EM algorithm [Both, Hard]
39. Implement SMOTE for class imbalance [Both, Medium]
40. Implement feature importance using permutation [Both, Medium]

### Lower Priority
41. Implement AdaBoost from scratch [Both, Hard]
42. Implement DBSCAN clustering algorithm [Both, Medium]
43. Implement hierarchical clustering (agglomerative) [Both, Medium]

---

## Category 3: Optimization & Gradient Descent (14 Questions)

### Critical Priority
44. **Implement SGD (Stochastic Gradient Descent) optimizer** [Both, Medium]

### High Priority
45. Implement SGD with momentum [Both, Medium]
46. Implement Adam optimizer from scratch [Both, Medium]
47. Implement L1 (Lasso) regularization [Both, Easy]
48. Implement L2 (Ridge) regularization [Both, Easy]

### Medium Priority
49. Implement RMSprop optimizer [Both, Medium]
50. Implement Elastic Net regularization [Both, Easy]
51. Implement learning rate scheduler (step, exponential, cosine) [Both, Easy]
52. Implement gradient clipping by value and by norm [Both, Easy]
53. Implement weight decay (L2 regularization in optimizer) [Both, Easy]
54. Implement warmup scheduler for learning rate [Both, Easy]
55. Implement early stopping with patience [Both, Easy]

### Lower Priority
56. Implement Adagrad optimizer [Both, Medium]
57. Implement Nesterov momentum [Both, Medium]

---

## Category 4: Generative Models (8 Questions)

### Critical Priority
58. **Implement Variational Autoencoder (VAE) with reparameterization trick** [OpenAI, Hard]

### High Priority
59. Implement basic autoencoder architecture [Both, Medium]
60. Implement GAN discriminator and generator networks [Both, Hard]
61. Implement GAN training loop with alternating optimization [Both, Hard]
62. Implement KL divergence loss for VAE [OpenAI, Medium]

### Medium Priority
63. Implement reconstruction loss (MSE and BCE) [Both, Easy]
64. Implement ELBO (Evidence Lower Bound) objective [OpenAI, Medium]

### Lower Priority
65. Implement conditional GAN (cGAN) architecture [Both, Hard]

---

## Category 5: NLP & Text Processing (16 Questions)

### Critical Priority
66. **Implement Byte Pair Encoding (BPE) tokenizer** [OpenAI, Hard]

### High Priority
67. Implement Word2Vec (Skip-gram) from scratch [Both, Hard]
68. Implement beam search decoding algorithm [OpenAI, Hard]
69. Implement top-k and nucleus (top-p) sampling [OpenAI, Medium]
70. Implement causal (autoregressive) attention masking [OpenAI, Medium]
71. Implement attention mask for encoder-decoder models [OpenAI, Medium]
72. Implement nucleus sampling with temperature [OpenAI, Medium]

### Medium Priority
73. Implement Word2Vec (CBOW) from scratch [Both, Hard]
74. Implement greedy decoding for sequence generation [OpenAI, Medium]
75. Implement TF-IDF vectorization from scratch [Both, Medium]
76. Implement n-gram language model [Both, Medium]
77. Implement text tokenizer with special tokens handling [OpenAI, Medium]
78. Implement padding mask for variable-length sequences [Both, Easy]
79. Implement language model scoring function [OpenAI, Medium]
80. Implement sentence embedding aggregation methods [Both, Easy]

### Lower Priority
81. Implement bag-of-words representation [Both, Easy]

---

## Category 6: Metrics & Evaluation (15 Questions)

### High Priority
82. Implement precision, recall, and F1-score calculations [Both, Easy]
83. Implement ROC curve and AUC calculation [Both, Medium]
84. Implement perplexity metric for language models [OpenAI, Medium]
85. Implement k-fold cross-validation from scratch [Both, Medium]

### Medium Priority
86. Implement Precision-Recall curve [Both, Medium]
87. Implement confusion matrix computation [Both, Easy]
88. Implement mean squared error (MSE) and RMSE [Both, Easy]
89. Implement R-squared (coefficient of determination) [Both, Easy]
90. Implement log loss (binary and multi-class) [Both, Easy]
91. Implement BLEU score for text generation [OpenAI, Medium]
92. Implement IoU (Intersection over Union) for object detection [Meta, Easy]
93. Implement mean average precision (mAP) [Both, Medium]
94. Implement NDCG (Normalized Discounted Cumulative Gain) [Both, Medium]
95. Implement MRR (Mean Reciprocal Rank) [Both, Easy]

### Lower Priority
96. Implement mean absolute error (MAE) [Both, Easy]

---

## Category 7: Distance & Similarity (6 Questions)

### High Priority
97. Implement cosine similarity and cosine distance [Both, Easy]
98. Implement Euclidean distance [Both, Easy]

### Medium Priority
99. Implement Manhattan (L1) distance [Both, Easy]
100. Implement Jaccard similarity [Both, Easy]
101. Implement dot product similarity [Both, Easy]

### Lower Priority
102. Implement Minkowski distance (generalized) [Both, Easy]

---

## Category 8: Data Structures for ML Systems (13 Questions)

### Critical Priority
103. **Implement LRU Cache** [OpenAI, Medium]
104. **Implement time-based key-value store** [OpenAI, Hard]

### High Priority
105. Implement versioned data store [OpenAI, Hard]
106. Implement resumable iterator with state serialization [OpenAI, Hard]
107. Implement in-memory database with basic SQL operations [OpenAI, Hard]
108. Implement key-value store with serialize/deserialize [OpenAI, Medium]

### Medium Priority
109. Implement priority queue / heap [Both, Medium]
110. Implement trie for autocomplete/prefix search [Both, Medium]
111. Implement hash map from scratch [Both, Medium]
112. Implement min-heap for k-nearest neighbors [Both, Medium]
113. Implement circular buffer for streaming data [Both, Medium]

### Lower Priority
114. Implement bloom filter for membership testing [Both, Medium]
115. Implement skip list for efficient search [Both, Hard]

---

## Category 9: Graph Algorithms (8 Questions)

### High Priority
116. Implement BFS (Breadth-First Search) [Both, Medium]
117. Implement DFS (Depth-First Search) [Both, Medium]
118. Implement graph for social network friend recommendations [Meta, Medium]

### Medium Priority
119. Implement topological sort for DAG [Both, Medium]
120. Implement Dijkstra's shortest path algorithm [Both, Medium]
121. Implement Union-Find (Disjoint Set Union) [Both, Medium]
122. Implement connected components detection [Meta, Medium]
123. Implement cycle detection in directed graph [Both, Medium]

---

## Category 10: Linear Algebra (8 Questions)

### High Priority
124. Implement matrix multiplication from scratch [Both, Medium]
125. Implement dot product of two vectors [Both, Easy]

### Medium Priority
126. Implement matrix transpose [Both, Easy]
127. Implement matrix inversion [Both, Hard]
128. Implement outer product of two vectors [Both, Easy]
129. Implement sparse matrix operations [Both, Medium]
130. Implement batch matrix multiplication (einsum) [Both, Medium]

### Lower Priority
131. Implement eigenvalue decomposition [Both, Hard]

---

## Category 11: Algorithmic Problems (20 Questions)

### High Priority
132. K closest points to origin (for recommendation context) [Meta, Medium]
133. Merge K sorted lists (feature aggregation) [Meta, Hard]
134. Sliding window maximum (engagement metrics) [Meta, Hard]
135. Design and implement a spreadsheet with formula dependencies [OpenAI, Hard]
136. Implement multithreaded web crawler [OpenAI, Hard]
137. Binary search and its variants [Both, Medium]
138. Two sum / three sum problems [Both, Easy]
139. Design data structure with O(1) insert/delete/getRandom and O(log n) getMedian [OpenAI, Hard]

### Medium Priority
140. Longest substring without repeating characters [Both, Medium]
141. Implement Unix CD command with symbolic link resolution [OpenAI, Medium]
142. Meeting rooms scheduling problem [Both, Medium]
143. Find largest values in variable k×k submatrices [OpenAI, Hard]
144. Implement tree traversals (inorder, preorder, postorder) [Both, Easy]
145. Dynamic programming: longest common subsequence [Both, Medium]
146. Dynamic programming: edit distance [Both, Medium]
147. Implement parallel prefix sum (for attention) [OpenAI, Medium]
148. Implement efficient batched operations for matrix multiplication [Both, Medium]
149. Design and implement a rate limiter [Both, Medium]
150. Implement quickselect for finding kth smallest element [Both, Medium]
151. Implement efficient string matching (KMP/Rabin-Karp) [Both, Hard]

---

## Category 12: System Design - ML Focused (17 Questions)

### Critical Priority
152. **Design a recommendation system (collaborative/content-based)** [Meta, Hard]
153. **Design news feed ranking system** [Meta, Hard]
154. **Design LLM-powered enterprise search system** [OpenAI, Hard]
155. **Design ChatGPT / conversational AI system** [OpenAI, Hard]

### High Priority
156. Design ad targeting/ranking system [Meta, Hard]
157. Design People You May Know feature [Meta, Hard]
158. Design GPU credit scheduling system [OpenAI, Hard]
159. Design real-time model A/B testing system [Both, Hard]
160. Design fraud detection ML pipeline [Both, Hard]
161. Design content moderation system [Meta, Hard]
162. Design model serving infrastructure with low latency [Both, Hard]
163. Design real-time LLM inference system [OpenAI, Hard]
164. Design embedding-based search/retrieval system [Both, Hard]

### Medium Priority
165. Design type-ahead search with ML ranking [Meta, Hard]
166. Design ML feature store [Both, Hard]
167. Design distributed training system [OpenAI, Hard]
168. Design model versioning and registry system [Both, Hard]

---

## Category 13: Probability & Statistics (10 Questions)

### High Priority
169. Compute KL divergence given probability distributions [OpenAI, Medium]
170. Calculate probability using Bayes' theorem [Both, Medium]

### Medium Priority
171. Implement Markov chain simulation [OpenAI, Medium]
172. Implement Monte Carlo sampling [Both, Medium]
173. Implement reservoir sampling [Both, Medium]
174. Implement weighted random sampling [Both, Medium]
175. Calculate expected value and variance [Both, Easy]
176. Implement importance sampling [Both, Hard]

### Lower Priority
177. Implement bootstrap sampling [Both, Medium]
178. Implement Gibbs sampling [Both, Hard]

---

## Category 14: Feature Engineering (8 Questions)

### Medium Priority
179. Implement one-hot encoding [Both, Easy]
180. Implement min-max normalization [Both, Easy]
181. Implement z-score standardization [Both, Easy]
182. Implement missing value imputation strategies [Both, Easy]
183. Implement feature hashing [Both, Medium]
184. Implement target encoding for categorical features [Both, Medium]
185. Implement data augmentation for images [Meta, Medium]

### Lower Priority
186. Implement label encoding [Both, Easy]

---

## Category 15: Advanced Deep Learning (14 Questions)

### High Priority
187. Implement LoRA (Low-Rank Adaptation) for fine-tuning [OpenAI, Hard]

### Medium Priority
188. Implement temperature scaling for model calibration [OpenAI, Easy]
189. Implement label smoothing regularization [Both, Easy]
190. Implement knowledge distillation loss [Both, Medium]
191. Implement contrastive loss (triplet loss, InfoNCE) [Both, Medium]
192. Implement focal loss for imbalanced classification [Both, Medium]
193. Implement residual connections (skip connections) [Both, Easy]
194. Implement attention pooling [Both, Medium]
195. Implement rotary positional embeddings (RoPE) [OpenAI, Hard]
196. Implement flash attention concepts [OpenAI, Hard]
197. Implement gradient checkpointing for memory efficiency [OpenAI, Hard]
198. Implement mixed precision training logic [Both, Hard]
199. Implement model quantization (int8) [Both, Hard]

### Lower Priority
200. Implement mixup data augmentation [Both, Medium]

---

## Preparation Strategy

### For OpenAI Interviews
1. **Focus Areas**: Transformer architecture, attention mechanisms, LLM components, NLP algorithms
2. **Must-Know**: LRU Cache, time-based data stores, BPE tokenizer, beam search, VAE
3. **System Design**: LLM-powered search, ChatGPT architecture, GPU scheduling
4. **Code Quality**: Production-ready, maintainable, handles edge cases

### For Meta Interviews
1. **Focus Areas**: Recommendation systems, CNNs, social graph algorithms, ranking systems
2. **Must-Know**: K-means, 2D convolution, collaborative filtering, news feed ranking
3. **System Design**: Recommendation systems, ad targeting, content moderation
4. **Context**: Frame problems in social network/engagement context

### General Tips
- Practice implementing algorithms from scratch using only NumPy (no sklearn/PyTorch)
- Understand both forward and backward passes for neural network components
- Be prepared to discuss time/space complexity
- Write clean, modular code with proper variable names
- Handle edge cases explicitly
- Practice coding under time pressure (35-45 minutes per problem)

---

## Sources

This question bank was compiled from multiple sources including:
- Glassdoor interview reports
- LeetCode discussion forums
- Reddit r/MachineLearning and r/leetcode
- Interview preparation platforms (InterviewQuery, HelloInterview, Exponent)
- Official company interview guides
- Candidate experience reports from 2024-2025

*Last Updated: November 2025*
