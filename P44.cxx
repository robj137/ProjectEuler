{

  vector<int> aray;
  for(int k = 1; k<5000; k++){
    aray.push_back(k*(3*k-1)/2);
  }

  int Ray[500][500] = {0};
  for(int k = 1; k<500; k++){
    cout << k << endl;
    for(int j = 1; j<k; j++){
      for(int m = 0; m<500; m++) {
        if(aray[m] == (aray[k] - aray[j])){
          Ray[k][j] += 1;
        }
        if(aray[m] == (aray[k] + aray[j])){
          Ray[k][j] += 2;
        }
      }
    }
  }

  for(int k = 0; k<500; k++){
    for(int l = 0; l<500; l++){
      if(Ray[k][l] ==3) cout << "oy " << k << "  " << l << endl;
    }
  }

}
