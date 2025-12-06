import numpy as np

def multi_head_attention(x, num_heads, d_model, Wq, Wk, Wv, Wo, mask=None):
    """
    Implements multi-head attention.
    
    Args:
        x: Input, shape (batch_size, seq_len, d_model)
        num_heads: Number of attention heads
        d_model: Model dimension
        Wq, Wk, Wv: Weight matrices, each shape (d_model, d_model)
        Wo: Output projection, shape (d_model, d_model)
        mask: Optional attention mask
        
    Returns:
        output: Multi-head attention output, shape (batch_size, seq_len, d_model)
    """
    batch_size, seq_len, _ = x.shape
    d_k = d_model // num_heads
    
    # Linear projections
    Q = np.matmul(x, Wq)  # (batch, seq_len, d_model)
    K = np.matmul(x, Wk)
    V = np.matmul(x, Wv)
    
    # Reshape to separate heads
    # (batch, seq_len, d_model) -> (batch, seq_len, num_heads, d_k) -> (batch, num_heads, seq_len, d_k)
    Q = Q.reshape(batch_size, seq_len, num_heads, d_k).transpose(0, 2, 1, 3)
    K = K.reshape(batch_size, seq_len, num_heads, d_k).transpose(0, 2, 1, 3)
    V = V.reshape(batch_size, seq_len, num_heads, d_k).transpose(0, 2, 1, 3)
    
    # Scaled dot-product attention for each head
    scores = np.matmul(Q, K.swapaxes(-2, -1)) / np.sqrt(d_k)  # (batch, num_heads, seq_len, seq_len)
    
    if mask is not None:
        # Expand mask for heads
        mask = np.expand_dims(mask, 1)  # (batch, 1, seq_len, seq_len)
        scores = np.where(mask, scores, -1e9)
    
    # Softmax
    max_scores = np.max(scores, axis=-1, keepdims=True)
    exp_scores = np.exp(scores - max_scores)
    attn_weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)
    
    # Apply attention
    attn_output = np.matmul(attn_weights, V)  # (batch, num_heads, seq_len, d_k)
    
    # Concatenate heads
    # (batch, num_heads, seq_len, d_k) -> (batch, seq_len, num_heads, d_k) -> (batch, seq_len, d_model)
    attn_output = attn_output.transpose(0, 2, 1, 3).reshape(batch_size, seq_len, d_model)
    
    # Final linear projection
    output = np.matmul(attn_output, Wo)
    
    return output

"""
NOTES:
1. Multi-Head Attention:
   - Run multiple attention operations in parallel
   - Each head learns different aspects of relationships
   - Concatenate outputs and project
   
2. Why Multiple Heads:
   - Single head might focus on one type of relationship
   - Multiple heads can capture different patterns (syntax, semantics, etc.)
   - Empirically works better than single large head
   
3. Dimension Splitting:
   - d_model is split across heads: d_k = d_model / num_heads
   - Total computation is same as single head with d_model
   - But provides more representational power
   
4. Common Values:
   - BERT: 12 heads, d_model=768, d_k=64
   - GPT-3: 96 heads, d_model=12288, d_k=128
"""
