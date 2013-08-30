#!/usr/bin/python



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


amicables = []
for i in range(1, 10010):
  if(isAmicable(i)):
    print i, sum(getDivisors(i)), getDivisors(i)
    amicables.append(i)

print amicables
print sum(amicables)
