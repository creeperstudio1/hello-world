import numpy as np
from scipy.spatial.transform import Rotation

np.set_printoptions(suppress=True)
#-------------------------------------------#

#Problem 2
print("Solution for Problem 2\n")

#Define object corners coordinates
ro_1=np.array([[0], [0], [0]])
ro_2=np.array([[1.0], [0], [0]])
ro_3=np.array([[1], [1], [0]])
ro_4=np.array([[0], [1], [0]])
r=np.vstack((np.hstack((ro_1,ro_2,ro_3,ro_4)),np.array([1,1,1,1])))
print(r)
#Define given matrices and vectors
theta=np.radians(120)
Rc_o=Rotation.from_euler('x', theta).as_matrix()
tc_o=np.array([[0],[0],[2]])
Tc_o=p=np.vstack((np.hstack((Rc_o,tc_o)),np.array([0,0,0,1])))

rc_p=np.zeros((4,4))
for i in range(4):
    rc_p[:,i]=Tc_o @ r[:,i]
    print(f"rc_{i+1} = \n{rc_p[:,[i]]}")

s=np.zeros((3,4))
for i in range(4):
    s[:,i]=1/rc_p[2,i] * rc_p[range(3),i]
    print(f"s_{i+1} = \n{s[:,[i]]}")
#-------------------------------------------#
    
