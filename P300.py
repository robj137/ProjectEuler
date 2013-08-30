#!/usr/bin/python

import sys

def findFibonnacci(n):
  n = int(n)-1
  fib = (1,1)
  while n > 0:
    n = n-1
    fib = (fib[1], fib[0] + fib[1])
  return fib

if __name__ == '__main__':
  print findFibonnacci(int(sys.argv[1]))[0]
