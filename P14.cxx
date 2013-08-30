void P14()
{
  ULong_t maxLength = 0;
  ULong_t length = 0;
  ULong_t maxK = 0;
  for(int k = 1; k<1e6; k++){
    if(k%10000 == 0) cout << k << endl;
    length = GetSequenceLength(k);
    if(length>maxLength){
      maxLength = length;
      maxK = k;
      cout << "Found new Maximum: " << maxLength << " from starting point " << k
      << endl;
    }
  }

}

ULong_t GetSequenceLength(int N)
{
  int k = 1;
  ULong_t n = (ULong_t)N;
  while(n != 1){
    GetNextTermInSequence(n);
    k++;
  }
  return k;
}

void GetNextTermInSequence(ULong_t &N)
{
  if( N%2==0 ){
    N /=2;
  } else {
    N*=3;
    N+=1;
  }
}
