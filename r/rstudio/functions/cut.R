indices = 1:100

kfold = cut(indices, breaks = 5, labels = FALSE)

for (k in 1:5) {
  fold_incices = which(kfold == k)
}
