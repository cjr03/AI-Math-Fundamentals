import numpy as np

def areVectorsOrthogonal(vectors):
    n = len(vectors)
    for i in range(n):
        for j in range(i+1, n):
            if np.dot(vectors[i], vectors[j]) != 0:
                return False
    return True
