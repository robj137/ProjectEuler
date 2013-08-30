#include "StringManipulation.cxx"

using namespace std;

int main(int argc, char* argv[]){
  if(argc != 2) {
    cout << "Just one argument please, i.e. how far up to look for palindromes" << endl;
    return 0;
  }
  
  int N = atoi(argv[1]);
  int sum = 0;
  for(int k = 0; k<N; k++){ 
    if(IsAPalindrome(k, "decimal") && IsAPalindrome(k, "binary")){
      cout << GetDecimalString(k) << " " << GetBinaryString(k) << endl;
      sum += k;
    }
  }
  cout << "Sum of doubly palindromic numbers from 1 to " << N << " is " << sum
  << endl;
  return 0;
}
