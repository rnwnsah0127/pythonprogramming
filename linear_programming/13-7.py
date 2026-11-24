import numpy as np

U = np.array([2,-5,-1])
V = np.array([3,2,-3])

products = U * V
dot_manual = np.sum(products)

dot_uv = np.dot(U,V)
dot_vu = np.dot(V,U)

U_col = U.reshape(3,1)
V_col = V.reshape(3,1)

dot_matrix = (U_col.T @ V_col).item()

print("성분별 곱 = ",products)
print("성분별 곱의 합 = ",dot_manual)
print("U * V = ",dot_uv)
print("V * U = ",dot_vu)
print("U^T V = ",dot_matrix)
print("교환법칙 확인: ",bool(dot_uv == dot_vu))