# ML Interview Practice - Neural Network Fundamentals

This repository contains complete implementations of **25 Neural Network interview questions** commonly asked at Meta and OpenAI.

## 🎯 Quick Start

### Test an Implementation
```bash
python3 compare.py neuralnetworks_fc_forward_high_easy.py
```

### List All Implementations
```bash
ls neuralnetworks_*.py
```

### Check Progress
```bash
cat questions_status.md
```

## 📁 Project Structure

```
interview_practice/
├── compare.py                          # Test runner script
├── questions_status.md                 # Progress tracker
├── tests/
│   ├── __init__.py
│   └── test_cases.py                   # Test cases for all implementations
├── neuralnetworks_*.py                 # 25 implementation files
└── interview_banks/
    └── implementation/
        └── ml_meta.md                  # Original question bank
```

## ✅ Completed Implementations (25/25)

### Critical Priority / Hard
- ✅ Backpropagation for 2-layer NN
- ✅ Transformer block (Multi-Head Attention + FFN)
- ✅ Self-attention mechanism
- ✅ 2D convolutional layer

### High Priority / Hard
- ✅ Multi-head attention layer
- ✅ LSTM cell with gates
- ✅ Batch normalization (forward + backward)

### High Priority / Medium
- ✅ Scaled dot-product attention
- ✅ Basic RNN cell
- ✅ 2D convolutional filter
- ✅ Layer normalization
- ✅ Softmax with numerical stability
- ✅ Cross-entropy loss
- ✅ FC layer backward pass

### High Priority / Easy
- ✅ FC layer forward pass
- ✅ Embedding layer lookup

### Medium Priority / Hard
- ✅ GRU cell
- ✅ Depthwise separable convolution

### Medium Priority / Medium
- ✅ Positional encoding (sinusoidal)

### Medium Priority / Easy
- ✅ Max/Average pooling
- ✅ Dropout (inverted)
- ✅ Binary cross-entropy
- ✅ ReLU/Leaky ReLU/GELU
- ✅ Sigmoid/Tanh with gradients
- ✅ Xavier/He weight initialization

## 🔧 Features

### Clean Implementations
- **NumPy-only**: No PyTorch/TensorFlow dependencies
- **Production-quality**: Proper error handling and edge cases
- **Well-documented**: Comprehensive docstrings

### Educational Notes
Each implementation includes:
- Mathematical derivations
- Edge case discussions
- Optimization strategies
- Common pitfalls
- Practical considerations

### Automated Testing
- Reference implementations for validation
- Numerical stability checks
- Multiple test cases per function

## 📖 Usage for Interview Prep

### 1. Study Phase
```bash
# Read an implementation
cat neuralnetworks_transformer_block_critical_hard.py
```

### 2. Practice Phase
- Close the reference file
- Implement the function from scratch
- Use the same function signature

### 3. Validation Phase
```bash
# Test your implementation
python3 compare.py your_file.py
```

### 4. Review Phase
- Compare with reference implementation
- Read the NOTES section
- Understand trade-offs

## 🎓 Key Concepts Covered

### Neural Network Basics
- Forward/backward propagation
- Activation functions
- Loss functions
- Weight initialization

### Attention Mechanisms
- Scaled dot-product attention
- Multi-head attention
- Self-attention
- Transformer blocks

### Recurrent Networks
- Vanilla RNN
- LSTM (Long Short-Term Memory)
- GRU (Gated Recurrent Unit)

### Convolutional Networks
- 2D convolution
- Pooling layers
- Depthwise separable convolution

### Normalization & Regularization
- Batch normalization
- Layer normalization
- Dropout

## 📊 Statistics

| Metric | Count |
|--------|-------|
| Total Implementations | 25 |
| Lines of Code | ~2,500 |
| Test Cases | 15+ |
| Documentation Notes | 25 sections |

## 🚀 Next Steps

This completes **Category 1: Neural Network Fundamentals** (25/200 questions).

Remaining categories:
- ML Algorithms from Scratch (18 questions)
- Optimization & Gradient Descent (14 questions)
- Generative Models (8 questions)
- NLP & Text Processing (16 questions)
- And 10 more categories...

## 📝 File Naming Convention

```
neuralnetworks_<problem>_<importance>_<difficulty>.py
```

Examples:
- `neuralnetworks_fc_forward_high_easy.py`
- `neuralnetworks_transformer_block_critical_hard.py`

## 🧪 Testing

All implementations have been tested and verified:
```bash
✅ All 25 implementations pass their test cases
```

## 📚 Resources

- Original question bank: `interview_banks/implementation/ml_meta.md`
- Progress tracker: `questions_status.md`
- Test infrastructure: `compare.py` and `tests/test_cases.py`

---

**Status**: ✅ Neural Network Fundamentals Complete (25/25)
