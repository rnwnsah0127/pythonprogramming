import numpy as np

np.set_printoptions(precision=4, suppress=True)

# 실습 7-1
# MATLAB: A=[2, 3; 3, -6]; poly(A); eig(A)

A = np.array([[2, 3],
              [3, -6]])
print("poly(A) =", np.poly(A))              # 특성다항식 계수 -> [1, 4, -21]
print("eig(A) =")
print(np.sort(np.real_if_close(np.linalg.eigvals(A))).reshape(-1, 1))  # 고윳값 -> -7, 3

# 실습 7-2
# MATLAB: A=[3, 2; 3, -2]; [X, lamda]=eig(A)

A = np.array([[3, 2],
              [3, -2]])
w, X = np.linalg.eig(A)
w, X = np.real_if_close(w), np.real_if_close(X)
lamda = np.diag(w)
print("X =")
print(X)          # 열이 고유벡터
print("lamda =")
print(lamda)      # 대각선이 고윳값

# 실습 7-3
# MATLAB: A=[3, -1, -1; -12, 0, 5; 4, -2, -1]; [X,lamda]= eig(A)

A = np.array([
    [3,-1,-1],
    [-12, 0, 5],
    [4,-2,-1]
])
w , X = np.linalg.eig(A)
w , X = np.real_if_close(w), np.real_if_close(X)
lamda = np.diag(w)
print("X = ",X)
print("lamda =",lamda)
# 실습 7-4
# MATLAB: A=[0, 0, 0; 0, 2, 5; 0, 0, -1]; eig(A)

A = np.array([[0, 0, 0],
              [0, 2, 5],
              [0, 0, -1]])
print("eig(A) =")
print(np.real_if_close(np.linalg.eigvals(A)).reshape(-1, 1))

# 실습 7-4
# MATLAB: A=[4, 0, 0; 0, 0, 0; 1, 0, -3]; eig(A)

A = np.array([[4, 0, 0],
              [0, 0, 0],
              [1, 0, -3]])
print("eig(A) =")
print(np.real_if_close(np.linalg.eigvals(A)).reshape(-1, 1))