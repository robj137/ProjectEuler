#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import numpy
import copy

def convertToList(aMat):
  if len(aMat) == 1:
    aMat = aMat.T
  list = []
  for i in aMat:
    list.append(int(i))
  return list

def MaxMinMatrix(m, Nmax):
  N = max(len(m), len(m.T))
  cMat = numpy.matrix([[Nmax for i in range(0,N)] for j in range(0,N)])
  return cMat-m

def minimizeRow(aRow):
  newRow = [int(i) for i in aRow]
  minN = min(newRow)
  minRow = []
  for j in newRow:
    minRow.append(j - minN)
  return minRow

def zeroRows(aMatrix):
  for i in range(0,len(aMatrix)):
    col = aMatrix[:,i]
    cMax = max(col)
    aMatrix[:,i] = (numpy.matrix(minimizeRow(col))).T
  return aMatrix

def assignJobs(aMat):
  zeroMat = copy.deepcopy(aMat)
  rowLines = []
  colLines = []
  zeros = []
  nZeros = 0
  isFlipped = false
  while 0 in zeroMat:
    for j,row in enumerate(zeroMat):
      lrow = convertToList(row)
      if lrow.count(0) == 1:
        i = lrow.index(0)
        nZeros = nZeros + 1
        aMat[i,j] = 1000

        rowLines.append(j)
        while 0 in convertToList(zeroMat[i,:]):
          jIndex = convertToList(zeroMat[i,:]).index(0)
          zeroMat[i,jIndex] = 2000
    zeroMat = zeroMat.T
    isFlipped = not(isFlipped)
  if isFlipped:
    zeroMat = zeroMat.T
    # this matrix now has 1000 for assignments.
    rowsToMark = [int(i) for i in range(len(zeroMat))]
    colsToMark = []
    for j, row in enumerate(zeroMat):
      lrow = convertToList(row)
      if 1000 not in lrow:
        rowsToMark.remove(j)
      iIndex = lrow.find(1000)


def getCovers(m):
  aMat = copy.deepcopy(m)
  xCovers = 0
  yCovers = 0
  xCovers, yCovers = assignJobs(aMat)
  while 0 in aMat: 
    x0 = []
    y0 = []
    for row in aMat:
      lRow = convertToList(row)
      x0.append(lRow.count(0))
    for row in aMat.T:
      lRow = convertToList(row)
      y0.append(lRow.count(0))
    xmax = max(x0), x0.index(max(x0))
    ymax = max(y0), y0.index(max(y0))
    if xmax > ymax:
      aMat[xmax[1],:] = markRow(aMat[xmax[1],:])
      xCovers = xCovers + 1
    else:
      aMat.T[ymax[1],:] = markRow(aMat.T[ymax[1],:])
      yCovers = yCovers + 1
  print xCovers + yCovers
  print m
  #kontinue = raw_input('continue? ')
  #if kontinue == 'y':
  if xCovers + yCovers == len(m):
    print 'yeehaw'
    print '-----------------------------------------------------------------------'
    print aMat
    print m
    print '-----------------------------------------------------------------------'
    return m
  else:
    minElement = 1000
    for row in aMat:
      if int(min(row.T)) < minElement:
        minElement = int(min(row.T))
    newMat = copy.deepcopy(m)
    for i in range(0,len(newMat)):
      for j in range(0, len(newMat)):
        if aMat[i,j] == 1000:
          newMat[i,j] = newMat[i,j]
        elif aMat[i,j] == 2000:
          newMat[i,j] = newMat[i,j] + minElement
        else:
          newMat[i,j] = newMat[i,j] - minElement
    cMat = getCovers(newMat)
    return cMat
    #return aMat

def markRow(aRow):
  list = convertToList(aRow)
  rList = []
  for el in list:
    if el == 1000:
      rList.append(2000)
    else:
      rList.append(1000)
  return rList

f = open('P345.txt')
rows = []
col = []
for line in f:
  rows.append([int(i) for i in line.split()])
m = numpy.matrix(rows)
pristineM = numpy.matrix(rows)

N = len(m)
mMax = 0
for i in range(0,N):
  if int(max(m[:,i]))> mMax:
    mMax = int(max(m[:,i]))

cMat = MaxMinMatrix(m, mMax)
zeroRows(cMat)
cMat = cMat.T
zeroRows(cMat)
cMat = cMat.T

covers = getCovers(cMat)

elements = []
rowstokill = []
colstokill = []
while len(elements) < len(cMat):
  if len(covers) ==1 and len(covers.T) == 1:
    elements.append(int(pristineM[0,0]))
  else:
    print 'So far, found', len(elements), 'distinct zeros', elements
    del rowstokill[:]
    del colstokill[:]
    for j, row in enumerate(covers):
      lRow = convertToList(row)
      if lRow.count(0) == 1:
        i = lRow.index(0)
        if j not in rowstokill and i not in colstokill:
          rowstokill.append(j)
          colstokill.append(i)
          elements.append(pristineM[i,j])
        else:
          print 'uh oh', i, j
          print covers
    rowstokeep = range(0, len(covers))
    colstokeep = range(0, len(covers))
    for i in rowstokill:
      rowstokeep.remove(i)
    for j in colstokill:
      colstokeep.remove(j)
    print '-----------'
    print covers
    print pristineM
    covers = covers[rowstokeep,:]
    covers = covers[:,colstokeep]
    pristineM = pristineM[rowstokeep,:]
    pristineM = pristineM[:,colstokeep]
    print '-----------'
    covers = covers.T
    pristineM = pristineM.T

sum = 0
for el in elements:
  sum = sum + el

print elements, sum
