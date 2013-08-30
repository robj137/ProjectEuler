#include "IsPrime.cxx"
void P10(ULong64_t N)
{
  ULong_t sum = 2;
  double dsum = 0;
  for(ULong64_t k = 3; k<N; k+=2){
    if(IsPrime(k)) {sum += k;}
    if(k%10000 == 0) cout << "checking " << k << endl;
  }
  cout << "sum of all primes below " << N << " is " << sum << endl;
}

ULong64_t P10Sieve(ULong64_t N)
{
  bool array[2001000];
  int r = sqrt(N);
  for(int k = 0; k<2001000; k++){
    array[k] = false;
  }
  for(int k = 4; k<N/2; k++){
    array[2*k] = true;
  }
  for(int k = 3; k<r; k++){
    if(!array[k]){
      cout << k << endl;
      for(int l = k*k; l<N; l++){
        array[l] = true;
        l++;
      }
    }
    k++;
  }
  ULong64_t sum = 0;
  for(int n = 2; n<N; n++){
    if(!array[k]) {sum += n;}
  }
  return sum;
}
