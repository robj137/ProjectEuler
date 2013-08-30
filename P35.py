#!/usr/bin/python


def getAllPrimes(max = 1e10):
  f = open('prime.txt')
  #f = open('Primes.txt')
  primes = []
  for line in f:
    for y in (line.rstrip('\n').split()):
      if int(y) < max:
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

primes = getAllPrimes(100000)
#primes = getAllPrimes(1000000)

circulars = []
for prime in primes:
  #print prime
  isP = 1
  sPrime = str(prime)
  length = len(str(sPrime)) # number of digits
  for iter in xrange(length):
    if isP:
      sPrime = iterate(sPrime)
      if not IsPrime(int(sPrime), primes):
        isP = 0
  if isP:
    circulars.append(prime)

print len(circulars), circulars
