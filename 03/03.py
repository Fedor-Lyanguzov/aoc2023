

inp = open('input.txt').read().strip().split('\n')

chars = [(i, j, c) for i, line in enumerate(inp) for j, c in enumerate(line) if c!='.' and not '0'<=c<='9']

nums = []
for i, line in enumerate(inp):
    line = '.'+line+'.'
    for j, (l, r) in enumerate(zip(line, line[1:])):
        if not l.isdigit() and r.isdigit():
            s = j-1
        if l.isdigit() and not r.isdigit():
            nums.append((i, s+1, j-1-s, int(line[s+2:j+1])))

places = {}
for n, (i, j, l, _) in enumerate(nums):
    for k in range(j, j+l):
        places[(i, k)] = n
        
sel = set()
neigh = {(di, dj) for di in range(-1, 2) for dj in range(-1, 2)} - {(0,0)}
for i, j, _ in chars:
    for di, dj in neigh:
        if (i+di, j+dj) in places:
            sel.add(places[(i+di, j+dj)])

print(sum(nums[i][3] for i in sel))

from math import prod
s = 0
for i, j, _ in filter(lambda x: x[2]=='*', chars):
    sel = set()
    for di, dj in neigh:
        if (i+di, j+dj) in places:
            sel.add(places[(i+di, j+dj)])
    if len(sel)==2:
        s += prod(nums[i][3] for i in sel)
print(s)
