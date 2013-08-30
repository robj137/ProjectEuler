#!/usr/bin/python

import sys

def getPatternLength(N):
  string = str(int(10**10000)/N)
  #print string[0:50]
  return findPatternInString(string)


def findPatternInString(string):
  copy = string[:]
  sub = string[-10:]
  index = 0
  delta = 0
  for y in range(0,5):
    delta = -index + string.find(sub,index+1)
    index = string.find(sub,index+1)
  return delta


if __name__ == "__main__":
  deltas = []
  for i in range(1, 1001):
    length = getPatternLength(i)
    print i, length
    deltas.append((length, i))

  print max(deltas)
