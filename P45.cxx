bool IsInteger(double aVal)
{
  if(pow(aVal-(int)aVal,2) < 1e-12){
    return true;
  }
  return false;


}


// so need to have 1+sqrt(1-4j+12j^2) be an integer and divisible by 2


void P45(int first = 1, int last = 1000)
{
  double tocheck;
  long  number = 0;
  for(long  k = first; k<= last; k++){
    tocheck = 0.25*(1+sqrt(1-4*k + 12*k*k));
    if(IsInteger(tocheck)){
      number = k*(3*k-1)/2;
      cout << k << " checks out with number " << number << endl;
      cout << " and j is " << 0.25*(1+sqrt(1-4*k+12*k*k)) << endl;
    }

  }
}
