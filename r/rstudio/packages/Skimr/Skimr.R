library(skimr)

X = data.frame(matrix(rnorm(1000), nrow = 100))
colnames(X) = 1:10

mjr = skim_to_wide(X)

mjr$variable

# NICE!!!!