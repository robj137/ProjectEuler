void P6(int N)
{
  double sumSquare = 0;
  double squareSum = 0;
  for(int k = 0; k<=N; k++){
    sumSquare += pow(k,2);
    squareSum += k;
  }
  squareSum *= squareSum;
  cout << "Sum of Squares for " << N << " is " << sumSquare << endl;
  cout << "Square of Sums for " << N << " is " << squareSum << endl;
  cout << "Thus the difference is " << squareSum - sumSquare << endl;
}
