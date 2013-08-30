#!/usr/bin/python
import sys

def explode(num):
  result = 0
  for digit in str(num):
    result += (int(digit))**5
  return result

boom = 0
for i in range(2,int(sys.argv[1])+1):
  boom = explode(i)
  if(boom == i):
    print "booyeah" 
    print i
