#!/usr/bin/python

from random import random



# circular binary, n=5, 2^5 = 32, put them in a circle, and read off 5-digit
# numbers, going clockwise.  they're distinct, which means that there are 32 of
# them, which means that it's all numbers from 0 to 31

# we can start with 11111 (31), because that has to be there, and the next has
# to be# 0 (11110, or 30), and the previous one had to be 0 (01111, 15)

def Check(num):
  nums = {}
  ahead = '0000'
  for i in range(0, 32):
    nums[((ahead + str(bin(i)[2:]))[-5:])] = 1
  num += num[0:5]
  for i in range(0,32):
    if nums[num[i:i+5]] == 0:
      return 0
    else:
      nums[num[i:i+5]] = 0
  return 1

def PreCheckIteration(num):


def GetIteration(i):
  #i is a number
  iteration = '0111110'
  for l in range(0, 20):
    if i & 2**l:
      iteration += '1'
    else:
      iteration += '0'
  return iteration


def GiveItATry():
  nums = {}
  ahead = '0000'
  for i in range(0, 32):
    nums[((ahead + str(bin(i)[2:]))[-5:])] = 1
  circle = '0111110'
  # remove 11111 and 11110:
  nums['11111'] = 0
  nums['11110'] = 0
  nums['01111'] = 0


  decision = '0'
  level = 0
  iters = 0
  beaters = 0
  biters = 0
  baddies = 0
  while len(circle) < 28:
    iters += 1
    if baddies > 100:
      print 'broken'
      break
    if iters > 1000:
      nums[circle[-5:]] = 1
      circle = circle[0:-1]
      iters = 0
      beaters += 1
    if beaters > 20:
      nums[circle[-5:]] = 1
      circle = circle[0:-1]
      nums[circle[-5:]] = 1
      circle = circle[0:-1]
      beaters = 0
      biters +=1
    if biters > 20:
      nums[circle[-5:]] = 1
      circle = circle[0:-1]
      nums[circle[-5:]] = 1
      circle = circle[0:-1]
      nums[circle[-5:]] = 1
      circle = circle[0:-1]
      nums[circle[-5:]] = 1
      circle = circle[0:-1]
      biters = 0
      baddies += 1
      print 'bad'
    circle += str(int(round(random())))
    if nums[circle[-5:]] == 0:
      circle = circle[0:-1]
    else:
      nums[circle[-5:]] = 0

  for key in nums.keys():
    if nums[key] == 1 and len(circle) < 32:
      if circle[-4:] == key[0:4]:
        circle += key
        nums[key] = 0
  if len(circle) == 32:
    circle += circle[0:5]
    success = 1
    print circle
    for i in range(24, 33):
      if nums[circle[i:i+5]] == 0:
        success = 0
      else:
        nums[circle[i:i+5]] = 0

    return success
  else:
    return 0

for i in range(0, 2**20):
  print GetIteration(i)
