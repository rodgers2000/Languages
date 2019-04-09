for (i in 1:10) {
  mjr[[i]] = list()
  for (j in 1:5) {
    mjr[[i]][[j]] = lm(y ~ x)
  }
}

preds = list()
for (i in 1:10) {
  preds[[i]] = list()
  for (j in 1:5) {
    reg = mjr[[i]][[j]]
    preds[[i]][[j]] = predict(reg)
  }
}