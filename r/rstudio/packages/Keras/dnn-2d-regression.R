# this is a tutorial to fit a deep neural network to predict a 2-dimensional vector of numbers

n = 10000
m = 1000
X_train = matrix(c(rnorm(n, 0, 1), 
             rnorm(n, 10, 5), 
             rnorm(n, 20, 1), 
             rnorm(n, 5, 20)), ncol = 4)

Y_train = matrix(c(rnorm(n, 5, 1),
                   rnorm(n, 10, 1)), ncol = 2)

X_test = matrix(c(rnorm(m, 0, 1), 
                   rnorm(m, 10, 5), 
                   rnorm(m, 20, 1), 
                   rnorm(m, 5, 20)), ncol = 4)

Y_test = matrix(c(rnorm(m, 5, 1), 
                  rnorm(m, 10, 1)), ncol = 2)

library(keras)
install_keras()

# standardize data
X_train = scale(X_train)
X_test = scale(X_test)

build_model <- function() {
  
  model <- keras_model_sequential() %>%
    layer_dense(units = 64, activation = "relu",
                input_shape = dim(X_train)[2]) %>%
    layer_dense(units = 32, activation = "relu") %>%
    layer_dense(units = 16, activation = "relu") %>% 
    layer_dense(units = 8, activation = "relu") %>% 
    layer_dense(units = 4, activation = "relu") %>% 
    layer_dense(units = 2, activation = "relu") %>% 
    layer_dense(units = 2)
  
  model %>% compile(
    loss = "mse",
    optimizer = "rmsprop",
    metrics = list("mean_squared_error")
  )
  
  return(model)
}

model <- build_model()
model %>% summary()

# Display training progress by printing a single dot for each completed epoch.
print_dot_callback <- callback_lambda(
  on_epoch_end = function(epoch, logs) {
    if (epoch %% 80 == 0) cat("\n")
    cat(".")
  }
)    

# train 
history <- model %>% fit(
  X_train,
  Y_train,
  epochs = 25,
  validation_split = 0.3,
  verbose = 1,
  callbacks = list(print_dot_callback)
)

model %>% evaluate(X_test, Y_test)
# model %>% predict(X_test)
