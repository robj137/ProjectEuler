#!/usr/bin/python

def GetNumericValue(name):
  result = 0
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for d in name:
    result += alphabet.find(d)+1

  return result

f = open('names.txt','r')
list = []
for line in f:
  list.append(line)

list.sort()
sum = 0
for index, item  in enumerate(list):
  sum += GetNumericValue(item)*(index+1)

print  sum
