library(caret)
n = 100
p = 50
X = matrix(rnorm(n * p), nrow = n)
Y = matrix(sample(c(1, 2), size = n, replace = TRUE))
# Y = matrix(rnorm(n), nrow = n)
# you feed the Y into data partition
indices = createDataPartition(Y, p = .8)

X_train = X[indices$Resample1]
Y_train = Y[indices$Resample1]
X_test = X[-indices$Resample1]
Y_test = Y[-indices$Resample1]
