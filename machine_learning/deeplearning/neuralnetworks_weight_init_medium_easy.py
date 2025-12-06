import numpy as np

def xavier_init(shape):
    """
    Xavier/Glorot initialization for weights.
    Variance = 2 / (fan_in + fan_out)
    
    Args:
        shape: Tuple (out_features, in_features)
        
    Returns:
        weights: Initialized weight matrix
    """
    fan_in = shape[1]
    fan_out = shape[0]
    
    # Xavier uniform: U[-limit, limit] where limit = sqrt(6 / (fan_in + fan_out))
    limit = np.sqrt(6.0 / (fan_in + fan_out))
    weights = np.random.uniform(-limit, limit, size=shape)
    
    return weights.astype(np.float32)

def he_init(shape):
    """
    He initialization for weights (for ReLU activations).
    Variance = 2 / fan_in
    
    Args:
        shape: Tuple (out_features, in_features)
        
    Returns:
        weights: Initialized weight matrix
    """
    fan_in = shape[1]
    
    # He normal: N(0, sqrt(2 / fan_in))
    std = np.sqrt(2.0 / fan_in)
    weights = np.random.randn(*shape) * std
    
    return weights.astype(np.float32)

"""
NOTES:
1. Xavier/Glorot Initialization:
   - Designed for sigmoid/tanh activations.
   - Keeps variance of activations and gradients roughly constant across layers.
   - Uniform variant: U[-sqrt(6/(fan_in+fan_out)), sqrt(6/(fan_in+fan_out))]
   - Normal variant: N(0, sqrt(2/(fan_in+fan_out)))
   
2. He Initialization:
   - Designed for ReLU activations.
   - Accounts for the fact that ReLU zeros out half the activations.
   - Variance is 2/fan_in instead of 2/(fan_in+fan_out).
   
3. Why Initialization Matters:
   - Too small: Activations shrink to zero in deep networks.
   - Too large: Activations explode or saturate.
   - Proper init helps gradient flow during backprop.
   
4. Modern Practices:
   - Use He init for ReLU/Leaky ReLU.
   - Use Xavier init for sigmoid/tanh.
   - Some use Xavier for all (works reasonably well).
"""
