import numpy as np

def layer_norm(x, gamma, beta, eps=1e-5):
    """
    Computes Layer Normalization.
    
    Args:
        x: Input data of shape (batch_size, sequence_length, hidden_dim) or similar.
           Normalization is performed over the last dimension.
        gamma: Scale parameter of shape (hidden_dim,)
        beta: Shift parameter of shape (hidden_dim,)
        eps: Epsilon for numerical stability
        
    Returns:
        out: Normalized output of same shape as x
    """
    # Mean and Variance over the last dimension
    mean = np.mean(x, axis=-1, keepdims=True)
    var = np.var(x, axis=-1, keepdims=True)
    
    # Normalize
    x_norm = (x - mean) / np.sqrt(var + eps)
    
    # Scale and Shift
    out = x_norm * gamma + beta
    
    return out
