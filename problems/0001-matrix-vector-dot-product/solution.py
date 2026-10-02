import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	li = []
	a = np.array(a)
	b = np.array(b)
	try : 
		return a @ b
	except ValueError:
		return -1