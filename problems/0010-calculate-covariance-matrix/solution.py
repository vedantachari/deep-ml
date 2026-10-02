import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	a = np.array(vectors)
	try:
		return np.cov(a).tolist()
	except : 
		return []