bool IsPrime(ULong64_t n)
{
  if(n == 1) { return false; }
  if(n <4) { return true; }
  if(n%2 == 0) { return false; }
  if(n<9) { return true; }
  if(n%3 == 0) { return false; }
  ULong64_t r = sqrt(n);
  ULong64_t f = 5;
  while(f<=r){
    if(n%f == 0) { return false; }
    if(n&(f+2) == 0) { return false; }
  f+=6;
  }
  return true;
}
