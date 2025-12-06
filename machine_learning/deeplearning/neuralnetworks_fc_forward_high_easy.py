import numpy as np

def fc_forward(x, w, b):
    """
    Computes the forward pass for a fully connected (dense) layer.
    
    Args:
        x: Input data of shape (batch_size, in_features)
        w: Weights of shape (out_features, in_features)
        b: Biases of shape (out_features,)
        
    Returns:
        out: Output of shape (batch_size, out_features)
    """
    # Linear transformation: y = xW^T + b
    # x shape: (N, D_in)
    # w shape: (D_out, D_in) -> w.T shape: (D_in, D_out)
    # b shape: (D_out,)
    # out shape: (N, D_out)
    
    out = np.dot(x, w.T) + b
    return out

"""
NOTES:
1. Vectorization:
   - This implementation uses NumPy's optimized BLAS/LAPACK bindings via `np.dot`.
   - A naive implementation using for-loops would be O(N * D_out * D_in) in Python, which is significantly slower.
   
2. Shapes & Broadcasting:
   - x: (N, D_in)
   - w: (D_out, D_in) -> w.T: (D_in, D_out)
   - x @ w.T results in (N, D_out)
   - b: (D_out,) is broadcasted across the batch dimension N to match (N, D_out).
   
3. Edge Cases:
   - Batch size 1: Works correctly due to broadcasting.
   - Mismatched shapes: `np.dot` will raise a ValueError if x.shape[1] != w.shape[1].
   - Non-2D inputs: If x is (D_in,), it treats it as 1D. For ML, we usually ensure x is at least 2D (batch dim).
"""
