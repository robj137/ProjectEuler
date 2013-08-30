#!/usr/bin/python

from math import sqrt

def getB(N):
  return (1 + sqrt(1+2*N*N - 2*N))/2

for N in range(long(1e12), long(1e12)+1000000):
#for N in range(1000000000000, 1000000011100):
  if sqrt(2*N*N - 2*N + 1) - int(sqrt(2*N*N - 2*N + 1)) < 0.000000001:
    b = int(getB(N))
    print N, b, float(b*(b-1))/float(N*(N-1))
