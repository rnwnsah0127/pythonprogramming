import numpy as np

U = np.array([1,2], dtype = float)
V = np.array([6,-3],dtype = float)

dot_product = np.dot(U,V)
norm_U = np.linalg.norm(U)
norm_V = np.linalg.norm(V)

print(f"내적 = {dot_product:.6f}")

if norm_U == 0 or norm_V == 0:
    print("직교합니다.")
    print("영벡터가 포함되어 각도는 정의되지 않습니다.")
else:
    cos_theta = dot_product / (norm_U * norm_V)
    cos_theta = np.clip(cos_theta,-1.0,1.0)

    theta_deg = np.degrees(np.arccos(cos_theta))
    is_orthogonal = np.isclose(
        cos_theta,0.0,atol=1e-10,rtol=0.0
    )

    print(f"cos(theta) = {cos_theta:.6f}")
    print(f"각도 = {theta_deg:.6f}도")
    print("직교합니다." if is_orthogonal else "직교하지 않습니다.")