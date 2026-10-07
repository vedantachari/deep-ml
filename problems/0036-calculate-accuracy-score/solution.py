import numpy as np

def accuracy_score(y_true, y_pred):
	list_len = len(y_true)
	k = 0
	for i in range(list_len):
		if (y_pred[i] == y_true[i]):
			k += 1
	return k/list_len