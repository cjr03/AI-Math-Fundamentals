def NonZeroVectorsInColSpaceOfMatrix(matrix):
	rows = len(matrix)
	cols = len(matrix[0])
	vectors = []

	for col in range(cols):
		vector = []
		nonZero = False
		for row in range(rows):
			vector.append(matrix[row][col])
			if matrix[row][col] != 0:
				nonZero = True
		if nonZero:
			vectors.append(vector)

	return vectors
