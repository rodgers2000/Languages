X = data.frame(matrix(rnorm(1000), nrow = 100))

impute = preProcess(X, method = "pca")
X = predict(impute, newdata = X)
head(X)
