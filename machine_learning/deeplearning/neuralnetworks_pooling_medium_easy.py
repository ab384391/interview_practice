import numpy as np

def max_pool(x, pool_size=2, stride=None):
    """
    Applies 2D max pooling.
    
    Args:
        x: Input of shape (H, W)
        pool_size: Size of pooling window
        stride: Stride (defaults to pool_size)
        
    Returns:
        output: Max pooled output
    """
    if stride is None:
        stride = pool_size
    
    H, W = x.shape
    out_H = (H - pool_size) // stride + 1
    out_W = (W - pool_size) // stride + 1
    
    output = np.zeros((out_H, out_W), dtype=x.dtype)
    
    for i in range(out_H):
        for j in range(out_W):
            h_start = i * stride
            w_start = j * stride
            patch = x[h_start:h_start+pool_size, w_start:w_start+pool_size]
            output[i, j] = np.max(patch)
    
    return output

def avg_pool(x, pool_size=2, stride=None):
    """
    Applies 2D average pooling.
    
    Args:
        x: Input of shape (H, W)
        pool_size: Size of pooling window
        stride: Stride (defaults to pool_size)
        
    Returns:
        output: Average pooled output
    """
    if stride is None:
        stride = pool_size
    
    H, W = x.shape
    out_H = (H - pool_size) // stride + 1
    out_W = (W - pool_size) // stride + 1
    
    output = np.zeros((out_H, out_W), dtype=x.dtype)
    
    for i in range(out_H):
        for j in range(out_W):
            h_start = i * stride
            w_start = j * stride
            patch = x[h_start:h_start+pool_size, w_start:w_start+pool_size]
            output[i, j] = np.mean(patch)
    
    return output

"""
NOTES:
1. Purpose:
   - Max pooling: Downsampling while preserving strongest activations.
   - Avg pooling: Downsampling with smooth averaging.
   
2. Backpropagation:
   - Max pool: Gradient flows only to the max element in each window.
   - Avg pool: Gradient is distributed equally across all elements.
   
3. Common Settings:
   - 2x2 with stride 2 (non-overlapping) is most common.
   - Reduces spatial dimensions by half.
"""
