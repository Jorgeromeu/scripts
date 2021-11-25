from collections import Counter
import matplotlib.pyplot as plt

fd = open('/home/jorge/.zshhistory', 'r', errors='replace')

cmds = []
for line in fd.readlines():
    args = line.split(' ')
    cmds.append(args[0])

# count 
count = Counter(cmds)

# sort commands by frequency
count = sorted(count.items(), key=lambda item:item[1], reverse=True)
count = dict(count)

count = dict(filter(lambda item: item[1] > 100, count.items()))

plt.bar(count.keys(), count.values())
plt.show()