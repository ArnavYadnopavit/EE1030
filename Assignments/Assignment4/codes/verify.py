import numpy as np
from ctypes import *
func=CDLL('./func.so')
A=[-3,-14]
B=[-3,-5]
AB=[]
AB.append(func.sub(A[0],B[0]))
AB.append(func.sub(A[1],B[1]))

AB_c = (c_int * len(AB))(*AB)
norm=func.vector_norm(AB_c,2)
print(norm)
