def isVectorInNullSpaceOfMatrix(matrix, vector):
	rows = len(matrix)
	cols = len(matrix[0])

	if(len(vector) != cols):
		return False

	for row in range(rows):
		sum = 0
		for col in range(cols)):
			num += matrix[row][col] * vector[col]
		if sum != 0:
			return False
	
	return True
