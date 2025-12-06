import numpy as np

def conv2d_filter(image, kernel):
    """
    Applies a 2D convolution filter to an image.
    
    Args:
        image: Input image of shape (H, W)
        kernel: Convolution kernel of shape (K_H, K_W)
        
    Returns:
        output: Convolved output of shape (H - K_H + 1, W - K_W + 1)
    """
    H, W = image.shape
    K_H, K_W = kernel.shape
    
    # Output dimensions (valid padding)
    out_H = H - K_H + 1
    out_W = W - K_W + 1
    
    output = np.zeros((out_H, out_W), dtype=image.dtype)
    
    # Slide kernel over image
    for i in range(out_H):
        for j in range(out_W):
            # Extract patch
            patch = image[i:i+K_H, j:j+K_W]
            # Element-wise multiply and sum
            output[i, j] = np.sum(patch * kernel)
    
    return output

"""
NOTES:
1. Padding:
   - This implementation uses "valid" padding (no padding).
   - For "same" padding, we would pad the input to maintain output size.
   
2. Stride:
   - This implementation uses stride=1.
   - For stride > 1, we would increment i and j by the stride value.
   
3. Optimization:
   - For production, use im2col + matrix multiplication for better performance.
   - Libraries like NumPy/PyTorch use FFT-based convolution for large kernels.
   
4. Multi-channel:
   - For RGB images (H, W, C), we would need separate kernels per channel
     or use depthwise/separable convolutions.
"""
