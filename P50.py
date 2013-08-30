#!/usr/bin/python


def getAllPrimes(min = 0, max = 1e10):
  f = open('prime.txt')
  #f = open('Primes.txt')
  primes = []
  for line in f:
    for y in (line.rstrip('\n').split()):
      if int(y) < max and int(y) > min:
        primes.append(int(y))
  f.close()
  return primes

def IsPrime(N, primes):
  if N in primes:
    return 1
  else:
    return 0

def iterate(sN):
  return sN[1:] + sN[0]

def getDifferenceSet(l):
  aList = l[:]
  diffSet = []
  length = len(aList)
  while len(aList)>0:
    el = aList.pop()
    redList = aList[:]
    while(len(redList)):
      diffSet.append(int(el) - int(redList.pop()))
  return diffSet

primes = getAllPrimes(0,1000000)

n = 0
cmax = 0
pmax = 0
primes.insert(0,0)
while len(primes) > 5:
  print cmax, pmax
  c = 0
  primes.pop(0)
  n = 0
  for i in primes:
    c += 1
    n += i
    if n > 1000000:
      break
    if n in primes:
      if c > cmax:
        cmax = c
        pmax = n

print cmax, pmax
