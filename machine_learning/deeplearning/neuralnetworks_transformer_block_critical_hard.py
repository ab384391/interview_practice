import numpy as np

def transformer_block(x, num_heads, d_model, d_ff, Wq, Wk, Wv, Wo, W1, b1, W2, b2, gamma1, beta1, gamma2, beta2, dropout_rate=0.1, training=True):
    """
    Implements a complete Transformer block (encoder layer).
    Components: Multi-Head Attention + Add & Norm + Feed-Forward + Add & Norm
    
    Args:
        x: Input, shape (batch_size, seq_len, d_model)
        num_heads: Number of attention heads
        d_model: Model dimension
        d_ff: Feed-forward hidden dimension
        Wq, Wk, Wv, Wo: Attention weight matrices
        W1, b1, W2, b2: Feed-forward network weights
        gamma1, beta1: Layer norm params for first sub-layer
        gamma2, beta2: Layer norm params for second sub-layer
        dropout_rate: Dropout probability
        training: Whether in training mode
        
    Returns:
        output: Transformer block output, shape (batch_size, seq_len, d_model)
    """
    batch_size, seq_len, _ = x.shape
    d_k = d_model // num_heads
    
    # ========== MULTI-HEAD ATTENTION ==========
    # Linear projections
    Q = np.matmul(x, Wq)
    K = np.matmul(x, Wk)
    V = np.matmul(x, Wv)
    
    # Reshape for multi-head
    Q = Q.reshape(batch_size, seq_len, num_heads, d_k).transpose(0, 2, 1, 3)
    K = K.reshape(batch_size, seq_len, num_heads, d_k).transpose(0, 2, 1, 3)
    V = V.reshape(batch_size, seq_len, num_heads, d_k).transpose(0, 2, 1, 3)
    
    # Attention
    scores = np.matmul(Q, K.swapaxes(-2, -1)) / np.sqrt(d_k)
    max_scores = np.max(scores, axis=-1, keepdims=True)
    exp_scores = np.exp(scores - max_scores)
    attn_weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)
    
    attn_output = np.matmul(attn_weights, V)
    attn_output = attn_output.transpose(0, 2, 1, 3).reshape(batch_size, seq_len, d_model)
    attn_output = np.matmul(attn_output, Wo)
    
    # Dropout
    if training:
        mask = np.random.binomial(1, 1-dropout_rate, size=attn_output.shape)
        attn_output = attn_output * mask / (1 - dropout_rate)
    
    # Add & Norm 1
    x = x + attn_output  # Residual connection
    mean1 = np.mean(x, axis=-1, keepdims=True)
    var1 = np.var(x, axis=-1, keepdims=True)
    x = (x - mean1) / np.sqrt(var1 + 1e-5) * gamma1 + beta1
    
    # ========== FEED-FORWARD NETWORK ==========
    # FFN: Linear -> ReLU -> Linear
    ff_output = np.dot(x, W1.T) + b1  # (batch, seq_len, d_ff)
    ff_output = np.maximum(0, ff_output)  # ReLU
    ff_output = np.dot(ff_output, W2.T) + b2  # (batch, seq_len, d_model)
    
    # Dropout
    if training:
        mask = np.random.binomial(1, 1-dropout_rate, size=ff_output.shape)
        ff_output = ff_output * mask / (1 - dropout_rate)
    
    # Add & Norm 2
    output = x + ff_output  # Residual connection
    mean2 = np.mean(output, axis=-1, keepdims=True)
    var2 = np.var(output, axis=-1, keepdims=True)
    output = (output - mean2) / np.sqrt(var2 + 1e-5) * gamma2 + beta2
    
    return output

"""
NOTES:
1. Transformer Block Components:
   - Multi-Head Self-Attention
   - Residual Connection + Layer Normalization
   - Position-wise Feed-Forward Network
   - Residual Connection + Layer Normalization
   
2. Residual Connections:
   - Help gradients flow through deep networks
   - Allow model to learn identity function easily
   - Formula: output = LayerNorm(x + Sublayer(x))
   
3. Layer Normalization:
   - Normalizes across feature dimension (not batch)
   - More stable than batch norm for variable-length sequences
   - Applied after residual connection
   
4. Feed-Forward Network:
   - Two linear layers with ReLU in between
   - Applied independently to each position
   - Typically d_ff = 4 * d_model
   
5. Dropout:
   - Applied after attention and FFN
   - Helps prevent overfitting
   - Typical rate: 0.1
"""
