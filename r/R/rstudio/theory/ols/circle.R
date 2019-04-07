library(tidyverse)
m = 200
t = seq(0, 1, length.out = m)
x = sin(2*pi*t) + .8*rnorm(m)
y = cos(2*pi*t) + 2*rnorm(m)

X = cbind(2*x, 2*y, 1)
Y = x^2 + y^2

beta = solve(t(X) %*% X) %*% t(X) %*% Y

print(beta)

r = sqrt(beta[3] + beta[1]^2 + beta[2]^2)

xxxx = beta[1] + r*sin(2*pi*t)
yyyy = beta[2] + r*cos(2*pi*t)


beta = solve(t(x) %*% x) %*% t(x) %*% y
yy = x %*% beta

xpoly = cbind(x, x^2, x^3, x^4, x^5, x^6)
beta = solve(t(xpoly) %*% xpoly) %*% t(xpoly) %*% y
yyy = xploy %*% beta

my_dat = data.frame('xcirc'=xxxx, 'ycirc'=yyyy, 'x'=x, 'y'=y, 'ylin'=yy, 'ypoly' = yyy)

ggplot(my_dat, aes(x=x, y=y)) + geom_point() + 
  geom_point(aes(x=xcirc, y=ycirc), color='cornflowerblue') + 
  geom_line(aes(x=x, y=ylin), color='springgreen') +
  labs(title='OLS Geometry Fitting')