#!/usr/bin/python

from math import sqrt

inp = open('Primes.txt')
prime2 = []
prime3 = []
prime4 = []
for line in inp:
  prime = int(line.rstrip())
  if prime**2 < (50e6):
    prime2.append(prime**2)
    if prime**3 < (50e6):
      prime3.append(prime**3)
      if prime**4 < (50e6):
        prime4.append(prime**4)

l = []
for p2 in prime2:
  for p3 in prime3:
    for p4 in prime4:
      if p2+p3+p4 < 50e6:
        l.append(p2+p3+p4)

l.sort()
w = []

nLines = len(l)
print 'Found', nLines, 'originally'
for i in range(0, nLines-1):
  if l[i+1] != l[i]:
    w.append(l[i])
w.append(l[-1])
print 'Found', len(w), 'on first pass'
print len(w)

