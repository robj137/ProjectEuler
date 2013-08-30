ULong64_t P10Sieve(ULong64_t N)
{
  bool array[2001000];
  int r = sqrt(N);
  for(int k = 0; k<2001000; k++){
    array[k] = false;
  }
  for(int k = 4; k<N; k+=2){
    array[k] = true;
  }
  for(int k = 3; k<=r; k+=2){
    if(!array[k]){
      for(int l = k*k; l<N; l+=2*k){
        array[l] = true;
      }
    }
  }
  ULong64_t sum = 0;
  for(int n = 2; n<N; n++){
    if(!array[n]) {sum += n;}
  }
  for(int l = 0; l<20; l++){
  }
  return sum;

}
