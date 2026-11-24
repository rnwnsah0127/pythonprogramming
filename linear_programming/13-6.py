import numpy as np

U = np.array([2,-4])
V = np.array([4,2])

dot_uv = np.dot(U,V)
print("U * V = ",dot_uv)

if np.isclose(dot_uv, 0):
    print("두 벡터는 서로 직교합니다.")
else:
    print("두 벡터는 서로 직교하지 않습니다.")

norm_product = np.linalg.norm(U) * np.linalg.norm(V)

if norm_product > 0:
    cos_theta = dot_uv / norm_product
    theta = np.degrees(
        np.arccos(np.clip(cos_theta,-1,1))
    )
    print(f"두 벡터의 사이각 = {theta:.2f}도")
else:
    print("0벡터가 포함되면 사이각이 정의되지 않습니다.")