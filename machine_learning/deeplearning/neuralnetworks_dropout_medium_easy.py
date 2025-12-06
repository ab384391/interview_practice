import numpy as np

def dropout(x, p=0.5, training=True):
    """
    Applies dropout regularization.
    
    Args:
        x: Input tensor of any shape
        p: Dropout probability (probability of zeroing an element)
        training: If True, apply dropout. If False, return input unchanged.
        
    Returns:
        output: Tensor with dropout applied (if training) or unchanged (if inference)
    """
    if not training:
        return x
    
    # Generate random mask
    mask = np.random.binomial(1, 1-p, size=x.shape)
    
    # Apply mask and scale by 1/(1-p) for inverted dropout
    # This ensures expected value remains the same
    output = x * mask / (1 - p)
    
    return output

"""
NOTES:
1. Inverted Dropout:
   - We scale by 1/(1-p) during training so that at inference we don't need to scale.
   - Alternative: Standard dropout scales at inference by (1-p).
   
2. Purpose:
   - Prevents co-adaptation of neurons.
   - Acts as an ensemble of many sub-networks.
   
3. Typical Values:
   - p=0.5 for hidden layers
   - p=0.2 for input layers
   - p=0.0 (no dropout) for output layers
"""
