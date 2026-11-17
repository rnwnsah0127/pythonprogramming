import numpy as np

U = np.array([[2],[-5],[-1]])
V = np.array([[3],[2],[-3]])

# .T:전치 , @: 행렬곱, .item():숫자 하나 추출
U_dot_V = (U.T @ V).item()
V_dot_U = (V.T @ U).item()

print("U * V =", U_dot_V)  # -1
print("V * U =", V_dot_U)  # -1
print("교환법칙 확인 : ", U_dot_V == V_dot_U) # True