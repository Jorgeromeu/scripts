import plotly.express as px
import plotly.graph_objs as go
from itertools import product
import numpy as np

x = [-525.344, -516.252, -534.206, -525.344, -516.252, -534.206]
y = [310.238, 323.558, 322.912, 310.238, 323.55, 322.912]
z = [0, 0, 0, 300, 300, 300]

nodes = [[i,j,k] for (i,j,k) in zip(x,y,z)]

labels = [0, 1, 2, 3, 4, 5]

def to_pairs(vertices):
    return list(product(vertices, vertices))

def to_graphobj(vertices):
    
    pairs = to_pairs(vertices)

    x_lines = []
    y_lines = []
    z_lines = []

    for p in pairs:
        for i in range(2):
            x_lines.append(x[p[i]])
            y_lines.append(y[p[i]])
            z_lines.append(z[p[i]])
        x_lines.append(None)
        y_lines.append(None)
        z_lines.append(None)

    lines = go.Scatter3d(
        x=x_lines,
        y=y_lines,
        z=z_lines,
        mode='lines',
        name='lines',
    )

    return lines

t1=[0, 3, 4, 5]
t2=[0, 1, 4, 5]
t3=[1, 2, 5, 0]
tetras = [t1, t2, t3]

fig = px.scatter_3d(x=x, y=y, z=z, text=labels)

for tetra in tetras:
    fig.add_traces(to_graphobj(tetra))

# fig.show()

def tetra_volume(tetra):
    e1 = np.array(nodes[tetra[0]]) - np.array(nodes[tetra[3]])
    e2 = np.array(nodes[tetra[1]]) - np.array(nodes[tetra[3]])
    e3 = np.array(nodes[tetra[2]]) - np.array(nodes[tetra[3]])

    vol = np.linalg.norm(np.dot(e1, np.cross(e2, e3))) / 6
    print(vol)
    return vol

fig.show()
