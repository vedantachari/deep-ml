import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)

    data = (data - mean) / std

    cov =  np.cov(data, rowvar=False)
    eig_val, eig_vec = np.linalg.eigh(cov)
    ind = np.argsort(eig_val)[::-1]
    eig_val = eig_val[ind]
    eig_vec = eig_vec[:,ind]
    com = eig_vec[:, :k]
    
    return com[::-1]
