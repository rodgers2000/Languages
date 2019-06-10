# generate data 
n1 = rnorm(100, 0, 1)
n2 = rnorm(100, 5, 1)
n3 = rnorm(100, 15, 1)

X = c(n1, n2, n3)

library(mclust)
# fit the gaussian mixture model
temp = Mclust(X, G = 1:9, modelNames = "E")

summary(temp)
temp$parameters
# fit the density 
x = seq(-5, 20, length.out = 200)
y = dens("V", x, parameters = temp$parameters)

plot(x, y)
