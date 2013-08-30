#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import math
import sys

'''
For a prime p let S(p) = ((p-k)!) mod(p) for 1  k  5.

For example, if p=7,
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! =
720+120+24+6+2 = 872.
As 872 mod(7) = 4, S(7) = 4.

It can be verified that S(p) = 480 for 5  p  100.

Find S(p) for 5  p  108.
'''

primes = open('Primes2e7.txt', 'r')

def getPrimesFromRange(s,t):
  primes = []
  for candidate in range(s,t):
    

def S(p):
  theSum = 0
  for k in range(1,6):
    theSum += math.factorial(p-k)
  print p, theSum%p
  return theSum%p

def main():
  if len(sys.argv) != 2:
    print 'Need to give an integer'
    sys.exit()
  pmax = int(sys.argv[1])
  if pmax < 5:
    print 'Need to give an interger < 5, yo'
    sys.exit()
  sumS = 0
  for p in range(5, pmax):
    if p
    sumS += S(p)
  print 'Sum is', sumS

if __name__ == '__main__':
  main()

