n = 10000
m = 1000
X_train = matrix(c(rnorm(n, 0, 1), 
                   rnorm(n, 10, 5), 
                   rnorm(n, 20, 1), 
                   rnorm(n, 5, 20)), ncol = 4)

Y_train = matrix(c(rnorm(n, 5, 1),
                   rnorm(n, 10, 1)), ncol = 2)

X_test = matrix(c(rnorm(m, 0, 1), 
                  rnorm(m, 10, 5), 
                  rnorm(m, 20, 1), 
                  rnorm(m, 5, 20)), ncol = 4)

Y_test = matrix(c(rnorm(m, 5, 1), 
                  rnorm(m, 10, 1)), ncol = 2)

reg = lm(Y_train ~ X_train)
yhats = predict(reg, data.frame(X_test))
