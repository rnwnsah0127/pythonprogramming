import numpy as np
np.set_printoptions(suppress=True,precision=2)

A = np.array([
    [3,2,1],
    [1,1,2],
    [2,1,1]
],dtype=float)

b = np.array([
    [5],
    [1],
    [2]
],dtype=float)

print("계수 행렬 A")
print(A)
print("\n상수 벡터 b")
print(b)

det_A = np.linalg.det(A)
print("\n 행렬식 det(A)")
print(round(det_A, 10))

if np.isclose(det_A,0):
    print("\ndet(A) = 0이므로 역행렬이 존재하지 않습니다.")
else:
    A_inverse = np.linalg.inv(A)

    print("\nA의 역행렬")
    print(A_inverse)

    X = A_inverse @ b
    print("\n선형시스템의 해")
    print(X)

    x,y,z = X.flatten()
    print(f"\nx = {x:.0f}")
    print(f"y = {y:.0f}")
    print(f"z = {z:.0f}")

    print("\n검산 결과 A @ X")
    print(A @ X)