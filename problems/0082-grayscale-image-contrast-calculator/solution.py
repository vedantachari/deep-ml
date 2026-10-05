import numpy as np

def calculate_contrast(img) -> int:
	img = np.array(img)
	min_pix = np.min(img)
	max_pix = np.max(img)

	return max_pix - min_pix