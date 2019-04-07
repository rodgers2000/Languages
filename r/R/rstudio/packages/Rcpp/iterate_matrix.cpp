#include <Rcpp.h>
using namespace Rcpp;
using namespace std; 

// This is a simple example of exporting a C++ function to R. You can
// source this function into an R session using the Rcpp::sourceCpp 
// function (or via the Source button on the editor toolbar). Learn
// more about Rcpp at:
//
//   http://www.rcpp.org/
//   http://adv-r.had.co.nz/Rcpp.html
//   http://gallery.rcpp.org/
//

// [[Rcpp::export]]
void PrintMatrix(NumericMatrix X) {
  int ncol = X.ncol();
  int nrow = X.nrow();
  for (int i = 0; i < ncol; i++) {
    for (int j = 0; j < nrow; j++) {
      cout << X(i, j) << endl; 
    }
  }
}


// You can include R code blocks in C++ files processed with sourceCpp
// (useful for testing and development). The R code will be automatically 
// run after the compilation.
//
