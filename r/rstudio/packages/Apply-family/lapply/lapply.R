my_list = list(1:10, (1:10)^2)
names(my_list) = letters[1:2]

lapply(my_list, sum)
sapply(my_list, sum)
a = vapply(my_list, sum, vector("double", 1))

data.frame(a)
