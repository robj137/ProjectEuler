// Find sum of all natural numbers below 1000 that are multiples of 3 or 5
{
  int val = 0;
  int total = 0;
  for(int k = 0; k<1000; k++){
    if( (k%3==0) || (k%5==0)){
      val += k;
    }
    total += k;
  }

}
