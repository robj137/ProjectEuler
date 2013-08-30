{

  //require that P = a+b +- sqrt(a*a + b*b)a
  double b = 0.0;
  int Pval[1000] = {0};
  for(int P = 2; P<=1000; P++){
    Pval[P-1] = 0;
    for(int a = 1; a<P; a++){
      b = 0.5*P*(P-2*a)/(P-a);
      if( sqrt(pow(b - (int)b,2)) < 1e-7 && (int)b > 0){
        Pval[P-1]++;
      }
    }
    Pval[P-1] /=2;

  }
}
