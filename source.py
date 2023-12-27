#Trong đoạn code này, A là ma trận hệ số, B là vector bên phải, và A1 là ma trận nghịch đảo của A. 
#Nghiệm của hệ phương trình tuyến tính Ax = B được tính bằng cách nhân ma trận nghịch đảo của A với vector B.
import numpy as np
A = np.array([(1, 2), (3, 4)])
B = np.array([5, 6])
A1 = np.linalg.inv(A)  # tao ma tran nghich dao
print(A)
print(B)
print(A1)
X = np.dot(A1, B)
print('Nghiem cua he:', X)
