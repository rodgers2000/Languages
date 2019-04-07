library(datasets)
a = tapply(mtcars$wt, mtcars$cyl, mean)

a = data.frame("mean" = a)
a$id = row.names(a)
print(a)
