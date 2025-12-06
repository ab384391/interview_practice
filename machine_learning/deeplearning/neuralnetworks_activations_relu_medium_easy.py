import numpy as np

def relu(x):
    """ReLU activation: max(0, x)"""
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    """Leaky ReLU activation: max(alpha*x, x)"""
    return np.where(x > 0, x, alpha * x)

def gelu(x):
    """
    GELU (Gaussian Error Linear Unit) activation.
    Approximation: 0.5 * x * (1 + tanh(sqrt(2/pi) * (x + 0.044715 * x^3)))
    """
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x**3)))

"""
NOTES:
1. ReLU:
   - Most common activation for hidden layers.
   - Pros: Simple, no vanishing gradient for positive values.
   - Cons: "Dying ReLU" problem (neurons can get stuck at 0).
   
2. Leaky ReLU:
   - Fixes dying ReLU by allowing small negative slope.
   - alpha typically 0.01 or 0.1.
   
3. GELU:
   - Used in transformers (BERT, GPT).
   - Smooth, non-monotonic.
   - Better than ReLU for some tasks.
   
4. Gradients:
   - ReLU: 1 if x > 0, else 0
   - Leaky ReLU: 1 if x > 0, else alpha
   - GELU: More complex, but smooth everywhere
"""
