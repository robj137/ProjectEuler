#!/usr/bin/python

from math import sqrt

per = 0
for n in range(2, 34333333):
  o = n-1
  h = sqrt(n*n - o*0.5*o*0.5)
  area = h*o
  if (abs(int(area) - area)) < 0.000000000001:
    if n+2*o < 1e9:
      per += n+2*o
  o = n+1
  h = sqrt(n*n - o*0.5*o*0.5)
  area = h*o
  if (abs(int(area) - area)) < 0.000000000001:
    print n, int(area), area
    if n+2*o < 1e9:
      per += n+2*o
print n+2*o
print per
