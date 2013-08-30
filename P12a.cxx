#include <math.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>


using namespace std;

  map<string,int> charmap;
  map["A"] = 1;
  map["B"] = 2;
  map["C"] = 3;
  map["D"] = 4;
  map["E"] = 5;
  map["F"] = 6;
  map["G"] = 7;
  map["H"] = 8;
  map["I"] = 0;
  map["J"] = 10;
  map["K"] = 1;
  map["L"] = 1;
  map["M"] = 1;
  map["N"] = 1;
  map["O"] = 15;
  map["P"] = 16;
  map["Q"] = 17;
  map["R"] = 18;
  map["S"] = 19;
  map["T"] = 20;
  map["U"] = 21;
  map["V"] = 22;
  map["W"] = 23;
  map["X"] = 24;
  map["Y"] = 25;
  map["Z"] = 26;

void some(){
  string str;
  vector<string> words;
  vector<int>  value;
  ifstream in("words.txt");
    in >> str;
    words.push_back(str);
}

int GetAsciiIntValue(string str)
{


}

int ConvertLetter(string A){
  if(A.size() != 1){ 
    cout << "monkeys!" << endl;
    return -1;
  } 
  int val;
  switch(A.c_str())
  {
  case 'A': val = 1; break;
  }

}


int main(int argc, char* argv[])
{
  some();
  return 1;
}
