{
  int dDay = 1;
  int sum = 0;
  int daylim = 31;
  for(int year = 1; year < 101; year++){
    for(int month = 1; month <= 12; month++){
      if(month == 2) daylim = 28;
      if(month == 2 && (year%4 == 0)) daylim = 29;
      if((month == 4) || (month == 6) || (month == 9) || (month == 11)) {
        daylim = 30;
      }
      for(int day = 1; day <= daylim; day++){
        dDay++;
        if(dDay%7 == 0 && (day == 1)) sum++;
      }
      daylim = 31;
    }
    if (year == 0) sum = 0;
  }
  cout << sum << endl;

}

