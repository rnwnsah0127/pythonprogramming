import numpy as np

U = np.array([4,1,1])
V = np.array([2,1,0])
W = np.array([0,2,3])

cross_product = np.cross(U,V)
S = np.linalg.norm(cross_product)

unit_normal = cross_product / S
h = abs(np.dot(W, unit_normal))

V1 = S * h

V2 = abs(np.dot(cross_product, W))

A = np.vstack([U, V, W])
V3 = abs(np.linalg.det(A))

print("U x V = ",cross_product)
print(f"밑면 넓이 S = {S:.6f}")
print(f"수직 높이 h = {h:.6f}")
print(f"밑면 x 높이로 구한 체적 = {V1:.6f}")
print(f"삼중곱으로 구한 체적 = {V2:.6f}")
print(f"행렬식으로 구한 체적 = {V3:.6f}")