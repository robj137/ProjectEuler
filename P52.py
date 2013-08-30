#!/usr/bin/python

import sys

def sameDigits(N, M):
  m = []
  n = []
  for i in str(N):
    n.append(i)
  for i in str(M):
    m.append(i)
  n.sort()
  m.sort()
  if n == m:
    return 1
  else:
    return 0

if __name__ == '__main__':

  for i in range(1, 200000):
    if sameDigits(i, 2*i):
      if sameDigits(i, 3*i):
        if sameDigits(i, 4*i):
          if sameDigits(i, 5*i):
            if sameDigits(i, 6*i):
              print i, 'huh'
