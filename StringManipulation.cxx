#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <vector>
#include "funcs.cxx"
using namespace std;

int GetNDigits(int N){
  int k = 0;
  while(N/((int)pow(10,k))){
    k++;
  }
  return k;
}

int GetNBits(int N){
  int k = 0;
  while(N/((int)pow(2,k))){
    k++;
  }
  return k;

}

string NumberAdder(string N1, string N2)
{

  int Length1 = N1.size();
  int Length2 = N2.size();
  for(int j = 0; j<(Length1-Length2); j++){
    N2.insert(0,"0");
  }
  for(int j = 0; j<(Length2-Length1); j++){
    N1.insert(0,"0");
  }
  int Length = N1.size();

  int carryover = 0;
  int colsum;
  reverse(N1.begin(), N1.end());
  reverse(N2.begin(), N2.end());
  
 // vector<int> sum;
  string sum;
  for(int k = 0; k<Length; k++){
    colsum = carryover + atoi((N1.substr(k,1)).c_str()) + atoi((N2.substr(k,1)).c_str());
    sum += itos(colsum%10);
    carryover = colsum/10;
  }
  reverse(sum.begin(), sum.end());
  if(carryover){
    sum.insert(0, itos(carryover));
  }

  return sum;
}

string SimpleMultiply(string N1, string N2){
  if(N1.size() != 1) { return "fail!";}
  //N1 is the single digit, N2 is a string of numbers
  string result = "";
  for(int k = 0; k<atoi(N1.c_str()); k++){
    result = NumberAdder(result, N2);
  }
  return result;
}


string ComplexMultiply(string N1, string N2){
  string longer, shorter;
  if(N1.size() > N2.size()) {
    longer = N1;
    shorter = N2;
  } else {
    longer = N2;
    shorter = N1;
  }
  reverse(shorter.begin(), shorter.end());
  string sum = "";
  string row = "";
  for(int k = 0; k<(int)(shorter.size()); k++){
    row = SimpleMultiply(shorter.substr(k,1),longer);
    for(int l = 0; l<k; l++){
      row.insert(row.size(), "0");
    }
    sum = NumberAdder(row, sum);
  }
  return sum;
}

string Exponentiate(int E, string N1, int cutoff = 1e6){
  string value = "1";
  for(int k = 0; k<E; k++){
    value = ComplexMultiply(value, N1);
    if((int)value.size()>cutoff) value.erase(0,cutoff);

  }
  return value;
}
string DigitSum(string N)
{
  string sum = "0";
  for(int k = 0; k<(int)(N.size()); k++){
    sum = NumberAdder(sum, N.substr(k, 1));
  }
  return sum;
}

string GetDecimalString(int N)
{
  return itos(N);
}

string GetBinaryString(int N)
{
  int Lb = GetNBits(N);
  string value = "";
  for(int k = 0; k<Lb; k++){
    value.insert(0,itos((bool)(N&((int)pow(2,k)))));
  }
  return value;
}


bool IsAPalindrome(string str)
{
  string cstr = str;
  reverse(cstr.begin(), cstr.end());
  if(!str.compare(cstr)) return true;
  else return false;
}

bool IsAPalindrome(int N, string base = "decimal"){
  string str;
  if(base.compare("decimal") != 0) str = GetDecimalString(N);
  if(base.compare("binary") != 0) str = GetBinaryString(N);
  return IsAPalindrome(str);
}

/*
bool IsABinaryPalindrome(int N)
{
  int O = 0;
  int M = 0;
  for(int k = 0; k<20; k++){
    if(N&(int)pow(2,k)) {O = k;}
  } 
  for(int k = 1; k<=O; k++){
    if(k < 0.5*O){ // bit shift left
    M += (N&(int)pow(2,k-1))<<(L-k);
    } else { 
      M+= (N&(int)pow(2,k-1))>>(L-k);
    }
  }
  cout << O << endl;
  return 1;
}
*/
bool IsADecimalPalindrome(int N)
{
  int n = N;
  int M = 0;
  int L = GetNDigits(N);
  for(int k = 0; k<L; k++){
    M += (N%10)*pow(10,L-k-1);
    N /= 10;
  } 

  return (M == n);
}

bool IsAPalindrome(int number, int base)
{}
