#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import numpy
import copy

def invert(list):
  iList = zip(*list)
  rList = []
  rRow = []
  for row in iList:
    for el in row:
      rRow.append(el)
    rList.append(rRow[:])
    del rRow[:]

  return rList

f = open('P345.txt')
rows = []
columns = []
for line in f:
  row = [1000-7-int(x) for x in line.split()]
  rows.append(row[:])

pristineRow = copy.deepcopy(rows)

#row operations first!
for row in rows:
  minEl = min(row)
  for el in row:
    row[row.index(el)] = el - minEl

cols = invert(rows)


for col in cols:
  minEl = min(col)
  for el in col:
    col[col.index(el)] = el - minEl

rows = invert(cols)
print '  '
Eyes = []
Jays = []
zeroes = []
for i, row in enumerate(rows):
  for j, el in enumerate(row):
    print '%3i'%int(el),
    if el == 0:
      Eyes.append(i)
      Jays.append(j)
      zeroes.append((i,j))
  print ' '

print ' ' 
costs = []
print zeroes
print ' ' 
for i,j in zip(Eyes, Jays):
  if Eyes.count(i) == 1 and Jays.count(j) == 1:
    print i, j, 993- pristineRow[j][i]
print ' ' 

