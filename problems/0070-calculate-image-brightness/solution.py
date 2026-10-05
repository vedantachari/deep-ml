
def calculate_brightness(img):
	len_mat = 0
	sum_mat = 0
	
	for i in img:
		r_len = len(img[0])
		if (r_len != len(i) or len(img) != r_len):
			return -1
		else:
			for j in i:
				len_mat += 1
				sum_mat += j
	if img == []:
		return -1

	return sum_mat/len_mat

