import numpy as np

def sigmoid(x):
    """
    Sigmoid activation: 1 / (1 + exp(-x))
    """
    return 1 / (1 + np.exp(-x))

def tanh_activation(x):
    """
    Tanh activation: (exp(x) - exp(-x)) / (exp(x) + exp(-x))
    """
    return np.tanh(x)

def sigmoid_grad(x):
    """
    Gradient of sigmoid: sigmoid(x) * (1 - sigmoid(x))
    """
    s = sigmoid(x)
    return s * (1 - s)

def tanh_grad(x):
    """
    Gradient of tanh: 1 - tanh(x)^2
    """
    t = np.tanh(x)
    return 1 - t**2

"""
NOTES:
1. Sigmoid:
   - Output range: (0, 1)
   - Used for binary classification output layer.
   - Suffers from vanishing gradient for large |x|.
   
2. Tanh:
   - Output range: (-1, 1)
   - Zero-centered (better than sigmoid for hidden layers).
   - Still suffers from vanishing gradient.
   
3. Gradients:
   - Both have gradients < 1, leading to vanishing gradient in deep networks.
   - This is why ReLU became popular for hidden layers.
   
4. Modern Usage:
   - Sigmoid: Output layer for binary classification.
   - Tanh: Sometimes in RNNs, but LSTM/GRU use gating.
   - Hidden layers: Prefer ReLU/GELU.
"""
