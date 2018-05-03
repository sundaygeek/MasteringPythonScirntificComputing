from sympy import *
u = Matrix([[1,2,3]]) # a row vector = 1x3 matrix
v = Matrix([[4],
[5],		# a col vector = 3x1 matrix
[6]])
v.T # use the transpose operation to
u[1] # 0-based indexing for entries
u.norm() # length of u
uhat = u/u.norm() # unit-length vec in same dir as u
uhat
uhat.norm()