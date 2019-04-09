layer_1_old_data <- function(Core) {
  Models = list()
  Models[[1]] = knn_caret
  Models[[2]] = ada_caret
  Models[[3]] = lda_caret
  Models[[4]] = nb_caret
  Models[[5]] = knn_caret
  Models[[6]] = lda_caret
  Models[[7]] = nb_caret
  Models[[8]] = ada_caret
  Models[[9]] = knn_caret
  Models[[10]] = ada_caret
  
  Trained_Models = list()
  Features = matrix(0, nrow = nrow(Core$Train$X), ncol = length(Models))
  
  for (i in 1:length(Models)) {
    Trained_Models[[i]] = Models[[i]](Core$Train$X, Core$Train$Y)
    Features[, i] = predict(Trained_Models[[i]], newdata = Core$Train$X)
  }
  Core$Train$X1 = data.frame(Features)
  Core$Models$Layer1 = Trained_Models
  return(Core)
}

layer_1_new_data <- function(Core) {
  Features = matrix(0, nrow = nrow(Core$Test$X), ncol = length(Core$Models$Layer1))
  for (i in 1:length(Core$Models$Layer1)) {
    Features[, i] = predict(Core$Models$Layer1[[i]], newdata = Core$Test$X)
  }
  Core$Test$X1 = data.frame(Features)
  return(Core)
}
