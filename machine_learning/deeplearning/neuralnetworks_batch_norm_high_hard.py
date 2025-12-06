import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Batch normalization forward pass.
    
    Args:
        x: Input, shape (batch_size, features) or (batch_size, height, width, channels)
        gamma: Scale parameter, shape (features,) or (channels,)
        beta: Shift parameter, shape (features,) or (channels,)
        eps: Small constant for numerical stability
        
    Returns:
        out: Normalized output, same shape as x
        cache: Values needed for backward pass
    """
    # Compute mean and variance across batch dimension
    # For 2D: axis=0, for 4D (images): axis=(0, 1, 2)
    if x.ndim == 2:
        axis = 0
    elif x.ndim == 4:
        axis = (0, 1, 2)
    else:
        axis = 0
    
    mean = np.mean(x, axis=axis, keepdims=True)
    var = np.var(x, axis=axis, keepdims=True)
    
    # Normalize
    x_norm = (x - mean) / np.sqrt(var + eps)
    
    # Scale and shift
    out = gamma * x_norm + beta
    
    # Cache for backward pass
    cache = (x, x_norm, mean, var, gamma, beta, eps)
    
    return out, cache

def batch_norm_backward(dout, cache):
    """
    Batch normalization backward pass.
    
    Args:
        dout: Gradient of loss w.r.t. output, same shape as forward input
        cache: Cached values from forward pass
        
    Returns:
        dx: Gradient w.r.t. input
        dgamma: Gradient w.r.t. gamma
        dbeta: Gradient w.r.t. beta
    """
    x, x_norm, mean, var, gamma, beta, eps = cache
    
    if x.ndim == 2:
        N = x.shape[0]
        axis = 0
    elif x.ndim == 4:
        N = x.shape[0] * x.shape[1] * x.shape[2]
        axis = (0, 1, 2)
    else:
        N = x.shape[0]
        axis = 0
    
    # Gradient w.r.t. gamma and beta
    dgamma = np.sum(dout * x_norm, axis=axis, keepdims=True)
    dbeta = np.sum(dout, axis=axis, keepdims=True)
    
    # Gradient w.r.t. normalized x
    dx_norm = dout * gamma
    
    # Gradient w.r.t. variance
    dvar = np.sum(dx_norm * (x - mean) * -0.5 * (var + eps)**(-1.5), axis=axis, keepdims=True)
    
    # Gradient w.r.t. mean
    dmean = np.sum(dx_norm * -1.0 / np.sqrt(var + eps), axis=axis, keepdims=True)
    dmean += dvar * np.mean(-2.0 * (x - mean), axis=axis, keepdims=True)
    
    # Gradient w.r.t. x
    dx = dx_norm / np.sqrt(var + eps)
    dx += dvar * 2.0 * (x - mean) / N
    dx += dmean / N
    
    return dx, dgamma.squeeze(), dbeta.squeeze()

"""
NOTES:
1. Batch Normalization:
   - Normalizes activations across the batch dimension
   - Reduces internal covariate shift
   - Allows higher learning rates
   
2. Training vs Inference:
   - Training: Use batch statistics (mean, var)
   - Inference: Use running statistics (exponential moving average)
   - This implementation shows training mode
   
3. Why It Works:
   - Keeps activations in a reasonable range
   - Reduces dependence on initialization
   - Acts as regularization (noise from batch statistics)
   
4. Backward Pass:
   - Complex due to mean and variance depending on all batch elements
   - Each element's gradient depends on all other elements
   - Chain rule through normalization, variance, and mean
   
5. Layer Norm vs Batch Norm:
   - Layer norm: Normalize across features (better for RNNs/Transformers)
   - Batch norm: Normalize across batch (better for CNNs)
"""
