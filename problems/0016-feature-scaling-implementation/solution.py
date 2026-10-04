import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	mean_data = np.mean(data, axis=0, keepdims=True)
	std_data = np.std(data, axis=0, keepdims=True)

	standardized_data = ((data - mean_data) / std_data)
	
	data_min = np.min(data, axis=0, keepdims=True)
	data_max = np.max(data, axis=0, keepdims=True)

	normalized_data = (data - data_min) / (data_max - data_min)
	return np.array(standardized_data), np.array(normalized_data)