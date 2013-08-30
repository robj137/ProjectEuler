void P9()
{
  for(int a = 0; a<1000; a++){
    for(int b = 0; b<1000; b++){
      if(1e6-2e3*(a+b)+2*a*b == 0 && b > a && a > 0){
        cout << "huzzah!  a = " << a << " and b = " << b << endl;
        cout << "hence abc = " << a*b*(1000-a-b) << endl;
      }
    }
  }

}
