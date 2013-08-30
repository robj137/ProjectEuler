// find largest prime factor of 600851475143
void FindPrimeFactors(int N)
{
  //
  ifstream in("Primes.txt");
  
  int value;
  while(in){
    cout <<
    in >> value;
    if(value>sqrt(N)) break;
    if( N%value ==0){
      cout << value << endl;
    }
  }
}

