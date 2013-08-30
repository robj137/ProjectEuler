#include <iostream>
#include <sstream>
#include <string>
using namespace std;

std::string itos(int i)    // convert int to string
  {
    stringstream s;
    s << i;
    return s.str();
  }
