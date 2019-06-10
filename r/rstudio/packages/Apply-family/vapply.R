mjr = list(1:10, 1:10, 1:10)

sapply(mjr, mean)

vapply(mjr, mean, FUN.VALUE = double(1))
