// find largest prime factor of 600851475143
{
  //
  ifstream in("Primes.txt");
  int value;
  long int N = 600851475143;
  long int H = 1;
  while(in){
    in >> value;
    if( N%value ==0){
      cout << value << endl;
      H *= value;
    }
  }
  cout << "H is " << H << " and remainder is " << 1.0*N/H << endl;;
}
