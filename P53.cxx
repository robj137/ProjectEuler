{ 
  int sum = 0;
  for(int N = 1; N<=100; N++){
    for(int k =0; k<=N; k++){
      if(TMath::Binomial(N,k) > 1e6){
        sum++;
      }
    }
  }
  cout << sum << endl;
}
