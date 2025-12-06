import numpy as np

def backprop_2layer_nn(x, y, w1, b1, w2, b2, learning_rate=0.01):
    """
    Implements forward and backward pass for a 2-layer neural network.
    Architecture: Input -> FC1 -> ReLU -> FC2 -> Output
    Loss: MSE
    
    Args:
        x: Input data, shape (batch_size, input_dim)
        y: Target labels, shape (batch_size, output_dim)
        w1: First layer weights, shape (hidden_dim, input_dim)
        b1: First layer biases, shape (hidden_dim,)
        w2: Second layer weights, shape (output_dim, hidden_dim)
        b2: Second layer biases, shape (output_dim,)
        learning_rate: Learning rate for gradient descent
        
    Returns:
        loss: Scalar loss value
        w1, b1, w2, b2: Updated weights and biases
        grads: Dictionary of gradients
    """
    batch_size = x.shape[0]
    
    # ========== FORWARD PASS ==========
    # Layer 1
    z1 = np.dot(x, w1.T) + b1  # (N, hidden_dim)
    a1 = np.maximum(0, z1)  # ReLU activation
    
    # Layer 2
    z2 = np.dot(a1, w2.T) + b2  # (N, output_dim)
    # No activation (linear output for regression)
    
    # Loss (MSE)
    loss = np.mean((z2 - y) ** 2)
    
    # ========== BACKWARD PASS ==========
    # Gradient of loss w.r.t. z2
    # d(MSE)/dz2 = 2/N * (z2 - y)
    dz2 = 2.0 / batch_size * (z2 - y)  # (N, output_dim)
    
    # Gradients for layer 2
    dw2 = np.dot(dz2.T, a1)  # (output_dim, hidden_dim)
    db2 = np.sum(dz2, axis=0)  # (output_dim,)
    
    # Backprop to layer 1
    da1 = np.dot(dz2, w2)  # (N, hidden_dim)
    
    # ReLU gradient
    dz1 = da1 * (z1 > 0)  # (N, hidden_dim)
    
    # Gradients for layer 1
    dw1 = np.dot(dz1.T, x)  # (hidden_dim, input_dim)
    db1 = np.sum(dz1, axis=0)  # (hidden_dim,)
    
    # ========== UPDATE WEIGHTS ==========
    w1 = w1 - learning_rate * dw1
    b1 = b1 - learning_rate * db1
    w2 = w2 - learning_rate * dw2
    b2 = b2 - learning_rate * db2
    
    grads = {
        'dw1': dw1,
        'db1': db1,
        'dw2': dw2,
        'db2': db2
    }
    
    return loss, w1, b1, w2, b2, grads

"""
NOTES:
1. Architecture:
   - 2-layer NN = 1 hidden layer + 1 output layer
   - Activation: ReLU for hidden, linear for output
   - Loss: MSE (can be changed to cross-entropy for classification)
   
2. Backpropagation Chain Rule:
   - Start from loss, work backwards through each layer
   - For each layer: compute gradient w.r.t. weights, biases, and inputs
   - ReLU gradient: 1 if z > 0, else 0
   
3. Gradient Shapes:
   - dw has same shape as w
   - db has same shape as b
   - Intermediate gradients match forward activations
   
4. Common Mistakes:
   - Forgetting to average gradients over batch (divide by N)
   - Wrong transpose in matrix multiplication
   - Not caching forward pass values needed for backward pass
"""
