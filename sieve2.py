#!/usr/bin/python

import sys
import math

def sieve(max):
  sievebound = (max-1) / 2
  sieve = range(0, sievebound)
  for i in range(0, len(sieve)):
    sieve[i] = 0
  crosslimit = (math.sqrt(max) - 1)/2
  for i in range(1, int(crosslimit)):
    if not sieve[i]:
      for j in range(2*i*(i+1), int(sievebound), (2*i+1)):
        sieve[j] = 1

  primes = []
  for i, value in enumerate(sieve):
    if not value:
      primes.append(2*i+1)
  return primes
#
N = int(sys.argv[1])
p = open('Primes.txt', 'w')
s = sieve(N)
for i in s:
  p.write(str(i)+'\n')
p.close()
