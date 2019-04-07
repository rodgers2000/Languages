# this is a tutorial to fit a deep neural network to predict a 2-dimensional vector of numbers

n = 100000
m = 100000
samples = 1000
X_train = array(data = rnorm(n, 5, 1), dim = c(samples, 10, 10, 1))

Y_train = matrix(c(rnorm(samples, 5, 1),
                   rnorm(samples, 10, 1), 
                   rnorm(samples, 0, 1)), ncol = 3)

X_test = array(data = rnorm(m, 5, 1), dim = c(samples, 10, 10, 1))

Y_test = matrix(c(rnorm(samples, 5, 1), 
                  rnorm(samples, 10, 1), 
                  rnorm(samples, 0, 1)), ncol = 3)

library(keras)
install_keras()

model <- keras_model_sequential() %>% 
  layer_conv_2d(filters = 32, kernel_size = c(3, 3), activation = "relu", 
                input_shape = c(10, 10, 1)) %>% 
  layer_max_pooling_2d(pool_size = c(2, 2)) %>% 
  layer_conv_2d(filters = 64, kernel_size = c(2, 2), activation = "relu") %>% 
  layer_conv_2d(filters = 128, kernel_size = c(1, 1), activation = "relu")
  
  
model <- model %>% 
  layer_flatten() %>% 
  layer_dense(units = 64, activation = "relu") %>% 
  layer_dense(units = 3)
  
model %>% compile(
  loss = "mse",
  optimizer = optimizer_rmsprop(),
  metrics = list("mean_squared_error"))

# train 
history <- model %>% fit(
  X_train,
  Y_train,
  epochs = 25,
  batch_size = 10, 
  validation_split = 0.3,
  verbose = 1
)

model %>% evaluate(X_test, Y_test)
# model %>% predict(X_test)
