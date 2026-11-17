import numpy as np

U = np.array([2,-5,-1])
V = np.array([-7,-4,6])

dot_product = np.dot(U,V)

squared_norm_U = np.dot(U, U)

difference = U - V
squared_distance = np.dot(difference,difference)

print("U * V =",dot_product)
print("||U|| ** 2 = ",squared_norm_U)
print("||U-V|| ** 2 = ",squared_distance)