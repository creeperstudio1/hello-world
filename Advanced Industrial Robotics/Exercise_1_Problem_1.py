import numpy as np
from scipy.spatial.transform import Rotation

np.set_printoptions(suppress=True)
#Define the camera parameters
k=1500
u0=640
v0=512

# Define K-Matrix
K = np.array([[k, 0, u0],
              [0, k, v0],
              [0, 0, 1]])

#-------------------------------------------#
#Problem 1
print("Solution for Problem 1\n")

#Part A
print("Solution for Part A\n")

#Define the 3D points
r1=np.array([[0.1], [0.2], [0.5]])
r2=np.array([[1.0], [2.0], [5.0]])
r3=np.array([[0.1], [0.2], [1.0]])
r=np.hstack((r1,r2,r3))

#Find s1,s2,s3
s=np.zeros((3,3))
for i in range(3):
    s[:,[i]]=1/r[2,i] * r[:,[i]]
    print(f"s{i+1} = \n{s[:,[i]]}")

#Find p1,p2,p3
p=np.zeros((3,3))
for i in range(3):
    p[:,[i]]=K @ s[:,[i]]
    print(f"p{i+1} = \n{p[:,[i]]}")

#-------------------------------------------#
    
#Part B
print("Solution for Part B\n")

#Define the pixel points
pa=np.array([[0], [0], [1]])
pb=np.array([[740], [612], [1]])   
pc=np.array([[1280], [1024], [1]])
p=np.hstack((pa,pb,pc))

#Inverse K matrix
K_inv=np.linalg.inv(K)

#Find sa,sb,sc
abc=np.array(['a','b','c'])
s=np.zeros((3,3))
for i in range(3):
    s[:,[i]]=K_inv @ p[:,[i]]
    print(f"s{abc[i]} = \n{s[:,[i]]}")

#-------------------------------------------#
    
#Part C
print("Solution for Part C\n")

#Define given matrices and vectors
theta=np.pi/2
Rc_o=Rotation.from_euler('x', theta).as_matrix()
tc_o=np.array([[0],[0],[4]])
Tc_o=p=np.vstack((np.hstack((Rc_o,tc_o)),np.array([0,0,0,1])))
ro_p=np.array([[1],[1],[0],[1]])

#Find C to safisfy z*s=C*ro_p in this case C=[Rc_o tc_o] E R3x4
C=np.hstack((Rc_o,tc_o))
print(f"C= \n{C}\n")

#Calculate rc_p
rc_p=Tc_o @ ro_p
print(f"rc_p= \n{rc_p}\n")

#Find z from rc_p
z=rc_p[2,0]
print(f"z= \n{z}\n")

#Find s
s=1/z * rc_p[range(3),0]
print(f"s= \n{s}\n")

#Find p
p=K @ s
print(f"p= \n{p}\n")

test=C @ ro_p
print(test)