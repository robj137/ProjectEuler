#include <stdio.h>
#include <iostream>

int GetGCD(int a, int b)
{
  if (b == 0) return a;
  return GetGCD(b,a%b);
}

void simplify(int &a, int &b)
{
  int gcd = GetGCD(a,b);
  if(gcd != 1){
    a /= gcd;
    b /= gcd;
  }
}

int GetN(int k)
{
  int a = 1;
  int b = k;
  while(b!= 1){
    a = a+1;
    b = b-1;
    simplify(a,b);
  }
  return a;
}

int GetCubeSum(int k)
{
  int cubeSum = 0;
  for(int l = 1; l<=k; l++){
    cubeSum += GetN(l*l*l);
  }
  return cubeSum;
}


int main(int argc, char* argv[])
{
  std::cout << GetCubeSum(atoi(argv[1])) << std::endl;
}
