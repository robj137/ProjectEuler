#!/usr/bin/python

from datetime import datetime

def getCurrency():
  money = [(200,1),(100,2),(50,4), (20,10), (10,20), (5,40), (2,100), (1,200)]
  #dict = [1,2,5,10,20,50,100,200]
  return money

begin = datetime.now()

amount = 200

nPermutations = 0


for j in range(0,3):
  for k in range(0, 5):
    for l in range(0, 11):
      for m in range(0, 21):
        for n in range(0, 41):
          for o in range(0, 101):
            for p in range(0, 201):
              mon = j*100
              mon = mon+ k*50
              mon = mon+ l*20
              mon = mon+ m*10
              mon = mon+ n*5
              mon = mon+ o*2
              mon = mon+ p
              if mon == 200:
                nPermutations = nPermutations + 1
              if mon > 200:
                break

print nPermutations

end = datetime.now()

print end-begin
