import numpy as np

A = np.array([-1,2,0])
B = np.array([2,1,3])
C = np.array([1,1,-1])

U = B - A
V = C - A

cross_product = np.cross(U,V)

parallelogram_area = np.linalg.norm(cross_product)

triangle_area = parallelogram_area / 2

print("U = ",U)
print("V = ",V)
print("U X V",cross_product)
print(f"평행사변형의 넓이 = {parallelogram_area:.6f}")
print(f"삼각형의 넓이 = {triangle_area:.6f}")