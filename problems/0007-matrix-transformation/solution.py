import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A = np.array(A)
	T = np.array(T)
	S = np.array(S)

	if (np.linalg.det(T) != 0 and np.linalg.det(S) != 0):
		T_inverse = np.linalg.inv(T)
		transformed_matrix = T_inverse @ A @ S
		return transformed_matrix.tolist()
	else:
		return -1
