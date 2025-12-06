import numpy as np

def gru_cell_forward(xt, h_prev, Wz, Uz, bz, Wr, Ur, br, Wh, Uh, bh):
    """
    Implements a single GRU cell forward pass.
    
    Args:
        xt: Input at time t, shape (batch_size, input_size)
        h_prev: Previous hidden state, shape (batch_size, hidden_size)
        Wz, Uz, bz: Weights and bias for update gate
        Wr, Ur, br: Weights and bias for reset gate
        Wh, Uh, bh: Weights and bias for candidate hidden state
        
    Returns:
        h_next: Next hidden state, shape (batch_size, hidden_size)
    """
    # Update gate: decides how much of past to keep
    zt = sigmoid(np.dot(xt, Wz.T) + np.dot(h_prev, Uz.T) + bz)
    
    # Reset gate: decides how much of past to forget
    rt = sigmoid(np.dot(xt, Wr.T) + np.dot(h_prev, Ur.T) + br)
    
    # Candidate hidden state: new information
    h_tilde = np.tanh(np.dot(xt, Wh.T) + np.dot(rt * h_prev, Uh.T) + bh)
    
    # Final hidden state: interpolation between previous and candidate
    h_next = (1 - zt) * h_prev + zt * h_tilde
    
    return h_next

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

"""
NOTES:
1. GRU vs LSTM:
   - GRU is simpler: 2 gates vs 3 gates
   - GRU has no separate cell state
   - GRU is faster to train (fewer parameters)
   - Performance is often similar
   
2. GRU Gates:
   - Update gate (zt): How much of previous hidden state to keep
   - Reset gate (rt): How much of previous hidden state to forget when computing candidate
   
3. Equations:
   - zt = σ(Wz·xt + Uz·h_{t-1} + bz)
   - rt = σ(Wr·xt + Ur·h_{t-1} + br)
   - h_tilde = tanh(Wh·xt + Uh·(rt ⊙ h_{t-1}) + bh)
   - ht = (1 - zt) ⊙ h_{t-1} + zt ⊙ h_tilde
   
4. Intuition:
   - When zt ≈ 1: Use new candidate (forget past)
   - When zt ≈ 0: Keep previous state (ignore new input)
   - Reset gate allows model to drop irrelevant history
"""
