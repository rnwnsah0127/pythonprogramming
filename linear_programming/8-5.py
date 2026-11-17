import numpy as np

U = np.array([1,1,0],dtype = float)
V = np.array([0,1,1],dtype=float)

dot_product = np.dot(U,V)
norm_U = np.linalg.norm(U)
norm_V = np.linalg.norm(V)

# 두 벡터 사이의 거리
distance = np.linalg.norm(U-V)

print(f"내적 = {dot_product:.6f}")
print(f"거리 = {distance:.6f}")

# 두 벡터 사이의 각도
if norm_U == 0 or norm_V == 0:
    print("영벡터가 포함되어 각도를 정의할 수 없습니다.")
else:
    cos_theta = dot_product/ (norm_U * norm_V)
    cos_theta = np.clip(cos_theta,-1.0,1.0)

    theta_rad = np.arccos(cos_theta)
    theta_deg = np.degrees(theta_rad)

    print(f"cos(theta) = {cos_theta:.6f}")
    print(f"각도 = {theta_deg:.6f}도")