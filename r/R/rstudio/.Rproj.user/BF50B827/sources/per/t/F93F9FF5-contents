x = seq(-50, 50, length.out = 1000)
func <- function(x) {
  y = x^2 + 100*cos(x)
  return(y)
}
plot(x, func(x))

gradient_approx <- function(func, x0, x1) {
  dy = func(x1) - func(x0)
  dx = x1 - x0
  return(dy/dx)
}

gradient_true <- function(x) {
  return(2*x - 100*sin())
}

x1 = 50
x2 = 50
learning_rate = .1
for (epoch in 1:10000) {
  x1 = x1 - learning_rate * gradient_approx(func, x1, x1 + rnorm(1))
  x2 = x2 - learning_rate * gradient_true(x2)
}

print(x1)
print(x2)
