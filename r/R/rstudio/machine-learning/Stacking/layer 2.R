layer_2_old_data <- function(Core) {
  Models = list()
  Models[[1]] = nb_caret
  
  Trained_Models = list()
  Features = matrix(0, nrow = nrow(Core$Train$X), ncol = length(Models))
  
  for (i in 1:length(Models)) {
    Trained_Models[[i]] = Models[[i]](Core$Train$X1, Core$Train$Y)
    Features[, i] = predict(Trained_Models[[i]], newdata = Core$Train$X1)
  }
  Core$Train$X2 = data.frame(Features)
  Core$Models$Layer2 = Trained_Models
  return(Core)
}

layer_2_new_data <- function(Core) {
  Features = matrix(0, nrow = nrow(Core$Test$X), ncol = length(Core$Models$Layer2))
  for (i in 1:length(Core$Models$Layer2)) {
    Features[, i] = predict(Core$Models$Layer2[[i]], newdata = Core$Test$X1)
  }
  Core$Test$X2 = Features
  return(Core)
}
