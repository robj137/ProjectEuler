

void some()
{

}

int GetFactorialRemainder(int num, int index){
  int ret = 0;
  if(index == 0) return 1;
  while(num > 0){
    num -= TMath::Factorial(index);
    ret++;
  }
  ret--;
  return ret;
}

unsigned int GetFactoradic(int num){
  unsigned int ret = 0;
  num++;
  /// assume < 10 digits
  for(int k = 10; k>0; k--){
    ret += (int)pow(10,k)*GetFactorialRemainder(num,k);
    num -= GetFactorialRemainder(num,k)*TMath::Factorial(k);
  }
  return ret;

}
