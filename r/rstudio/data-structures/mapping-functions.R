func1 <- function(a) {
  print(a)
}

func2 <- function(b) {
  print(b)
}

mjr = list(func1, func2)

for (i in 1:length(mjr)) {
  temp = mjr[[i]]
  temp(i)
}