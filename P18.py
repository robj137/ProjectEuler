#!/usr/bin/python

import sys

a = []
fi = open(sys.argv[1], 'r')
for line in fi:
  a.append([int(z) for z in line.split()])
fi.close()
c = []
a.reverse()
while len(a) > 1:
#for i in range(0, len(a)-1):
  b = a.pop(0)
  n = a.pop(0)
  n.append(0)
  for num in n:
    if num > 0:
      c.append(num + max(b[k], b[k+1]))
      
  for k in range(0, len(b)-1):
  #del a[0]
  a.insert(0,c[:])
  print c
  del c[:]


print 'finally', a
