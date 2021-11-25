import numpy as np
import random

# generate random list of "colors" 
colors = []
for _ in range(100):
    r = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)
    colors.append(np.array([r,g,b]))

# get actual average color
avg = np.array([0.0, 0.0, 0.0])
for color in colors:
    avg += color
avg /= len(colors)

# get incremental coverage
running_avg = np.array([0.0, 0.0, 0.0])
for i, color in enumerate(colors):
    running_avg = running_avg + (color - running_avg) / (i+1)
    print(running_avg)

print(f'avg: {avg}')
print(f'running_avg: {running_avg}')
