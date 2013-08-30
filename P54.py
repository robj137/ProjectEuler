#!/usr/bin/python

import sys


def getHandSuits(aHand):
  nSuits = 0
  suits = [0,0,0,0]
  for card in aHand:
    if 'H' in card:
      suits[0] = suits[0]+1
    if 'D' in card:
      suits[1] = suits[1]+1
    if 'C' in card:
      suits[2] = suits[2]+1
    if 'S' in card:
      suits[3] = suits[3]+1
  return suits

def isFlush(hand):
  suits = getHandSuits(hand)
  if 5 in suits:
    return True
  return False

def isStraight(hand):
  vals = []
  for card in hand:
    vals.append(card[0])
  vals.sort()
  if vals[4] == 1+vals[3]:
    if vals[3] == 1+vals[2]:
      if vals[2] == 1+vals[1]:
        if vals[1] == 1+vals[0]:
          return True
  return False

def getMultiplicity(hand):
  vals = {}
  for card in hand:
    if card[0] in vals:
      vals[card[0]] += 1
    else:
      vals[card[0]] = 1
  hkeys, hvals = vals.keys(), vals.values()
  num4 = hvals.count(4)
  num3 = hvals.count(3)
  num2 = hvals.count(2)
  val4 = val3 = val2 = 0
  if num4:
    val4 = hkeys[hvals.index(4)]
  if num3:
    val3 = hkeys[hvals.index(3)]
  if num2:
    val2 = hkeys[hvals.index(2)]
  return [num4, val4], [num3, val3], [num2, val2]

def getCardSuit(card):
  return card[1]

def getCardValue(card):
  val = card[0]
  try:
    value = int(val)
  except:
    if val == 'T':
      value = 10
    if val == 'J':
      value = 11
    if val == 'Q':
      value = 12
    if val == 'K':
      value = 13
    if val == 'A':
      value = 14
  return value

def convertHand(cards):
  hand = []
  for card in cards:
    hand.append((getCardValue(card), getCardSuit(card)))
  return hand

def getHighCard(cards):
  return max(getCardValue(cards))

def getHandRank(cards):
  straight = isStraight(cards)
  flush = isFlush(cards)
  if straight and flush:
    if 14 in cards:
      return 280
    else:
      return 270
  fours, threes, twos = getMultiplicity(cards)
  if fours[0] == 1:
    return 260+0.01*fours[1]
  if threes[0] == 1 and twos[0] == 1:
    return 250 + 0.01*threes[1]
  if flush:
    return 240
  if straight:
    return 230
  if threes[0] == 1:
    return 220 + 0.01*threes[1]
  if twos[0] == 2:
    return 210 + 0.01*twos[1]
  if twos[0] == 1:
    return 200 + 0.01*twos[1]
  return 100+max(cards)[0]

f = open('poker.txt')
i = 0
for game in f:
  cards = game.split()
  handA = convertHand(cards[0:5])
  handB = convertHand(cards[5:])
  
  if getHandRank(handA) > getHandRank(handB):
    i = i+1
    print getHandRank(handA), getHandRank(handB)
  #fours, threes, twos = getMultiplicity(handA)
  #if fours:
  #  print handA
  #fours, threes, twos = getMultiplicity(handB)
  #if twos == 2:
  #  print handB
print i
