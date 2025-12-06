import numpy as np

def binary_cross_entropy(predictions, targets, eps=1e-12):
    """
    Computes binary cross-entropy loss.
    
    Args:
        predictions: Predicted probabilities, shape (N,) or (N, 1)
        targets: Ground truth labels (0 or 1), shape (N,) or (N, 1)
        eps: Small epsilon for numerical stability
        
    Returns:
        loss: Scalar loss value
    """
    # BCE = -mean(y*log(p) + (1-y)*log(1-p))
    # Add epsilon to avoid log(0)
    
    loss = -np.mean(
        targets * np.log(predictions + eps) + 
        (1 - targets) * np.log(1 - predictions + eps)
    )
    
    return loss

"""
NOTES:
1. Numerical Stability:
   - Adding epsilon prevents log(0) which would give -inf.
   - In practice, predictions should already be clipped to [eps, 1-eps].
   
2. Relationship to Cross-Entropy:
   - BCE is a special case of cross-entropy for binary classification.
   - For multi-class: use categorical cross-entropy.
   
3. Logits vs Probabilities:
   - This function expects probabilities (after sigmoid).
   - For numerical stability, use binary_cross_entropy_with_logits in production.
"""
