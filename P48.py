#!/usr/bin/python
def f(num):
  result = 0 
  for i in range(1,num+1): 
    result += xp(i) 
  return result 

def xp(num):
  result = 1
  for i in range(0, num):
    result *= num
  return result

number = f(1000)
print number
