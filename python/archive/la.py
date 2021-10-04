import sympy as sym
from sympy.matrices import Matrix
from sympy.vector import Vector

# create symbols
eig1, eig2, eig3 = sym.symbols('λ1, λ2, λ3')

v11, v12, v13 = sym.symbols('v11 v12 v13')
v21, v22, v23 = sym.symbols('v21 v22 v22')
v31, v32, v33 = sym.symbols('v31 v32 v33')

f1, f2, f3 = sym.symbols('f1, f2, f3')

# create f vector
f = Matrix((f1, f2, f3))

# create v1, v2 and v3 column vectors
v1 = Vector(v11, v12, v13)
v2 = Vector(v21, v22, v23)
v3 = Vector(v31, v32, v33)

# V diagonal matrix
V = Matrix(((v11, v21, v31), (v12, v22, v32), (v13, v23, v33)))

# inverse of L
L_inv = Matrix(((1/eig1, 0, 0), (0, 1/eig2, 0), (0, 0, 1/eig3)))

# do matrix product
u = V*L_inv*V.transpose()*f

# pretty printing
sym.init_printing(True)
