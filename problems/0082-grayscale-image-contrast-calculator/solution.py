import numpy as np

def calculate_contrast(img) -> int:
	"""
	Calculate the contrast of a grayscale image.
	Args:
		img (numpy.ndarray): 2D array representing a grayscale image with pixel values between 0 and 255.
	"""
	img = np.array(img)
	min_pix = np.min(img)
	max_pix = np.max(img)

	return max_pix - min_pix