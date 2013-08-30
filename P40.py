#!/usr/bin/python

num = ''
for i in range(0, 185186):
  num = num + str(i)

prod = 1
for i in range(0, 7):
  prod = prod*int(num[10**i])

print num
print prod
