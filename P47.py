#!/usr/bin/python
from datetime import datetime
import sys

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

def getPrimeFactorization(N, primes):
  n = N
  factors = {}
  while n > 1:
    p = primes[:]
    for i in primes:
      a,b = divmod(n, i)
      if b == 0:
        factors[i] = 1
        n = a
        break
    if i == primes[-1]:
      break
  return factors.keys()

if __name__ == '__main__':

  begin = datetime.now()
  bigN = int(sys.argv[1])
  primes = getAllPrimes(0,(bigN+1)**0.5)
  for i in xrange(2,bigN):
    if len(getPrimeFactorization(i, primes)) == 4:
      if len(getPrimeFactorization(i+1, primes)) == 4: 
        if len(getPrimeFactorization(i+2, primes)) == 4:
          if len(getPrimeFactorization(i+3,primes)) == 4:
            print 'hi', i
            break

  end = datetime.now()
  print end-begin
