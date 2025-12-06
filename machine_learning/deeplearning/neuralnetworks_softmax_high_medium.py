import numpy as np

def softmax(x):
    """
    Computes the softmax function for each row of the input x.
    
    Args:
        x: Input data of shape (..., num_classes)
        
    Returns:
        out: Softmax probabilities of shape (..., num_classes)
    """
    # Numerical stability: subtract max
    # x shape: (..., C)
    max_x = np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x - max_x)
    
    # Sum over classes
    sum_exp_x = np.sum(exp_x, axis=-1, keepdims=True)
    
    return exp_x / sum_exp_x
