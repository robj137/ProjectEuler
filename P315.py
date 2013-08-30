#!/usr/bin/python

import sys
import datetime


def getCost():
  Q = {}
  Q[0] = 0b0111111
  Q[1] = 0b0000110
  Q[2] = 0b1011011
  Q[3] = 0b1001111
  Q[4] = 0b0110110
  Q[5] = 0b1101101
  Q[6] = 0b1111011
  Q[7] = 0b0001111
  Q[8] = 0b1111111
  Q[9] = 0b1101111
  Q[' '] = 0b0000000
  Cost = {}
  theRange = range(0,10)
  theRange.insert(0,' ')
  for M in theRange:
    for N in theRange:
      m1 = Q[M]
      m2 = Q[N]
      n1 = bin(m1).count('1')
      n2 = bin(m2).count('1')
      sim = bin(m1&m2).count('1')
      Cost[(N,M)] = (n1+n2)-2*sim
  return Cost

def calculateDigitalRoots(aNumber):
  roots = [str(aNumber)]
  blank = '        '
  length = len(roots[0])
  while len(str(int(roots[-1]))) > 1:
    roots.append(str(sum(int(i) for i in roots[-1])))
  for i,y in enumerate(roots[1:]):
    roots[i+1] = (blank+y)[-length:]
  return roots

#def getMaxsList(roots):
  

def calculateTransitionCost(aNumber):
  #first get the roots
  roots = calculateDigitalRoots(aNumber)
  MaxDigits = []
  SamDigits = []
  for root in roots:
    print 'hi'
  #need to form the tuples that will 
  #make sure that roots is 2 or greater!

def calculatePairCost(M,N,cost):
  return sum(cost[(int(i),'_')] for i in str(N))

    
def main():
  start = datetime.datetime.now()
  if len(sys.argv) > 1:
    prime = int(sys.argv[1])
    print 'The difference for', prime, 'is',
    print calculateTransitionCost(prime)
    end = datetime.datetime.now()
    print end-start
  else:
    print 'Calculating for all primes between 1e7 and 2e7'
    infile = open('Primes2e7.txt')
    i = 0
    Sams = []
    Maxs = []
    Diffs = []
    for line in infile:
      prime = int(line.split()[0])
      Sam, Max = calculateTransitionCost(prime)
      Sams.append(Sam)
      Maxs.append(Max)
      Diffs.append(Sam-Max)
    y = open('SamMax.txt','w')
    for el in zip(Sams, Maxs, Diffs):
      y.write(str(el)+'\n')
    p.close()
    end = datetime.datetime.now()
    print end-start

if __name__ == '__main__':
  main()
