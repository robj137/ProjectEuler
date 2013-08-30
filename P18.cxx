#include <math.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <iomanip>
#include <TH2D.h>
#include "TCanvas.h"
using namespace std;



void FillGrid(int *grid){
  int val;

  ifstream in("P18.txt");
  //TH2D h2("h2", "", 15, 0, 15, 15, 0, 15);
  for(int row = 0; row<15; row++){
    for(int col = 0; col< row+1;col++){
      in >> val;
      grid[15*row + col] = val;
     // if(val>60)h2.SetBinContent(col+1,14-row+1, val);
    }
  }
  //for(int row = 0; row<15; row++){
  //  for(int col = 0; col<15; col++){
  //    cout << setw(2) << grid[row][col] << " ";
  //  }
  //  cout << endl;
 // }
 // TCanvas *c1 = new TCanvas();
 // c1->SetLogz(0);
 // h2.SetStats(0);
 // h2.Draw("COLZ");
  //c1->Print("~/Desktop/temp.pdf");
  //c1->WaitPrimitive();
  //delete c1;
 // for(int col = 0; col <= 13; col++){
 //   cout << grid[13][col] + grid[14][col];
 //   cout << " vs. " <<  grid[13][col] + grid[14][col+1];
 //   cout << endl;
 // }

  
}

int MaxSumInefficient()
{
  int temp[15*15];
  FillGrid(temp);
  int grid[15][15];
  for(int k = 0; k<15; k++){
    for(int l = 0; l<k+1; l++){
      grid[k][l] = temp[15*k + l];
    }
  }
  
  for(int row = 0; row<15; row++){
    for(int col = 0; col<15; col++){
      cout << setw(2) << grid[row][col] << " ";
    }
    cout << endl;
  }
  
  int maxSum = 0;
  int sum = 0;
  int colsum = 0;
  for(col = 0; col<15; col++){
    for(row = 0; row<15; row++){
      
    }
  }
  return 1;
}

int main(int argc, char* argv[])
{
  MaxSumInefficient();
  return 1;
}
