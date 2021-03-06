#include "Rcpp.h"
using namespace Rcpp;

//[[Rcpp::export]]         
NumericVector func1(NumericVector x){
  NumericVector a(x.size());
  for (int i = 0; i < x.size(); i++) {
  a[i] = x[i];
  }
  return a;
}
//[[Rcpp::export]]
NumericMatrix func2(NumericMatrix df){
  NumericMatrix my_matrix(df.nrow(), df.ncol());
  for (int col = 0; col < df.ncol(); col++) {
    for (int row = 0; row < df.nrow(); row++) {
      my_matrix(row, col) = df(row, col);
    }
  }
  return my_matrix; 
}


