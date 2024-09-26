import numpy as np
import ctypes
func=ctypes.CDLL('/home/arnav/git/EE1030/Assignments/Assignment3/codes/func.so')
A=[-2,3,5]
B=[1,2,3]
C=[7,0,-1]

if func.sub(3*B[0],2*A[0])==C[0] and func.sub(3*B[1],2*A[1])==C[1] and func.sub(3*B[2],2*A[2])==C[2] :
    print("Rank 1 and thus A,B,C collinear")
else:
    print("A,B,C not collinear")
