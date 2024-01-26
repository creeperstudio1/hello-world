import numpy as np
X = np.array([[1, 0, 1], [0, 1, 1], [0, -1, 1], [-2, -1.5, 1], [-1, 0, 1],[-1, 1, 1], [2, 2, 1], [0.5, 0.8660, 1], [0.7071, 0.7071, 1]]).T
ind = np.array([[1, 3, 4], [1, 2, 3], [1, 4, 5],[2, 3, 4], [2, 4, 5], [3, 4, 5], [3, 4, 6]]).T
ind = ind - 1
npoint = X.shape[1]; ncomb = ind.shape[1] # .shape[i] is to know one of the dimensions of the matrix i will be 0 for rows and 1 for columns
X_inlier = np.zeros((npoint, ncomb))
C = np.zeros((4,ncomb))
N_inlier = np.zeros(ncomb)
maxinliers = 0; j_maxinliers = 0


print(N_inlier)