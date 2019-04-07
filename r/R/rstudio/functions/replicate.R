xx <- faithful$eruptions
fit1 <- density(xx)
fit2 <- replicate(1000, {
  x <- sample(xx, replace = TRUE)
})


