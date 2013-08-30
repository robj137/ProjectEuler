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

validproducts = []
for i in range(2,1000):
  if '0' not in str(i):
    for j in range(3,20000):
      if '0' not in str(j) and '0' not in str(i*j):  
        if AreNumbersComplete([i,j, i*j]):
          if i*j not in validproducts:
            print i, j, i*j
            validproducts.append(i*j)

print len(validproducts)
print sum(validproducts)
