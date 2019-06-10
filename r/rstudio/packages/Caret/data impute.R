X = data.frame(matrix(rnorm(1000), nrow = 100))

X[1, 1] = NA
X[1, 2] = NA

impute = preProcess(X, method = "knnImpute")
X = predict(impute, newdata = X)
head(X)
