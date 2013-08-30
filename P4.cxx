//find the largest palindromic # from the product of 2 3-digit numbers

int Reverse3(int N)
{
  if (N < 100 || N > 999 ){
    cout << "cry!" << endl;
    return -1;
  }
  int a, b, c;
  a = N/100;
  b = (N-100*a)/10;
  c = (N-100*a) - 10*b;

  return 100*c + 10*b + a;


}

int MakePalindrome(int N){
  if (N < 100 || N > 999 ){
    cout << "cry!" << endl;
    return -1;
  }
  return 1000*N + Reverse3(N);

}

void CheckNumber()
{
  for(int k = 100; k<1000; k++){
    for(int j = 100; j<1000; j++){
      if(MakePalindrome(k)%j ==0 && MakePalindrome(k)/j < 1000){
        cout << j << " is a factor in " << MakePalindrome(k) << endl;
      }
    }
  }

}

