mjr = list()

for (i in 1:10) {
  mjr[[i]] = list()
  for (j in c('a', 'b', 'c')) {
    mjr[[i]][[j]] = 1
  }
}

for (i in 1:10) {
  mjr[[paste0(i)]] = list()
  for (j in c('a', 'b', 'c')) {
    mjr[[paste0(i)]][[j]] = 1
  }
}

str(mjr)

mjr = list()

mjr$parameters$ahead = 1 
mjr$parameters$time = 5
mjr$parameters$yolo = 10

mjr$Train$X = 1
mjr$Train$Y = 5

str(mjr)
