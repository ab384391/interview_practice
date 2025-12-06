import numpy as np

def self_attention(x, Wq, Wk, Wv, mask=None):
    """
    Implements self-attention mechanism.
    
    Args:
        x: Input sequence, shape (batch_size, seq_len, d_model)
        Wq: Query weight matrix, shape (d_model, d_k)
        Wk: Key weight matrix, shape (d_model, d_k)
        Wv: Value weight matrix, shape (d_model, d_v)
        mask: Optional attention mask
        
    Returns:
        output: Attention output, shape (batch_size, seq_len, d_v)
        weights: Attention weights, shape (batch_size, seq_len, seq_len)
    """
    # Project to Q, K, V
    Q = np.matmul(x, Wq)  # (batch, seq_len, d_k)
    K = np.matmul(x, Wk)  # (batch, seq_len, d_k)
    V = np.matmul(x, Wv)  # (batch, seq_len, d_v)
    
    d_k = Q.shape[-1]
    
    # Compute attention scores
    scores = np.matmul(Q, K.swapaxes(-2, -1)) / np.sqrt(d_k)  # (batch, seq_len, seq_len)
    
    # Apply mask if provided
    if mask is not None:
        scores = np.where(mask, scores, -1e9)
    
    # Softmax
    max_scores = np.max(scores, axis=-1, keepdims=True)
    exp_scores = np.exp(scores - max_scores)
    weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)
    
    # Apply attention to values
    output = np.matmul(weights, V)  # (batch, seq_len, d_v)
    
    return output, weights

"""
NOTES:
1. Self-Attention vs Attention:
   - Self-attention: Q, K, V all come from the same input sequence
   - Cross-attention: Q from one sequence, K, V from another
   
2. Key Components:
   - Linear projections: x -> Q, K, V
   - Scaled dot-product: Q @ K^T / sqrt(d_k)
   - Softmax: Convert scores to probabilities
   - Weighted sum: Attention weights @ V
   
3. Computational Complexity:
   - Time: O(n^2 * d) where n = seq_len, d = d_model
   - Space: O(n^2) for attention matrix
   - This is why long sequences are expensive!
   
4. Masking:
   - Causal mask: Prevent attending to future positions (decoder)
   - Padding mask: Ignore padding tokens
"""
