// find largest prime factor of 600851475143
{
  //
  ifstream in("Primes.txt");
  int value;
  int array[10000];
  for(int k = 0; k<10000; k++){
    in >> value;
    array[k] = value;
  }
  int NN = array[9999];
  bool IsPrime = false;
  while(!IsPrime){
    NN++;
    IsPrime = true;
    for(int l = 0; l<10000; l++){
      if(NN%array[l] == 0) IsPrime = false;
    }
  }
  cout << NN << endl;

}
