import numpy as np

def conv2d_layer(x, W, b, stride=1, padding=0):
    """
    Implements a full 2D convolutional layer with multiple input/output channels.
    
    Args:
        x: Input, shape (batch_size, in_channels, height, width)
        W: Weights, shape (out_channels, in_channels, kernel_height, kernel_width)
        b: Biases, shape (out_channels,)
        stride: Stride for convolution
        padding: Padding to add to input
        
    Returns:
        out: Output, shape (batch_size, out_channels, out_height, out_width)
    """
    batch_size, in_channels, H, W_in = x.shape
    out_channels, _, K_H, K_W = W.shape
    
    # Add padding
    if padding > 0:
        x = np.pad(x, ((0, 0), (0, 0), (padding, padding), (padding, padding)), mode='constant')
        H += 2 * padding
        W_in += 2 * padding
    
    # Calculate output dimensions
    out_H = (H - K_H) // stride + 1
    out_W = (W_in - K_W) // stride + 1
    
    # Initialize output
    out = np.zeros((batch_size, out_channels, out_H, out_W))
    
    # Perform convolution
    for n in range(batch_size):  # For each sample in batch
        for c_out in range(out_channels):  # For each output channel
            for i in range(out_H):  # For each output height position
                for j in range(out_W):  # For each output width position
                    # Calculate input region
                    h_start = i * stride
                    w_start = j * stride
                    
                    # Extract patch from all input channels
                    patch = x[n, :, h_start:h_start+K_H, w_start:w_start+K_W]
                    # patch shape: (in_channels, K_H, K_W)
                    
                    # Convolve with kernel for this output channel
                    kernel = W[c_out]  # shape: (in_channels, K_H, K_W)
                    
                    # Element-wise multiply and sum over all dimensions
                    out[n, c_out, i, j] = np.sum(patch * kernel) + b[c_out]
    
    return out

"""
NOTES:
1. Full Convolutional Layer:
   - Multiple input channels (e.g., RGB has 3)
   - Multiple output channels (number of filters)
   - Each output channel has one kernel per input channel
   
2. Weight Dimensions:
   - W: (out_channels, in_channels, kernel_h, kernel_w)
   - Total params: out_channels * in_channels * kernel_h * kernel_w + out_channels
   
3. Padding:
   - 'valid': No padding (output smaller than input)
   - 'same': Padding such that output size = input size (when stride=1)
   - Padding = (kernel_size - 1) / 2 for 'same' with stride=1
   
4. Optimization:
   - This nested loop implementation is slow
   - Production uses im2col + matrix multiplication
   - Or FFT-based convolution for large kernels
   
5. Typical Values:
   - Kernel size: 3x3 or 5x5
   - Stride: 1 or 2
   - Padding: 1 for 3x3, 2 for 5x5 (to maintain size)
"""
