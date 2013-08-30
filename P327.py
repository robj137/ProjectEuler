#!/usr/bin/python

import sys

def calculateM(C,R):
  C = int(C)
  R = int(R)
  # C is number of cards to carry
  # R is number of rooms
  if R < 3 or R > 30:
    print 'Number of rooms', R, 'is out of range'
    return 0
  # The Cth room always requires a cost of C, and so if R <=C, then Cost = R
  if R < C:
    cost = R + 1 # because there are R+1 doors to cross, and you don't need to
                 # store anything
    print 'Total # of Cards for', R, 'rooms at cost', C, 'is', cost
    return cost
  if C == 3:
    #special case
    cost = 3
    for i in range(1, R-1):
      cost = cost + 3**i
    print 'Total # of Cards for', R, 'rooms at cost', C, 'is', cost
    return cost
  # So if R > C, then need to figure out the cost of the excess rooms.
  xRooms = R-C + 1
  cost = C
  while xRooms > 0:
    cost = getCostToFillRoomAndEnter(C, cost)
    xRooms = xRooms - 1
  print 'Total # of Cards for', R, 'rooms at cost', C, 'is', cost
  return cost

def getCostToFillRoomAndEnter(C, N):
  # Need to put N cards into the room, but can only carry C at a time. That
  # means that each trip can add C-2 cards except for the last trip, which only
  # costs C-1
  nLeft = N
  cost = 0
  while nLeft > C-2: # i.e. if C = 4 and nLeft = 4, then 1+2+1 leaves nLeft = 2,
    cost = cost+1 # entering the rooma
    nLeft = nLeft - (C-2)
    cost = cost + (C-2)
    if nLeft == 1:
      nLeft = nLeft - 1
      cost = cost + 1 #and we're all set now, nleft = 0
    else:
      cost = cost + 1 # have to exit the room
  #ok, so now the number left is anywhere from 2 to C-2
  if nLeft > 0:
    cost = cost + 1 #enter the room
    cost = cost + nLeft
    nLeft = 0
  return cost
  

#C = int(sys.argv[1])
#R = int(sys.argv[2])
#print calculateM(C,R)
#print getCostToFillRoomAndEnter(C,R)
sum = 0
for C in range(int(sys.argv[1]), int(sys.argv[2])):
  sum = sum + calculateM(C,30)
print sum
