import numpy as np

def cross_entropy_loss(logits, targets):
    """
    Computes the cross-entropy loss between logits and targets.
    
    Args:
        logits: Input logits of shape (batch_size, num_classes)
        targets: Target indices of shape (batch_size,)
        
    Returns:
        loss: Scalar loss value (mean over batch)
    """
    # 1. Compute softmax probabilities
    # Stability: subtract max
    max_logits = np.max(logits, axis=-1, keepdims=True)
    exp_logits = np.exp(logits - max_logits)
    probs = exp_logits / np.sum(exp_logits, axis=-1, keepdims=True)
    
    # 2. Select probabilities for target classes
    batch_size = logits.shape[0]
    # Advanced indexing: [0...N-1], [target_0...target_N-1]
    correct_class_probs = probs[np.arange(batch_size), targets]
    
    # 3. Compute negative log likelihood
    # Add epsilon for numerical stability
    loss = -np.mean(np.log(correct_class_probs + 1e-12))
    
    return loss
