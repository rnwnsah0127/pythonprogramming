import numpy as np

U = np.array([4,1,1])
V = np.array([2,1,0])

u1, u2, u3 = U
v1, v2, v3 = V

c1 = u2 * v3 - u3 * v2
c2 = -(u1 * v3 - u3 * v1)
c3 = u1 * v2 - u2 * v1

result = np.array([c1,c2,c3])

print("i 성분",c1)
print("j 성분",c2)
print("k 성분",c3)
print("U * V",result)

reference = np.cross(U,V)
print("Numpy 결과",reference)
print("결과 일치",np.allclose(result,reference))

print("U * (U X V):",np.dot(U, result))
print("V * (U X V):",np.dot(V, result))