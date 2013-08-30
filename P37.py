#!/usr/bin/python

import sys

# obvious ones are all of the 2 digit primes:
# 23, 29, 37, 53, 73


def getAllPrimes():
  f = open('prime.txt')
  #f = open('Primes.txt')
  primes = []
  
  for line in f:
    for y in (line.rstrip('\n').split()):
      if len(str(y)) < 2:
        primes.append(int(y))
      if len(str(y)) > 1:
        x = str(y)[1:]
        if '0' in x or '2' in x or '4' in x or '6' in x or '8' in x or len(x) < 1:
          pass
        else:
          primes.append(int(y))
  f.close()
  print primes[0:200]
  return primes

def chopLeft(N):
  # chop off the highest integer
  return int(str(N)[1:])

def chopRight(N):
  # chop off the highest integer
  return int(str(N)[0:-1])

def isTrunctable(N,primes):
  isT = 1
  n = N
  s = str(n)
  if len(str(n)) < 2:
    return 0
  #if '0' in s or  '4' in s or '6' in s or '8' in s or len(str(n)) < 2:
  #if len(str(n)) < 2:
  #  return 0
  while len(str(n)) > 1:
    if n not in primes:
      return 0
    n = chopLeft(n)
    if len(str(n)) ==1:
      isT = isT*(n in primes)
  n=N
  while len(str(n)) > 1:
    if n not in primes:
      return 0
    n = chopRight(n)
    if len(str(n)) ==1:
      isT = isT*(n in primes)
  return isT
  

if __name__ == '__main__':
  trunks = []
  i = 0
  primes = getAllPrimes()
  print 'found', len(primes), 'primes'
  for l in primes:
    i = i+1
    if i%1000 == 0:
      print '   ',float(i)/float(len(primes))
    if isTrunctable(l,primes):
      trunks.append(l)
      print l
      if len(trunks) == 11:
        print 'found 11'
        print 'trunctable numbers are', trunks
        print 'sum of truncable numbers is',sum(trunks)
        break

