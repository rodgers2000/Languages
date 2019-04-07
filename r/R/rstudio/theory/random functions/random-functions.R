linear <- function(a, b, x) {
  return(a * x + b)
}

x = seq(1, 100, by = .25)
p = 20
a = rnorm(p, 20, 5)
b = rnorm(p, 20, 5)

Y = c()
for (i in 1:p) {
  temp = linear(a[i], b[i], x)
  Y = c(Y, temp)
}

Labels = c()
label = 1
for (i in 1:(p*length(x))) {
  if (i %% length(x) == 0) {
    label = label + 1
  }
  Labels = c(Labels, label)
}
X = rep(x, p)
df = data.frame(X = X, Y = Y, Labels = factor(Labels))

library(ggplot2)

ggplot(df, aes(x = X, y = Y, color = Labels)) + geom_point()
