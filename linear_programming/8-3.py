import numpy as np

U = np.array([1,2,3])
V = np.array([-4,3,5])

# 각 벡터의 길이
norm_U = np.linalg.norm(U)
norm_V = np.linalg.norm(V)

# 두 벡터 사이의 거리
difference = V - U
distance = np.linalg.norm(difference)

print(f"U의 길이 = {norm_U:.6f}")
print(f"V의 길이 = {norm_V:.6f}")
print("V - U = ",difference)
print("각 성분의 제곱 = ", difference ** 2)
print(f"두 벡터의 거리 = {distance:.6f}")