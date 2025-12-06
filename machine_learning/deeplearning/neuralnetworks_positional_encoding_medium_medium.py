import numpy as np

def positional_encoding(seq_len, d_model):
    """
    Generates sinusoidal positional encodings for transformers.
    
    Args:
        seq_len: Sequence length
        d_model: Model dimension (embedding size)
        
    Returns:
        pe: Positional encoding matrix of shape (seq_len, d_model)
    """
    pe = np.zeros((seq_len, d_model))
    
    # Position indices
    position = np.arange(seq_len).reshape(-1, 1)  # (seq_len, 1)
    
    # Dimension indices
    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))
    
    # Apply sin to even indices
    pe[:, 0::2] = np.sin(position * div_term)
    
    # Apply cos to odd indices
    pe[:, 1::2] = np.cos(position * div_term)
    
    return pe.astype(np.float32)

"""
NOTES:
1. Formula:
   - PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
   - PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
   
2. Properties:
   - Each dimension has a different frequency.
   - Allows model to learn relative positions.
   - Can extrapolate to longer sequences than seen during training.
   
3. Why Sinusoidal:
   - PE(pos+k) can be represented as a linear function of PE(pos).
   - This helps the model learn to attend by relative positions.
   
4. Alternatives:
   - Learned positional embeddings (used in BERT).
   - Rotary positional embeddings (RoPE, used in modern LLMs).
"""
