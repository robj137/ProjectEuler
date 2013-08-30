#include "StringManipulation.cxx"

using namespace std;

int main(int argc, char* argv[]){
  if(argc != 2) {
    cout << "Just one argument pleae, the n^n of which you want the sum " << endl;
    cout << "of digits." << endl;
    return 0;
  }
  
  string value = "0";
  //for(int k = 1; k<=atoi(argv[1]); k++){
  //  cout << k << endl;
  //  value = NumberAdder(Exponentiate(k,itos(k)),value);
 // }
   string sum = "0";
  for(int k = 1; k<=atoi(argv[1]);k++){
    value = Exponentiate(k,itos(k));
    sum = NumberAdder(sum,value);
    //cout << value << endl;
  }
  cout << value << endl;
  cout << sum << endl;
  return 0;
}
