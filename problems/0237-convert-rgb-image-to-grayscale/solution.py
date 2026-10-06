import numpy as np

def rgb_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminosity method.
    
    Args:
        image: RGB image as list or numpy array of shape (H, W, 3)
               with values in range [0, 255]
    
    Returns:
        Grayscale image as 2D list with integer values,
        or -1 if input is invalid
    """
    image = np.array(image)
    if image.ndim != 3 or image.shape[2] != 3:
        return -1

    if np.any(image < 0) or np.any(image > 255):
        return -1

        
    weights = [0.299, 0.587, 0.114]
    
    gray = np.round(np.dot(image, weights)).astype(np.uint8)
    
    return gray.tolist()
