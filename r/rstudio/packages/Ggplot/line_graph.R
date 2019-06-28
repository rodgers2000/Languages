library(ggplot2)

X = rnorm(100)
Y = sample(c(0, 1), 100, replace = TRUE)

mjr = data.frame('x' = 1:100, 'y' = X, 'color' = factor(Y))

ggplot(mjr, aes(x=x, y=y, color=color)) + geom_point() + geom_line()
