X = data.frame(matrix(rnorm(1000), nrow = 100))
Y = matrix(sample(c(1, 2), 100, replace = TRUE))

datControl = preProcess(X, method = c("center", "scale"))
X = predict(datControl, newdata = X)

fitControl = trainControl(method = "cv")
  
gridControl = expand.grid(k = 1:25)
  
knn_fit = train(X, factor(Y), 
                  method = "knn",
                  trControl = fitControl, 
                  tuneGrid = gridControl)
  
Yhat = predict(knn_fit, newdata = X)

sum(Yhat == Y) / length(Y)

mjr = confusionMatrix(factor(Y), Yhat, mode = "everything")
