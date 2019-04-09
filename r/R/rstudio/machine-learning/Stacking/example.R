mjr = list()
n = 100
p = 50
X = matrix(rnorm(n * p), nrow = n)
Y = rnorm(n)

reg = lm(Y ~ X)
preds = predict(reg, newdata = data.frame(X))
mse = mean((Y - preds)^2)
print(mse)