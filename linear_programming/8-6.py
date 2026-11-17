import numpy as np

U = np.array([1,-1,0],dtype = float)
V = np.array([2,-1,2],dtype=float)

dot_product = np.dot(U,V)
norm_U = np.linalg.norm(U)
norm_V = np.linalg.norm(V)

distance = np.linalg.norm(U-V)

print(f"내적 = {dot_product:.6f}")
print(f"거리 = {distance:.6f}")

if norm_U == 0 or norm_V == 0:
    raise ValueError("영벡터가 포함되면 각도를 정의할 수 없습니다.")

cos_theta = dot_product/ (norm_U * norm_V)
cos_theta = np.clip(cos_theta,-1.0,1.0)

theta_rad = np.arccos(cos_theta)
theta_deg = np.degrees(theta_rad)

print(f"내적 = {dot_product:.6f}")
print(f"U의 길이 = {norm_U:.6f}")
print(f"V의 길이 = {norm_V:.6f}")
print(f"cos(theta) = {cos_theta:.6f}")
print(f"각도(라디안) = {theta_rad:.6f}")
print(f"각도(도) = {theta_deg:.6f}도")