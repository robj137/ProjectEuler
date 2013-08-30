#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
using namespace std;

int MaxColumn(int grid[],int);
int MaxRow(int grid[],int);

void P11()
{
  ifstream in("P11.txt");
  int grid[400];
  int k = 0;
  int val = 0;
  while(in){
    in >> val;
    grid[k] = val;
    k++;
  }
  cout << "Max of columns is " << MaxColumn(grid,400) << endl;
  cout << "Max of Rows is " << MaxRow(grid,400) << endl;
  // now shift left, col k shifts to the left k positions
  int gridL[400] = {0};
  int gridR[400] = {0};
  for(int row= 0; row<20; row++){
    for(int col = row; col<20; col++){
      gridL[row*20 + col] = grid[row*20+col-row];
    }
  }
  for(int row= 0; row<20; row++){
    for(int col = 0; col<20-row; col++){
      gridR[row*20 + col] = grid[row*20+col+row];
    }
  }
  //for(int row = 0; row<20; row++){
  //  for(int col = 0; col<20; col++){
  //    cout << setw(2) << gridR[row*20 + col] << " ";
  //  }
  //  cout << endl;
 // }
  cout << "Max of columns is " << MaxColumn(grid,400) << endl;
  cout << "Max of Rows is " << MaxRow(grid,400) << endl;
  cout << "Max of DiagL is " << MaxColumn(gridL,400) << endl;
  cout << "Max of DiagR is " << MaxColumn(gridR,400) << endl;
}



int MaxColumn(int grid[], int size)
{
  int MaxProd = 1;
  int prod = 1;
  for(int col = 0; col<(int)sqrt(size); col++){
    for(int row = 0; row<(int)sqrt(size)-3; row++){
      prod = 1;
      for(int k = 0; k<4; k++){
        prod *= grid[(int)sqrt(size)*row + col + (int)sqrt(size)*k];
        if(prod > MaxProd) {
          MaxProd = prod;
        }
      }
    }
  }
  return MaxProd;
}

int MaxRow(int grid[], int size)
{
  int prod = 1;
  int MaxProd = 1;
  for(int row = 0; row<(int)sqrt(size); row++){
    for(int col = 0; col<(int)sqrt(size)-3; col++){
      prod = 1;
      for(int k = 0; k<4; k++){
        prod *= grid[(int)sqrt(size)*row + col + k];
        if(prod > MaxProd){
          MaxProd = prod;
        }
      }
    }
  }
  return MaxProd;
}



int main(){
  P11();
  return 0;
}
