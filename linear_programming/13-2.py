import numpy as np

U = np.array([3,-1,2])
V = np.array([1,-2,4])

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

print("Numpy 결과",np.cross(U,V))

print("U * (U X V):",np.dot(U, result))
print("V * (U X V):",np.dot(V, result))