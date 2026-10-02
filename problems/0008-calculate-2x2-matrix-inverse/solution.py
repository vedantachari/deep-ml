import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    a = np.array(matrix)
    try:
        return np.linalg.inv(a).tolist()
    except np.linalg.LinAlgError:
        return None