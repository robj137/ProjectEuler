#!/usr/bin/python

def IsNumberValid(n):
  sN = str(n)
  if len(sN) == 1:
    return True
  candies = []
  candies.append(int(sN[0]))
  sN = sN[1:]
  while len(sN) > 0:
    candy = int(sN[0])
    if candy in candies:
      return False
    candies.append(candy)
    sN = sN[1:]
  return True

def AreNumbersCompatible(nList):
  # assume that IsNumberalid already run
  combined = int(''.join(str(n) for n in nList))
  return IsNumberValid(combined)

def AreNumbersComplete(nList):
  if sum([len(str(n)) for n in nList]) != 9:
    return False
  if not AreNumbersCompatible(nList):
    return False
  return True

for i in range(9000,9999):
  if AreNumbersCompatible([i, i*2]):
    print i, i*2
