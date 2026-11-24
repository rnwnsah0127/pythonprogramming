import numpy as np

U= np.array([3,1,0])
V= np.array([1,3,2])

cross_product = np.cross(U,V)

squared_length = np.dot(cross_product,cross_product)
area = np.linalg.norm(cross_product)

print("U X V",cross_product)
print(f"넓이의 제곱 = {squared_length}")
print(f"평행사변형의 넓이 = {area:.6f}")