#!/usr/bin/python

psum = 0
for a in range(0,101):
  for b in range(0,101):
    sum = 0
    for s in str(a**b):
      sum += int(s)
    if sum > psum:
      psum = sum

print psum
    
