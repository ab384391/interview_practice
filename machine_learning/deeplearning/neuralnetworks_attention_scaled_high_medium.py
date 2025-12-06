import numpy as np

def scaled_dot_product_attention(q, k, v, mask=None):
    """
    Computes scaled dot-product attention.
    
    Args:
        q: Queries of shape (..., seq_len_q, d_k)
        k: Keys of shape (..., seq_len_k, d_k)
        v: Values of shape (..., seq_len_v, d_v)
        mask: Optional mask of shape (..., seq_len_q, seq_len_k)
              0 or False indicates positions to mask out (set to -inf).
              1 or True indicates valid positions.
              Alternatively, mask can be additive (0 for valid, -inf for mask).
              Here we assume standard boolean mask (True=keep, False=mask) or None.
        
    Returns:
        output: Attention output of shape (..., seq_len_q, d_v)
        weights: Attention weights of shape (..., seq_len_q, seq_len_k)
    """
    d_k = q.shape[-1]
    
    # 1. Compute scores: Q @ K^T / sqrt(d_k)
    # q: (..., N, d_k)
    # k: (..., M, d_k) -> k.swapaxes(-2, -1): (..., d_k, M)
    # scores: (..., N, M)
    scores = np.matmul(q, k.swapaxes(-2, -1)) / np.sqrt(d_k)
    
    # 2. Apply mask
    if mask is not None:
        # Assuming mask is 0/1 or False/True where 0/False means "mask out"
        # We set masked positions to a very large negative number
        scores = np.where(mask, scores, -1e9)
    
    # 3. Softmax
    # Stability: subtract max
    max_scores = np.max(scores, axis=-1, keepdims=True)
    exp_scores = np.exp(scores - max_scores)
    weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)
    
    # 4. Compute output: weights @ V
    # weights: (..., N, M)
    # v: (..., M, d_v)
    # output: (..., N, d_v)
    output = np.matmul(weights, v)
    
    return output, weights

"""
NOTES:
1. Scaling Factor:
   - Division by sqrt(d_k) prevents dot products from growing too large in magnitude,
     which would push softmax into regions with extremely small gradients.
     
2. Masking:
   - Essential for decoder self-attention (causal mask) and handling padding.
   - In NumPy, `np.where` or boolean indexing is used.
   
3. Complexity:
   - Time: O(N^2 * d_k)
   - Space: O(N^2) to store attention weights.
"""
