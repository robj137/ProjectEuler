#include <math.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>


using namespace std;

int FindPrimes(int N)
{

  ifstream in("Primes.txt");
  vector<int> primes;
  int val;
  while(in){
    in >> val;
    primes.push_back(val);
  }
  int Na = N;
  vector<int> Nprimes;
  int k = 0;
  bool isPrime = true;
  while(primes[k]<((N/2)+1) && k < 10000){
    if(Na%primes[k] == 0){
      Nprimes.push_back(primes[k]);
      isPrime = false;
      Na /= primes[k];
      k--;
    }
    if(Na == 1) break;
    k++;
  }
  if(isPrime) {
    Nprimes.push_back(N);
  }
  map<int,int> rprimes;
  map<int,int>::iterator iter;
  for(int l = 0; l<Nprimes.size(); l++){
    iter = rprimes.find(Nprimes[l]);
    if(iter == rprimes.end()){
      rprimes.insert(pair<int,int>(Nprimes[l],1));
    } else {
      rprimes[Nprimes[l]] += 1;
    }
  }
  //cout << rprimes.size() << endl;
  double prod = 1;
  for( iter = rprimes.begin(); iter != rprimes.end(); ++iter){
    prod *= ((*iter).second+1);
  }
  return prod;
  //cout << prod << " factors" << endl;
} 

void GetMaxFactors(int N)
{
  int value;
  int MaxValue = 0;
  for(int k = 0; k<=N; k++){
    value = FindPrimes((int)(k*(k+1)/2.0));
    if(value > MaxValue) MaxValue = value;
    if(MaxValue > 500) {
      cout << MaxValue << " at " << k << endl;
      break;
    }
  }
  cout << "max is " << MaxValue << endl;
}

int main(int argc, char* argv[])
{

  GetMaxFactors((int)atoi(argv[1]));
  return 1;
}
