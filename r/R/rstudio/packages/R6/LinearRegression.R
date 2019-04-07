library(R6)

LinearRegression = R6Class("LinearRegression", list(
  loss = c(),
  weights = NA,
  intercept = NA,
  X = NA,
  Y = NA, 
  initialize = function(X, Y) {
    self$X = X
    self$Y = Y
    self$weights = array(0, dim = c(dim(X)[2], dim(Y)[2]))
    self$intercept = vector("double", length = ncol(X))
  },
  Yhats = function() {
    preds = self$X %*% self$weights + self$intercept
    return(preds)
  }, 
  Optimize = function(n_iters, learning_rate) {
  for (iter in 1:n_iters) {
    self$loss = c(1 / nrow(self$X) * sum((self$Y - self$Yhats())^2), self$loss)
    self$weights = self$weights  - learning_rate * 1 / nrow(self$X) * t(self$X) %*% (self$Yhats() - self$Y)
    self$intercept = self$intercept - learning_rate * 1 / nrow(self$X) * sum(self$Yhats() - self$Y)
  } 
  }
))

n = 50

X = matrix(0, nrow = n, ncol = 5)
for (col in 1:5) {
  X[, col] = rnorm(n)
}
Y = matrix(c(rnorm(n), rnorm(n)), ncol = 2)

mjr = LinearRegression$new(X, Y)
mjr$Optimize(150, .1)
mjr$weights
mjr$intercept
mjr$loss
