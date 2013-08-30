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

primes = getAllPrimes(999,10000)
#primes = getAllPrimes(1000000)
sets = {}
sprime = []
for prime in primes:
  del sprime[:]
  s = str(prime)
  for i in s:
    sprime.append(i)
  sprime.sort()
  try:
    sets[str(sprime)].append(prime)
  except:
    sets[str(sprime)] = [prime]
   

for key in sets.keys():
  if len(sets[key]) < 3:
    sets.pop(key)
  
indices = []
for key in sets.keys():
  del indices[:]
  n = 0
  ray = sets[key]
  #print ray
  diffSet = getDifferenceSet(ray)
  diffSet.sort()
  for i in range(0,len(diffSet)-1):
    if diffSet[i] == diffSet[i+1]:
      n = n+1
      indices.append(i)
  for el in ray:
    for index in indices:
      if el + diffSet[index] in ray and el+diffSet[index]*2 in ray:
        delta = diffSet[index]
        print str(el)+str(el+delta) + str(el+2*delta)



