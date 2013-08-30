#!/usr/bin/python

import sys
import math


for i in range(3, 1407000):
  s = str(i)
  N = 0
  for n in s:
    N = N + math.factorial(int(n))
  if N == i:
    print i
