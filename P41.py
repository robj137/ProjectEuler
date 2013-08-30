#!/usr/bin/python

primefile = open('Primes33000.txt')
permfile = open('perms9pan.txt')

primes = []
pans = []
for number in primefile:
  primes.append(int(number.rsplit()[0]))
 
valids = []
for number in permfile:
  isPrime = True
  pan =  (int(number.rsplit()[0]))
  for prime in primes:
    if prime*prime > pan:
      break
    if pan%prime == 0:
      isPrime = False
      break
  if isPrime == 1:
    valids.append(pan)

print 'The maximum pandigital prime (1-9) is',max(valids)

