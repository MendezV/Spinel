import numpy as np
from numpy import linalg as la
'''
C=np.array([1.75390 ,-0.51310, -0.00060])
Pt=np.array([-0.33130,  0.01060 , 0.00000])
v=C-Pt
v=v/np.sqrt(np.sum(v**2))
'''
###script that generates the rotation matrix that aligns a to b (a moves to align with b)
a=np.mat([1,1,1])
b=np.mat([0,0,1])
a=a/np.sqrt(np.dot(a,a.T))
c=np.dot(a,b.T)
v=np.cross(a,b)[0]
s=np.sqrt(np.dot(v,v.T))
y = np.mat([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])

Rot=np.mat(np.diag([1,1,1]))+y+np.dot(y,y)*(((1-c)/s**2)[0,0])

print(Rot, la.det(Rot))
print(np.dot(Rot,np.mat([1,0,0]).T), np.dot(Rot,np.mat([0,1,0]).T))
print(la.inv(Rot))
