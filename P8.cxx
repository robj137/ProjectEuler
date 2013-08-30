void P8()
{
  int aray[1000];
  int k = 0;
  ifstream in("P8.txt");
  int val;
  double maxProduct = 0;
  double Product = 0;
  for(k = 0; k<1000; k++){
    in >> val;
    aray[k] = val;
  }
  for(int k = 0; k<=995; k++){
    Product = 1;
    for(int j = 0;j<5; j++){
      Product *= aray[k+j];
    }
    if(Product > maxProduct) maxProduct = Product;
  }
  cout << "the max product is " << maxProduct << endl;
}
