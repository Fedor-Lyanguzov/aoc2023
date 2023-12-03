

inp = open('input.txt').read().strip().split('\n')

def f(line):
    i, rounds = line.split(': ')
    i = int(i[5:])
    rounds = [[(int(y[0]), y[1]) for x in r.split(', ') if (y:=x.split(' '))] for r in rounds.split('; ')]
    return i, rounds
req = {'red': 12, 'green': 13, 'blue': 14}

print(sum(i for i, rounds in map(f, inp) if all(a<=req[b] for r in rounds for a, b in r)))

from functools import reduce
from math import prod

def cubes_power(d):
    return prod(d.values())

def max_dict(a, b):
    return {k: max(a.get(k,0), b.get(k,0)) for k in a.keys() | b.keys()}

print(sum(cubes_power(
    reduce(max_dict, map(lambda x: dict((b, a) for a, b in x), rounds))
    ) for _, rounds in map(f, inp)))
