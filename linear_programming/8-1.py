import numpy as np

U = np.array([[2],[-5],[-1]])
V = np.array([[3],[2],[-3]])

U_dot_V = (U.T @ V).item()
V_dot_U = (V.T @ U).item()

print("U * V =", U_dot_V)
print("V * U =", V_dot_U)
print("교환법칙 확인 : ", U_dot_V == V_dot_U)