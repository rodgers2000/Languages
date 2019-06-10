library(caret)
library(tidyverse)

n = 50
p = 50

X = matrix(rnorm(n * p), ncol = n) %>% data.frame()
Y = sample(c(1, 2), n, replace = TRUE)

fitControl = trainControl(method = "none")

datControl = c("center", "scale")

gridControl = expand.grid(k = 2)

models = list()
model_index = 1
X1 = X
Y1 = Y

while (nrow(X1) > 1) {
  print(1)
  knn_fit = train(X1, factor(Y1), 
                  method = "knn", 
                  preProcess = datControl,
                  trControl = fitControl, 
                  tuneGrid = gridControl)
  
  Yhat = predict(knn_fit, newdata = X1)
  indices = Y1 != Yhat
  X1 = X1[indices, ]
  Y1 = Y1[indices]
  models[[model_index]] = knn_fit
  model_index = model_index + 1
}

preds = matrix(data = 0, nrow = n)
for (model in models) {
  Yhats = predict(model, X)
  preds = cbind(preds, Yhats)
}
preds = preds[,-1]

winners = c()

for (row in 1:nrow(preds)) {
  results = table(preds[row, ])
  winner = names(which.max(results))
  winners = c(winners, winner)
}

sum(Y == as.double(winners)) / length(Y)

knn_fit = train(X, factor(Y), 
                method = "knn", 
                preProcess = datControl,
                trControl = fitControl, 
                tuneGrid = gridControl)

Yhat = predict(knn_fit, newdata = X)
sum(Y == Yhat) / length(Y)
