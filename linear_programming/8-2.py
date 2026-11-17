import numpy as np

U = np.array([1,2,-4])
V = np.array([2,-3,5])
W = np.array([4,2,-3])

print("U * V =",np.dot(U,V))
print("U * W =",np.dot(U,W))
print("V * W =",np.dot(V,W))