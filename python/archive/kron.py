import numpy as np
import sympy as sym

left_x, right_x = (-1.5, 1.5)
left_y, right_y = (-1.5, 1.5)

nx, ny = 4, 4

hx, hy = sym.symbols('hx hy')

dx = (right_x - left_x) / nx
dy = (right_y - left_y) / ny

def Dx_func(n):
    sqr = (1 / hx ** 2) * np.diag([1] * n) + np.diag([-1] * (n - 1), -1)
    return sqr[:, :n - 1]  # / hx

def Dy_func(n):
    sqr = (1 / hy ** 2) * np.diag([1] * n) + np.diag([-1] * (n - 1), -1)
    return sqr[:, :n - 1]  # / hy

Dx = Dx_func(nx)
Dy = Dy_func(ny)

Axx = np.matmul(np.transpose(Dx), Dx)
Ayy = np.matmul(np.transpose(Dy), Dy)

Ix = np.diag([1] * (nx - 1))
Iy = np.diag([1] * (ny - 1))

A = np.kron(Iy, Axx) + np.kron(Ayy, Ix)

A_evaled = np.vectorize(lambda e: e.subs({hx: 2.5, hy: 1.25}))(A)

A_simplify = np.vectorize(lambda e: sym.simplify(e))(A)

def texify(mx):
    tex = '\\begin{bmatrix}\n'

    mx_tex = np.vectorize(lambda e: sym.latex(e))(mx)

    for row in mx_tex:
        for e in row[:-1]:
            tex += str(e)
            tex += ' & '
        tex += str(row[-1])
        tex += '\\\\\n'

    tex += '\\end{bmatrix}'

    tex = tex.replace("hx", "h_x")
    tex = tex.replace("hy", "h_y")
    return tex

print(texify(A))


