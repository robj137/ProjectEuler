#!/usr/bin/python

import sys

def simplify(a,b):
  gcd = getGCD(a,b)
  if gcd != 1:
    a = a/gcd
    b = b/gcd
  return a,b

def getGCD(a,b):
  if b == 0:
    return a
  return getGCD(b,a%b)
  
def getN(k):
  a = 1
  b = k
  while b != 1:
    a,b, = simplify(a+1,b-1)
  return a

def getN3(k):
  a = 1
  b = k*k*k
  while b != 1:
    a,b, = simplify(a+1,b-1)
  return a

def getCubeSum(k):
  k = int(k)
  cubeSum = 0
  for j in range(1, k+1):
    print j, getN(j**3)
    cubeSum = cubeSum + getN(j**3)
  return cubeSum

def sumCube(k):
  k = int(k)
  cubeSum = 0
  for j in range(1,k+1):
    cubeSum = cubeSum + getN(j**3)
    #print j, getN(j**3), cubeSum
  return cubeSum

def main(k):
  print getCubeSum(k)

def euler343c(N=2*10**6):
   L=N+2
   M=[0]*L 
   MF=[1]*L
   A=[0]*L 
   AF=[1]*L 
   for k in xrange(1,L):
      M[k]=k
      A[k]=k*k-k+1    
   for k in xrange(1,L):
      p=M[k]
      if p>1:
         for x in xrange(k,L,p):
            while M[x]%p==0: M[x]/=p
            MF[x]=p
      p=A[k]
      if p>1:
         for x in xrange(k%p,L,min(L,p)):
            while A[x]%p==0: A[x]/=p
            AF[x]=max(AF[x],p)
         for x in xrange(min(L,(1-k)%p),N+1,min(L,p)):
            while A[x]%p==0: A[x]/=p
            AF[x]=max(AF[x],p)
   print sum(max(MF[k+1],AF[k])-1 for k in xrange(1,N+1))

if __name__ == '__main__':
  main(sys.argv[1])
  #euler343c()
