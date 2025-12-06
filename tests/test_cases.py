import numpy as np

def assert_close(actual, expected, rtol=1e-5, atol=1e-8):
    np.testing.assert_allclose(actual, expected, rtol=rtol, atol=atol)

def fc_forward(module):
    print("Testing fc_forward...")
    
    # Test Case 1: Basic
    batch_size = 2
    in_features = 3
    out_features = 4
    
    x = np.random.randn(batch_size, in_features).astype(np.float32)
    w = np.random.randn(out_features, in_features).astype(np.float32)
    b = np.random.randn(out_features).astype(np.float32)
    
    # Expected
    expected = np.dot(x, w.T) + b
    
    # Actual
    if not hasattr(module, 'fc_forward'):
        raise AssertionError("Module does not have function 'fc_forward'")
    
    actual = module.fc_forward(x, w, b)
    
    assert_close(actual, expected)
    print("  Case 1 passed")

def embedding(module):
    print("Testing embedding_lookup...")
    
    # Test Case 1: Basic
    vocab_size = 10
    embed_dim = 4
    num_indices = 5
    
    matrix = np.random.randn(vocab_size, embed_dim).astype(np.float32)
    indices = np.array([1, 5, 9, 0, 2])
    
    # Expected
    expected = matrix[indices]
    
    # Actual
    if not hasattr(module, 'embedding_lookup'):
        raise AssertionError("Module does not have function 'embedding_lookup'")
        
    # Plan said: def embedding_lookup(indices, embedding_matrix):
    actual = module.embedding_lookup(indices, matrix)
    
    assert_close(actual, expected)
    print("  Case 1 passed")

def softmax(module):
    print("Testing softmax...")
    
    # Test Case 1: Basic
    x = np.array([[1.0, 2.0, 3.0], [1.0, -1.0, 0.0]], dtype=np.float32)
    
    # Expected (stable)
    max_x = np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x - max_x)
    expected = exp_x / np.sum(exp_x, axis=-1, keepdims=True)
    
    # Actual
    if not hasattr(module, 'softmax'):
        raise AssertionError("Module does not have function 'softmax'")
        
    actual = module.softmax(x)
    
    assert_close(actual, expected)
    print("  Case 1 passed")

def cross_entropy(module):
    print("Testing cross_entropy_loss...")
    
    # Test Case 1: Basic
    batch_size = 3
    num_classes = 4
    logits = np.random.randn(batch_size, num_classes).astype(np.float32)
    targets = np.array([0, 2, 3]) # Indices
    
    # Expected
    # Softmax
    max_logits = np.max(logits, axis=-1, keepdims=True)
    exp_logits = np.exp(logits - max_logits)
    probs = exp_logits / np.sum(exp_logits, axis=-1, keepdims=True)
    
    # NLL
    # Select prob for correct class
    correct_probs = probs[np.arange(batch_size), targets]
    expected = -np.mean(np.log(correct_probs + 1e-12))
    
    # Actual
    if not hasattr(module, 'cross_entropy_loss'):
        raise AssertionError("Module does not have function 'cross_entropy_loss'")
        
    actual = module.cross_entropy_loss(logits, targets)
    
    assert_close(actual, expected)
    print("  Case 1 passed")

def layer_norm(module):
    print("Testing layer_norm...")
    
    # Test Case 1: Basic
    batch_size = 2
    seq_len = 3
    embed_dim = 4
    
    x = np.random.randn(batch_size, seq_len, embed_dim).astype(np.float32)
    gamma = np.ones((embed_dim,), dtype=np.float32)
    beta = np.zeros((embed_dim,), dtype=np.float32)
    eps = 1e-5
    
    # Expected
    mean = np.mean(x, axis=-1, keepdims=True)
    var = np.var(x, axis=-1, keepdims=True)
    expected = (x - mean) / np.sqrt(var + eps) * gamma + beta
    
    # Actual
    if not hasattr(module, 'layer_norm'):
        raise AssertionError("Module does not have function 'layer_norm'")
        
    actual = module.layer_norm(x, gamma, beta, eps)
    
    assert_close(actual, expected)
    print("  Case 1 passed")

def scaled_dot_product_attention(module):
    print("Testing scaled_dot_product_attention...")
    
    # Test Case 1: Basic
    batch_size = 2
    n_heads = 1 # Simplified for basic attention
    seq_len = 3
    d_k = 4
    
    q = np.random.randn(batch_size, seq_len, d_k).astype(np.float32)
    k = np.random.randn(batch_size, seq_len, d_k).astype(np.float32)
    v = np.random.randn(batch_size, seq_len, d_k).astype(np.float32)
    mask = None
    
    # Expected
    scores = np.matmul(q, k.swapaxes(-2, -1)) / np.sqrt(d_k)
    attn_weights = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
    attn_weights /= np.sum(attn_weights, axis=-1, keepdims=True)
    expected = np.matmul(attn_weights, v)
    
    # Actual
    if not hasattr(module, 'scaled_dot_product_attention'):
        raise AssertionError("Module does not have function 'scaled_dot_product_attention'")
        
    actual, weights = module.scaled_dot_product_attention(q, k, v, mask)
    
    assert_close(actual, expected)
    assert_close(weights, attn_weights)
    print("  Case 1 passed")

def rnn_cell(module):
    print("Testing rnn_cell_forward...")
    
    # Test Case 1: Basic
    batch_size = 2
    input_size = 3
    hidden_size = 4
    
    xt = np.random.randn(batch_size, input_size).astype(np.float32)
    h_prev = np.random.randn(batch_size, hidden_size).astype(np.float32)
    
    Wx = np.random.randn(hidden_size, input_size).astype(np.float32)
    Wh = np.random.randn(hidden_size, hidden_size).astype(np.float32)
    b = np.random.randn(hidden_size).astype(np.float32)
    
    # Expected: h_next = tanh(xt @ Wx.T + h_prev @ Wh.T + b)
    linear = np.dot(xt, Wx.T) + np.dot(h_prev, Wh.T) + b
    expected = np.tanh(linear)
    
    # Actual
    if not hasattr(module, 'rnn_cell_forward'):
        raise AssertionError("Module does not have function 'rnn_cell_forward'")
        
    actual = module.rnn_cell_forward(xt, h_prev, Wx, Wh, b)
    
    assert_close(actual, expected)
    print("  Case 1 passed")

def conv2d_filter(module):
    print("Testing conv2d_filter...")
    
    # Test Case 1: 3x3 input, 2x2 kernel, valid padding
    image = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]], dtype=np.float32)
    kernel = np.array([[1, 0],
                       [0, -1]], dtype=np.float32)
    
    # Expected output (2x2)
    # [1*1 + 5*-1, 2*1 + 6*-1] = [-4, -4]
    # [4*1 + 8*-1, 5*1 + 9*-1] = [-4, -4]
    expected = np.array([[-4, -4], [-4, -4]], dtype=np.float32)
    
    # Actual
    if not hasattr(module, 'conv2d_filter'):
        raise AssertionError("Module does not have function 'conv2d_filter'")
        
    actual = module.conv2d_filter(image, kernel)
    
    assert_close(actual, expected)
    print("  Case 1 passed")

def fc_backward(module):
    print("Testing fc_backward...")
    
    # Test Case 1: Basic
    batch_size = 2
    in_features = 3
    out_features = 4
    
    d_out = np.random.randn(batch_size, out_features).astype(np.float32)
    x = np.random.randn(batch_size, in_features).astype(np.float32)
    w = np.random.randn(out_features, in_features).astype(np.float32)
    b = np.random.randn(out_features).astype(np.float32)
    
    # Expected
    # d_x = d_out @ w
    # d_w = d_out.T @ x
    # d_b = sum(d_out, axis=0)
    expected_dx = np.dot(d_out, w)
    expected_dw = np.dot(d_out.T, x)
    expected_db = np.sum(d_out, axis=0)
    
    # Actual
    if not hasattr(module, 'fc_backward'):
        raise AssertionError("Module does not have function 'fc_backward'")
        
    dx, dw, db = module.fc_backward(d_out, x, w, b)
    
    assert_close(dx, expected_dx)
    assert_close(dw, expected_dw)
    assert_close(db, expected_db)
    print("  Case 1 passed")

def pooling(module):
    print("Testing max_pool and avg_pool...")
    
    # Test Case 1: 4x4 input, 2x2 pool
    x = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]], dtype=np.float32)
    
    # Expected max pool (2x2)
    expected_max = np.array([[6, 8], [14, 16]], dtype=np.float32)
    # Expected avg pool (2x2)
    expected_avg = np.array([[3.5, 5.5], [11.5, 13.5]], dtype=np.float32)
    
    if not hasattr(module, 'max_pool') or not hasattr(module, 'avg_pool'):
        raise AssertionError("Module missing max_pool or avg_pool")
    
    actual_max = module.max_pool(x, pool_size=2)
    actual_avg = module.avg_pool(x, pool_size=2)
    
    assert_close(actual_max, expected_max)
    assert_close(actual_avg, expected_avg)
    print("  Case 1 passed")

def dropout(module):
    print("Testing dropout...")
    
    # Test Case 1: Training mode
    x = np.ones((10, 5), dtype=np.float32)
    p = 0.5
    
    if not hasattr(module, 'dropout'):
        raise AssertionError("Module does not have function 'dropout'")
    
    # Training mode - should zero out some elements and scale
    out_train = module.dropout(x, p, training=True)
    # Check that some elements are zero
    assert np.any(out_train == 0), "Dropout should zero some elements in training"
    # Check scaling (non-zero elements should be scaled by 1/(1-p))
    non_zero = out_train[out_train != 0]
    if len(non_zero) > 0:
        assert_close(non_zero, np.ones_like(non_zero) / (1 - p))
    
    # Inference mode - should return input unchanged
    out_infer = module.dropout(x, p, training=False)
    assert_close(out_infer, x)
    print("  Case 1 passed")

def binary_cross_entropy(module):
    print("Testing binary_cross_entropy...")
    
    predictions = np.array([0.9, 0.1, 0.8, 0.3], dtype=np.float32)
    targets = np.array([1, 0, 1, 0], dtype=np.float32)
    
    # Expected: -mean(y*log(p) + (1-y)*log(1-p))
    eps = 1e-12
    expected = -np.mean(targets * np.log(predictions + eps) + 
                       (1 - targets) * np.log(1 - predictions + eps))
    
    if not hasattr(module, 'binary_cross_entropy'):
        raise AssertionError("Module does not have function 'binary_cross_entropy'")
    
    actual = module.binary_cross_entropy(predictions, targets)
    assert_close(actual, expected)
    print("  Case 1 passed")

def activations_relu(module):
    print("Testing ReLU, Leaky ReLU, GELU...")
    
    x = np.array([-2, -1, 0, 1, 2], dtype=np.float32)
    
    # ReLU
    expected_relu = np.array([0, 0, 0, 1, 2], dtype=np.float32)
    # Leaky ReLU (alpha=0.01)
    expected_leaky = np.array([-0.02, -0.01, 0, 1, 2], dtype=np.float32)
    
    if not hasattr(module, 'relu'):
        raise AssertionError("Module missing relu")
    
    actual_relu = module.relu(x)
    actual_leaky = module.leaky_relu(x, alpha=0.01)
    
    assert_close(actual_relu, expected_relu)
    assert_close(actual_leaky, expected_leaky)
    
    # GELU - just check it runs and has right shape
    if hasattr(module, 'gelu'):
        actual_gelu = module.gelu(x)
        assert actual_gelu.shape == x.shape
    
    print("  Case 1 passed")

def activations_sigmoid(module):
    print("Testing sigmoid and tanh...")
    
    x = np.array([-2, -1, 0, 1, 2], dtype=np.float32)
    
    # Expected
    expected_sigmoid = 1 / (1 + np.exp(-x))
    expected_tanh = np.tanh(x)
    
    if not hasattr(module, 'sigmoid') or not hasattr(module, 'tanh_activation'):
        raise AssertionError("Module missing sigmoid or tanh_activation")
    
    actual_sigmoid = module.sigmoid(x)
    actual_tanh = module.tanh_activation(x)
    
    assert_close(actual_sigmoid, expected_sigmoid)
    assert_close(actual_tanh, expected_tanh)
    print("  Case 1 passed")

def weight_init(module):
    print("Testing weight initialization...")
    
    shape = (100, 50)
    
    if not hasattr(module, 'xavier_init') or not hasattr(module, 'he_init'):
        raise AssertionError("Module missing xavier_init or he_init")
    
    # Xavier
    xavier_weights = module.xavier_init(shape)
    assert xavier_weights.shape == shape
    # Check variance is approximately correct
    expected_var_xavier = 2.0 / (shape[0] + shape[1])
    actual_var = np.var(xavier_weights)
    assert abs(actual_var - expected_var_xavier) < 0.05, f"Xavier var {actual_var} vs expected {expected_var_xavier}"
    
    # He
    he_weights = module.he_init(shape)
    assert he_weights.shape == shape
    expected_var_he = 2.0 / shape[0]
    actual_var_he = np.var(he_weights)
    assert abs(actual_var_he - expected_var_he) < 0.05, f"He var {actual_var_he} vs expected {expected_var_he}"
    
    print("  Case 1 passed")
