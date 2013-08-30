#include "StringManipulation.cxx"

using namespace std;

int main(int argc, char* argv[]){
  if(argc != 2) {
    cout << "Just one argument pleae, the number of digits " << endl;
    cout << "to look for in th fibonacci sequence." << endl;
    return 0;
  }

  string Number0 = "1";
  string Number1 = "1";
  string Number = Number0;
  int k = 2;
  while((int)Number.size() < (int)atoi(argv[1])){
    k++;
    Number = NumberAdder(Number0, Number1);
    Number0 = Number1;
    Number1 = Number;
  }
  cout << "Aha, the sequence goes above " << atoi(argv[1]) <<
  " digits after " << k << " terms." << endl;
  return 0;
}
