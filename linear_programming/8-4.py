import numpy as np

U = np.array([2,-5,-1])
V = np.array([-7,-4,6])

# (1) 내적 
dot_product = np.dot(U,V)

# (2) 길이의 제곱
squared_norm_U = np.dot(U, U)

# (3) 거리의 제곱
difference = U - V
squared_distance = np.dot(difference,difference)

print("U * V =",dot_product)
print("||U|| ** 2 = ",squared_norm_U)
print("||U-V|| ** 2 = ",squared_distance)