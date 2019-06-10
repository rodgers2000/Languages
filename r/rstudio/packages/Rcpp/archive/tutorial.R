library(Rcpp)

func1(1:10)

my_df = data.frame('a' = 1:10, 'b' = (1:10)^2, 'c'=rnorm(10))
my_df = as.matrix(my_df)

func2(my_df)
