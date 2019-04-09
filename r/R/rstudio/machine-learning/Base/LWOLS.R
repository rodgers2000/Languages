n = 100
p = 1

X = seq(-3, 3, length.out = n)
Y = log(abs(X ^ 2 - 1) + .5)

radial_basis <- function(x, x0, sigma) {
  num = -1*(x - x0)^2
  den = 2*sigma^2
  return(num / den)
}

local_regression <- function(X, Y, x0, sigma = .01) {
  weights = c()
  for (x in X) {
    weights = c(weights, radial_basis(x, x0, sigma))
  }
  W = matrix(0, nrow = length(X), ncol = length(X))
  diag(W) = weights
  Beta = solve(t(X) %*% W %*% X) %*% t(X) %*% W %*% Y
  return(x0 %*% Beta)
}

preds = c()
for (x in X) {
  preds = c(preds, local_regression(X, Y, x, 100000))
}

library(ggplot2)

# R function

mjr = loess(Y ~ X, span = .1)
yhats = predict(mjr, X)

mjr = data.frame("X" = X, "Y" = Y, "LOESS" = yhats)
ggplot(mjr, aes(x = X)) + geom_point(aes(y = Y, color = "Truth")) + geom_point(aes(y = LOESS, color = "LOESS"))
