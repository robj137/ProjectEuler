#include "StringManipulation.cxx"

using namespace std;

int main(int argc, char* argv[]){
  if(argc != 2) {
    cout << "Just one argument pleae, the exponent of the power of two" << endl;
    cout << "you want to sum the digits of." << endl;
    return 0;
  }

  string value = "1";
  for(int k = 0; k<atoi(argv[1]); k++){
    value = ComplexMultiply(value, "2");
  }
  cout << "Value is " << endl;
  cout << value << endl;
  cout << "and the sum of digits is " << DigitSum(value) << endl;
  return 0;
}
