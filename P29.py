#!/usr/bin/python
a = [2**2]
for i in range(2, 101):
  for j in range(2,101):
    a.append(i**j)

fruit = set(a)

print len(a)
print len(fruit)
