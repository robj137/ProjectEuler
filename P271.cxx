/*
For a positive number n, define S(n) as the sum of the integers x, for which 1xn
and
x31 mod n.

When n=91, there are 8 possible values for x, namely : 9, 16, 22, 29, 53, 74,
79, 81.
Thus, S(91)=9+16+22+29+53+74+79+81=363.

Find S(13082761331670030).
*/
void S(ULong_t N)
{
  int sum = 0;
  for(int k = 2; k<N; k++){
    if((k*k*k)%N ==1) {
      cout << k << endl;
      sum += k;
    }
  }
  cout << "total SUm is " << sum << endl;

}
