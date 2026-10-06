import numpy as np

def flip_image(image, direction):
    """
    Flip an image horizontally or vertically.
    
    Args:
        image: 2D or 3D list/array representing a grayscale or RGB image
        direction: string, either 'horizontal' or 'vertical'
    
    Returns:
        Flipped image as a nested list, or -1 if input is invalid
    """
    image = np.array(image)
    if image is None or len(image) == 0: 
        return -1
    if image.ndim not in (2, 3): 
        return -1
    if direction == 'vertical':
        new_img = np.flip(image, axis = 0)
    elif direction == 'horizontal':
        new_img = np.flip(image, axis = 1)
    else:
        return -1

    return new_img.tolist()