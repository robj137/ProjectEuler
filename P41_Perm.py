#!/usr/bin/python
import sys
from itertools import permutations

f = open('perms9pan.txt', 'w')
number = str(sys.argv[1])
for a in permutations(number):
  f.write((''.join(str(n) for n in a))+'\n')

f.close()
