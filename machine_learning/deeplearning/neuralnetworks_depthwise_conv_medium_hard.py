import numpy as np

def depthwise_separable_conv(x, W_depthwise, W_pointwise, b_depthwise, b_pointwise, stride=1, padding=0):
    """
    Implements depthwise separable convolution.
    Consists of: Depthwise Conv -> Pointwise Conv (1x1)
    
    Args:
        x: Input, shape (batch_size, in_channels, height, width)
        W_depthwise: Depthwise weights, shape (in_channels, 1, kernel_h, kernel_w)
        W_pointwise: Pointwise weights, shape (out_channels, in_channels, 1, 1)
        b_depthwise: Depthwise biases, shape (in_channels,)
        b_pointwise: Pointwise biases, shape (out_channels,)
        stride: Stride for depthwise convolution
        padding: Padding for depthwise convolution
        
    Returns:
        out: Output, shape (batch_size, out_channels, out_height, out_width)
    """
    batch_size, in_channels, H, W_in = x.shape
    _, _, K_H, K_W = W_depthwise.shape
    out_channels = W_pointwise.shape[0]
    
    # ========== DEPTHWISE CONVOLUTION ==========
    # Apply one filter per input channel (no mixing across channels)
    
    # Add padding
    if padding > 0:
        x_padded = np.pad(x, ((0, 0), (0, 0), (padding, padding), (padding, padding)), mode='constant')
    else:
        x_padded = x
    
    H_padded, W_padded = x_padded.shape[2], x_padded.shape[3]
    
    # Calculate output dimensions
    out_H = (H_padded - K_H) // stride + 1
    out_W = (W_padded - K_W) // stride + 1
    
    # Depthwise output
    depthwise_out = np.zeros((batch_size, in_channels, out_H, out_W))
    
    for n in range(batch_size):
        for c in range(in_channels):
            for i in range(out_H):
                for j in range(out_W):
                    h_start = i * stride
                    w_start = j * stride
                    
                    # Extract patch from single channel
                    patch = x_padded[n, c, h_start:h_start+K_H, w_start:w_start+K_W]
                    
                    # Apply filter for this channel only
                    kernel = W_depthwise[c, 0]  # shape: (K_H, K_W)
                    
                    depthwise_out[n, c, i, j] = np.sum(patch * kernel) + b_depthwise[c]
    
    # ========== POINTWISE CONVOLUTION (1x1) ==========
    # Mix channels using 1x1 convolution
    
    pointwise_out = np.zeros((batch_size, out_channels, out_H, out_W))
    
    for n in range(batch_size):
        for c_out in range(out_channels):
            for i in range(out_H):
                for j in range(out_W):
                    # 1x1 convolution: just a weighted sum across channels
                    value = 0
                    for c_in in range(in_channels):
                        value += depthwise_out[n, c_in, i, j] * W_pointwise[c_out, c_in, 0, 0]
                    pointwise_out[n, c_out, i, j] = value + b_pointwise[c_out]
    
    return pointwise_out

"""
NOTES:
1. Depthwise Separable Convolution:
   - Factorizes standard convolution into two steps
   - Step 1 (Depthwise): Apply spatial filter to each channel independently
   - Step 2 (Pointwise): Mix channels with 1x1 convolution
   
2. Computational Savings:
   - Standard conv: K*K*C_in*C_out*H*W operations
   - Depthwise separable: K*K*C_in*H*W + C_in*C_out*H*W operations
   - Reduction factor: ~1/C_out + 1/(K*K)
   - For K=3, C_out=256: ~8-9x fewer operations
   
3. Parameter Reduction:
   - Standard: K*K*C_in*C_out parameters
   - Depthwise separable: K*K*C_in + C_in*C_out parameters
   - Significant savings for large C_out
   
4. Use Cases:
   - MobileNets: Designed for mobile/embedded devices
   - Efficient neural networks where speed/size matters
   - Often achieves similar accuracy with much less computation
   
5. Trade-offs:
   - Slightly less expressive than standard convolution
   - May need more layers to achieve same capacity
   - But overall efficiency gain is usually worth it
"""
