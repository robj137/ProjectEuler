#include <math.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;


int GetWordValue(string);
int GetAsciiIntValue(string);
int IsTriangle(int);

void some(){
  string str;
  vector<string> words;
  vector<int>  value;
  ifstream in("words.txt");
  while(in){
    in >> str;
    words.push_back(str);
    value.push_back(GetWordValue(str));
  }

  int SumTriangle = 0;
  for(int k = 0; k<(int)words.size(); k++){
    SumTriangle += IsTriangle(value[k]);
    if(IsTriangle(value[k])) cout << words[k]<< endl;
  }
  cout << SumTriangle << endl;
}

int IsTriangle(int N){
  int val;
  val = sqrt(2*N);

  if((int)(0.5*val*(val+1)) == N){
    return 1;
  }
  return 0;


}

int GetWordValue(string str)
{
  int sum = 0;
  for(int k = 0; k<(int)str.size(); k++){
    sum += GetAsciiIntValue(str.substr(k,1));
  }
  return sum;
}

int GetAsciiIntValue(string str)
{
  static map<string,int> charmap;
  charmap["A"] = 1;
  charmap["B"] = 2;
  charmap["C"] = 3;
  charmap["D"] = 4;
  charmap["E"] = 5;
  charmap["F"] = 6;
  charmap["G"] = 7;
  charmap["H"] = 8;
  charmap["I"] = 9;
  charmap["J"] = 10;
  charmap["K"] = 11;
  charmap["L"] = 12;
  charmap["M"] = 13;
  charmap["N"] = 14;
  charmap["O"] = 15;
  charmap["P"] = 16;
  charmap["Q"] = 17;
  charmap["R"] = 18;
  charmap["S"] = 19;
  charmap["T"] = 20;
  charmap["U"] = 21;
  charmap["V"] = 22;
  charmap["W"] = 23;
  charmap["X"] = 24;
  charmap["Y"] = 25;
  charmap["Z"] = 26;

  return charmap[str];;
}



int main(int argc, char* argv[])
{
  some();
  return 1;
}
