// Find sum of all the even valued terms in the fibonacci sequence which do not
// exceed 4e6
{
  
  std::vector<int> vec;
  vec.push_back(1);
  vec.push_back(1);
  int temp = 0;
  int sum = 0;
  int TotalSum = 2;
  while(vec[vec.size()-1] < 4e6){
  vec.push_back(vec[vec.size()-1] + vec[vec.size()-2]);
  if(vec[vec.size()-1]%2 == 0) sum += vec[vec.size()-1];
  TotalSum += vec[vec.size()-1];
  cout << vec[vec.size()-1] << endl;
  }
  cout << "Total Sum: " << TotalSum << endl;
  cout << "Even Sum: " << sum << endl;
}
