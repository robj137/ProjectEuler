#!/usr/bin/python

import sys

def areAmicable(a,b):
  # if amicable:
  A = sum(getDivisors(a))
  B = sum(getDivisors(b))
  if A == b and B == a:
    return 1
  else:
    return 0

def isAmicable(a):
  b = sum(getDivisors(a))
  A = sum(getDivisors(b))
  if(A == a and a != b):
    return 1
  else:
    return 0

def getDivisors(N):
  divisors = []
  for i in range(1,N/2+2):
    rat, rem = divmod(N, i)
    if rem == 0 and i < N:
      divisors.append(i)
  return divisors

def getsumDivisors(N):
  return sum(getDivisors(N))


N = int(sys.argv[1])
max = 20
lengths = []
i=0
members = []
nonos = []
for i in xrange(1000000):
  nonos.append(0)
nonos[0] = 1
nonos[1] = 1
for a in xrange(N):
  del members[:]
  A = a
  i = 0
  while i < max:
    if nonos[a] == 1:
      break
    i = i+1
    A = getsumDivisors(A)
    if A > 1e6-1:
      break
    if nonos[A]:
      break
    nonos[A] = 1
    if A in members:
      break
    members.append(A)
    if A == a:
      print i, a, members
      lengths.append((i,a))
      nonos[A] = 1
      break
    
    
print lengths
