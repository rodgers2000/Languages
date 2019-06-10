n = 1000
p = 50
X = data.frame(matrix(rnorm(n*p), nrow = n))
Y = sample(c(1, 2), size = n, replace = TRUE)
X_test = data.frame(matrix(rnorm(n*p), nrow = n))
Y_test = sample(c(1, 2), size = n, replace = TRUE)

Core = list()
Core$Train$X = X
Core$Train$Y = Y
Core$Test$X = X_test
Core$Test$Y = Y_test