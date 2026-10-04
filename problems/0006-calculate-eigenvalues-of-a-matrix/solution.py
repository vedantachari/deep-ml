import numpy as np
import math 
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	matrix = np.array(matrix)
	matrix_det = np.linalg.det(matrix)
	matrix_trace = np.trace(matrix) / 2
	eig1 = matrix_trace + math.sqrt(matrix_trace * matrix_trace - matrix_det)
	eig2 = matrix_trace - math.sqrt(matrix_trace * matrix_trace - matrix_det)
	eigenvalues = [eig1, eig2]
	return eigenvalues