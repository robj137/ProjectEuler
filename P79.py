#!/usr/bin/python

f = open('keylog.txt')
numbers = []
for line in f:
  numbers.append(str(line).rstrip('\n'))
f.close()

PIN = '73162890'

for n in numbers:
  i = PIN.find(n[0])
  j = PIN.find(n[1])
  k = PIN.find(n[2])
  if j < i or j > k or i > k:
    print 'shenanigans'

