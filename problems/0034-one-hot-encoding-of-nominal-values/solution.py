import numpy as np

def to_categorical(x, n_col=None):
    x = np.array(x, dtype=int)

    if n_col is None:
        n_col = np.max(x) + 1

    c = np.zeros((len(x), n_col))

    for i, v in enumerate(x):
        c[i, v] = 1

    return c