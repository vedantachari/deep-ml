import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	try : 
		return np.multiply(np.array(matrix), scalar).tolist()
	except ValueError:
		return []