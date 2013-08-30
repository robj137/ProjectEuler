#!/usr/bin/python

f = open('prime.txt')
#f = open('Primes.txt')

primes = []
for line in f:
  for y in (line.rstrip('\n').split()):
    if int(y) < 100 and int(y) > 1:
      primes.append(int(y))
f.close()

def getPrimeFactorization(N, primes):
  n = N
  factors = []
  while n > 1:
    p = primes[:]
    for i in primes:
      a,b = divmod(n, i)
      if b == 0:
        factors.append(i)
        n = a
        break
  return factors

def factorSmart(a,b):
  afactors = getPrimeFactorization(a,primes)
  bfactors = getPrimeFactorization(b,primes)
  aS = afactors[:]
  bS = bfactors[:]
  for a in aS:
    if a in bfactors:
      afactors.pop(afactors.index(a))
      bfactors.pop(bfactors.index(a))
  aNew = 1
  bNew = 1
  for i in afactors:
    aNew *= i
  for i in bfactors:
    bNew *= i
  return aNew, bNew

def factorDumb(a,b):
  aList = [int(i) for i in str(a)]
  bList = [int(i) for i in str(b)]
  aS = aList[:]
  bS = bList[:]
  for a in aS:
    if a in bList:
      aList.pop(aList.index(a))
      bList.pop(bList.index(a))
  if len(aList) == 0 or len(bList) == 0:
    return a, b
  aRed = int(''.join(str(n) for n in aList))
  bRed = int(''.join(str(n) for n in bList))
  return aRed, bRed

ups = 1
downs = 1
for up in range(9,99):
  for down in range(up+1,99):
    dumbUp, dumbDown = factorDumb(up,down)
    smartUp, smartDown = factorSmart(up,down)
    dsUp, dsDown = factorSmart(dumbUp, dumbDown)
    if (dsUp, dsDown) == (smartUp, smartDown):
      if smartUp != up and dumbUp != up and up%10 != 0:
        ups *= up
        downs *= down


newUp, newDown = factorSmart(ups, downs)
print newUp, newDown
