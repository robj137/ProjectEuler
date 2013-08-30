bool GetAbundance(int val);
bool IsAbundant(int val);
void GetSumOfProperFactors(int num);

void P23()
{
  int sum = 0;
  for(int k = 1; k<= 28123; k++){
    if(NoAbundantSums(k)){
      sum += k;
    }
  }
  cout <<"sum is " <<  sum << endl;

}

bool NoAbundantSums(int val){
  for(int k = 1; k<=val/2; k++){
    if(GetAbundance(k) && GetAbundance(val-k)){
      //cout << k << endl;
      return false;
    }
  }
  return true;
}


bool GetAbundance(int val){
  static int  aray[28124] = {0};
  static bool first = true;
  if(first){
    int sum = 0;
    for(int k = 1; k<=28123; k++){
      sum = 0;
      for(int l = 1; l<=k/2; l++){
        if(k%l == 0) {
          sum += l;
        }
      }
      if (sum > k) aray[k] = 1;
    }
    first = false;
    cout << "finished filling array " << endl;
  }
  return (bool)(aray[val]);
}

