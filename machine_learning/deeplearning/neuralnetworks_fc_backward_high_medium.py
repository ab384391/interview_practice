import numpy as np

def fc_backward(d_out, x, w, b):
    """
    Computes the backward pass for a fully connected layer.
    
    Args:
        d_out: Gradient of loss w.r.t. output, shape (batch_size, out_features)
        x: Input data, shape (batch_size, in_features)
        w: Weights, shape (out_features, in_features)
        b: Biases, shape (out_features,)
        
    Returns:
        dx: Gradient w.r.t. input, shape (batch_size, in_features)
        dw: Gradient w.r.t. weights, shape (out_features, in_features)
        db: Gradient w.r.t. biases, shape (out_features,)
    """
    # Forward pass was: out = x @ w.T + b
    # Chain rule:
    # dx = d_out @ w
    # dw = d_out.T @ x
    # db = sum(d_out, axis=0)
    
    dx = np.dot(d_out, w)
    dw = np.dot(d_out.T, x)
    db = np.sum(d_out, axis=0)
    
    return dx, dw, db

"""
NOTES:
1. Derivation:
   - Forward: y = xW^T + b where x: (N, D_in), W: (D_out, D_in), b: (D_out,)
   - dy/dx = W -> dx = d_out @ W
   - dy/dW = x^T -> dW = d_out^T @ x
   - dy/db = 1 -> db = sum(d_out) over batch dimension
   
2. Shapes:
   - d_out: (N, D_out)
   - w: (D_out, D_in)
   - dx: (N, D_in) = d_out @ w
   - dw: (D_out, D_in) = d_out.T @ x
   - db: (D_out,) = sum over batch
   
3. Memory:
   - We need to cache x and w from the forward pass for backprop.
"""
