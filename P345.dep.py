#!/usr/bin/python

def invert(aLoL):
  inverted = zip(*aLoL)[:]
  iLol = []
  row = []
  for tup in inverted:
    for el in tup:
      row.append(el)
    iLol.append(row[:])
    del row[:]
  return iLol

def getMaxAndCut(aLoL):
  m = []
  for row in aLoL:
    m.append(max(row))
  #m = map(lambda x: max(x, key=lambda y: y), aLoL)
  #print m
  maxI = max(m)
  ndxj = m.index(maxI)
  ndxi = rows[ndxj].index(max(m))
  #print ndxi, ndxj
  temp = aLoL[0:ndxj] + aLoL[ndxj+1:]
  aLoL = invert(temp)[:]
  temp = aLoL[0:ndxi] + aLoL[ndxi+1:]
  aLoL = invert(temp)
  return aLoL, maxI

f = open('P345.txt')
rows = []
columns = []
for line in f:
  row = [1000-7-int(x) for x in line.split()]
  rows.append(row[:])

for row in rows:
  print row

maxI = 0
while len(rows) > 0:
  #print rows
  rows, theMax = getMaxAndCut(rows)
  maxI = maxI + theMax
#maxI = maxI + max

print maxI


