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

def addMembers(members, nonos):
  for i in members:
    nonos[i] = 1

N = int(sys.argv[1])
max = 2000
lengths = []
i=0
members = []
nonos = []
for i in xrange(int(1e6)):
  nonos.append(0)
nonos[0] = 1
nonos[1] = 1
for a in range(100,N):
  nonos[a] = 1
  del members[:]
  A = a
  i = 0
  while i < max:
    i = i+1
    A = getsumDivisors(A)
    if A == a:
      print i, a, members
      lengths.append((i,a))
      addMembers(members, nonos)
      break
    if A > 1e6-1:
      addMembers(members, nonos)
      break
    if nonos[A] == 1:
      addMembers(members, nonos)
      break
    if A in members:
      break
    members.append(A)
    if i == max-1:
      print 'crap'
    
print lengths
print sum(nonos)
