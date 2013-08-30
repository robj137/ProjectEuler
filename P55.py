#!/usr/bin/python

import sys

def convert(N):
  return N + int(str(N)[::-1])

def isPalindrome(N):
  if str(N) == str(N)[::-1]:
    return 1
  else:
    return 0





if __name__ == '__main__':

  nLychrel = 0
  for i in range(1, 10000):
    iterations = 0
    isLychrel = 1
    while iterations < 50:
      iterations += 1
      i = convert(i)
      if isPalindrome(i):
        isLychrel = 0
        break
    if isLychrel:
      nLychrel += 1

  print nLychrel
