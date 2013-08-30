#!/usr/bin/python


def getAllPrimes():
  f = open('prime.txt')
  #f = open('Primes.txt')
  primes = []
  for line in f:
    for y in (line.rstrip('\n').split()):
      primes.append(int(y))
  f.close()
  return primes

def IsPrime(N, primes):
  if N in primes:
    return 1
  else:
    return 0

def evaluate(n,a,b):
  return n*n + a*n + b

primes = getAllPrimes()
B = primes[0:168]
most = (0, 0, 0)
for a in range(-999, 1000):
  for b in B:
    #print a,b
    i = 0
    while(1):
      #print i,
      if not IsPrime(evaluate(i,a,b), B):
        break
      i = i+1
    #print ' '
    if (i, a, b) > most:
      most = (i,a,b)


print most
print most[1]*most[2]
