import math
import numpy as np
def softmax(scores: list[float]) -> list[float]:
    e_x = np.exp(scores - np.max(scores))
    return e_x / np.sum(e_x)