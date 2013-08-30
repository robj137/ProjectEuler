#!/usr/bin/python
from datetime import datetime
import sys

def getComposites(N):
  y = open('Primes.txt')
  primes = []
  for line in y:
    p = int(line.rstrip())
    if p < N+1:
      primes.append(p)
  comps = []
  for i in range(2, N+1):
    if i not in primes and i%2 ==1:
      comps.append(i)

  return comps

if __name__ == '__main__':

  begin = datetime.now()
  bigN = int(sys.argv[1])
  comps = getComposites(bigN)
  print comps
  end = datetime.now()
  print end-begin
