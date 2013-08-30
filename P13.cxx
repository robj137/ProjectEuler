void P13()
{
  ifstream in("P13.txt");
  int aRay[50][100];
  int answer[50];
  double sum = 0;
  int val = 0;
  for(int row = 0; row<100; row++){
    for(int col = 0; col<50; col++){
      in >> val;
      aRay[49-col][row] = val;
      // so in the array, the LSF is now on the left
    }
  }
  int colsum = 0;
  int carryover = 0;
  int answerindex = 0;
  for(int col = 0; col<50; col++){
    colsum = carryover;  carryover = 0;
    for(int row = 0; row<100; row++){
      colsum += aRay[col][row];
    }
    answer[col] = colsum%10;
    carryover = (colsum/10);
  }
  cout << carryover;
  for(int col = 49; col>=0; col--){
    cout << answer[col];
  }
  cout << endl;
  //for(int k = 49; k>-1; k--) {
  //  cout << answer[k];
 // }
 // cout << endl;

}

