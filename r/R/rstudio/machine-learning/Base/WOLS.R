# weighted linear regression

Book = list()
Book$n = 100
Book$p = 1
Book$X = matrix(rnorm(Book$n*Book$p), nrow = Book$n)
Book$X_test = matrix(rnorm(Book$n*Book$p), nrow = Book$n)
Book$Y = matrix(rnorm(Book$n), nrow = Book$n)
Book$Y_test = matrix(rnorm(Book$n), nrow = Book$n)
Book$B = matrix(rnorm(Book$p), nrow = Book$p)
Book$W = matrix(0, nrow = Book$n, ncol = Book$n)
diag(Book$W) = 1

run <- function(Book, reps = 10){
  for (rep in 1:reps) {
    Book$B = solve(t(Book$X) %*% Book$W %*% Book$X) %*% t(Book$X) %*% Book$W %*% Book$Y
    temp_W = c()
    for (i in 1:Book$n) {
      p = Book$Y[i] - Book$X[i, ] %*% Book$B
      w = 1 / abs(p)
      temp_W = c(temp_W, 1/w)
    }
    diag(Book$W) = temp_W
  }
  return(Book)
}

mjr = run(Book, reps = 1000)
diag(mjr$W)
mjr$B
mjr$yhat = mjr$X_test %*% mjr$B

B = solve(t(mjr$X) %*% mjr$X) %*% t(mjr$X) %*% mjr$Y
OLS = mjr$X_test %*% B


A = data.frame("WOLS" = mjr$yhat, "Y" = mjr$Y_test, "X" = mjr$X_test, "OLS" = OLS)

library(ggplot2)

ggplot(A, aes(x = X)) + geom_point(aes(y = Y, color = "Truth")) + 
  geom_point(aes(y = WOLS, color = "WOLS")) + 
  geom_point(aes(y = OLS, color = "OLS"))
