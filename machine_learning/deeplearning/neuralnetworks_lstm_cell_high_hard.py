import numpy as np

def lstm_cell_forward(xt, h_prev, c_prev, Wf, Uf, bf, Wi, Ui, bi, Wc, Uc, bc, Wo, Uo, bo):
    """
    Implements a single LSTM cell forward pass.
    
    Args:
        xt: Input at time t, shape (batch_size, input_size)
        h_prev: Previous hidden state, shape (batch_size, hidden_size)
        c_prev: Previous cell state, shape (batch_size, hidden_size)
        Wf, Wi, Wc, Wo: Input weights for forget, input, cell, output gates
        Uf, Ui, Uc, Uo: Hidden weights for forget, input, cell, output gates
        bf, bi, bc, bo: Biases for forget, input, cell, output gates
        
    Returns:
        h_next: Next hidden state, shape (batch_size, hidden_size)
        c_next: Next cell state, shape (batch_size, hidden_size)
    """
    # Forget gate: decides what to forget from cell state
    ft = sigmoid(np.dot(xt, Wf.T) + np.dot(h_prev, Uf.T) + bf)
    
    # Input gate: decides what new information to store
    it = sigmoid(np.dot(xt, Wi.T) + np.dot(h_prev, Ui.T) + bi)
    
    # Candidate cell state: new information to potentially add
    c_tilde = np.tanh(np.dot(xt, Wc.T) + np.dot(h_prev, Uc.T) + bc)
    
    # Update cell state
    c_next = ft * c_prev + it * c_tilde
    
    # Output gate: decides what to output
    ot = sigmoid(np.dot(xt, Wo.T) + np.dot(h_prev, Uo.T) + bo)
    
    # Hidden state
    h_next = ot * np.tanh(c_next)
    
    return h_next, c_next

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

"""
NOTES:
1. LSTM Gates:
   - Forget gate (ft): What to forget from previous cell state
   - Input gate (it): What new information to add
   - Output gate (ot): What to output based on cell state
   - Cell gate (c_tilde): Candidate values to add to cell state
   
2. Cell State vs Hidden State:
   - Cell state (c): Long-term memory, flows with minimal modification
   - Hidden state (h): Short-term memory, output at each step
   
3. Why LSTM Works:
   - Solves vanishing gradient problem of vanilla RNN
   - Cell state provides a "highway" for gradients
   - Gates control information flow
   
4. Equations:
   - ft = σ(Wf·xt + Uf·h_{t-1} + bf)
   - it = σ(Wi·xt + Ui·h_{t-1} + bi)
   - c_tilde = tanh(Wc·xt + Uc·h_{t-1} + bc)
   - ct = ft ⊙ c_{t-1} + it ⊙ c_tilde
   - ot = σ(Wo·xt + Uo·h_{t-1} + bo)
   - ht = ot ⊙ tanh(ct)
"""
