knn_caret <- function(X, Y) {
  fitControl = trainControl(method = "cv")
  
  gridControl = expand.grid(k = 1:25)
  
  knn_fit = train(X, factor(Y), 
                  method = "knn",
                  trControl = fitControl, 
                  tuneGrid = gridControl)
  return(knn_fit)
}

ada_caret <- function(X, Y) {
  fitControl = trainControl(method = "none")
  
  gridControl = expand.grid(method = "Adaboost.M1", nIter = 10)
  
  ada_fit = train(X, factor(Y), 
                  method = "adaboost",
                  trControl = fitControl, 
                  tuneGrid = gridControl)
  return(ada_fit)
}

lda_caret <- function(X, Y) {
  fitControl = trainControl(method = "none")
  
  lda_fit = train(X, factor(Y), 
                  method = "lda",
                  trControl = fitControl)
  return(lda_fit)
}

nb_caret <- function(X, Y) {
  fitControl = trainControl(method = "none")
  gridControl = expand.grid(laplace = 0, usekernel = TRUE, adjust = FALSE)
  
  nb_fit = train(X, factor(Y), 
                 method = "naive_bayes", 
                 trControl = fitControl, 
                 tuneGrid = gridControl)
}
