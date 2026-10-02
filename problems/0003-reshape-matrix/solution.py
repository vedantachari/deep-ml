import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	a = np.array(a)
	try:
		reshaped_matrix = np.reshape(a, new_shape).tolist()
		return reshaped_matrix
	except ValueError:
		return []