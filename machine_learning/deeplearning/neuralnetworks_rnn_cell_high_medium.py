import numpy as np

def rnn_cell_forward(xt, h_prev, Wx, Wh, b):
    """
    Computes a single time step of a basic RNN.
    
    Args:
        xt: Input at time t, shape (batch_size, input_size)
        h_prev: Hidden state at time t-1, shape (batch_size, hidden_size)
        Wx: Input weights, shape (hidden_size, input_size)
        Wh: Hidden weights, shape (hidden_size, hidden_size)
        b: Bias, shape (hidden_size,)
        
    Returns:
        h_next: Hidden state at time t, shape (batch_size, hidden_size)
    """
    # h_t = tanh(x_t @ W_x^T + h_{t-1} @ W_h^T + b)
    
    # Linear transformations
    linear_x = np.dot(xt, Wx.T)
    linear_h = np.dot(h_prev, Wh.T)
    
    # Activation
    h_next = np.tanh(linear_x + linear_h + b)
    
    return h_next

"""
NOTES:
1. Vanishing Gradients:
   - Basic RNNs suffer from vanishing gradients over long sequences because the gradient
     flows through many matrix multiplications and tanh derivatives (which are < 1).
   - Solution: Use LSTM or GRU.
   
2. Shapes:
   - Wx maps input space to hidden space.
   - Wh maps hidden space to hidden space (recurrence).
"""
