m = 10000 # * 10 
n = m / 100 * 10
labels = 0:1
X = c()
for (i in 1:10) {
  x = matrix(c(rnorm(m, 0, 1), 
           rnorm(m, 10, 5), 
           rnorm(m, 20, 1), 
           rnorm(m, 5, 20)), ncol = 4)
  X = rbind(X, x)
}
X_train = array(data = X, dim = c(n, 10, 10, 1))

Y_train = matrix(sample(labels, n, replace = TRUE), ncol = 1)

X = c()
for (i in 1:10) {
  x = matrix(c(rnorm(m, 0, 1), 
               rnorm(m, 10, 5), 
               rnorm(m, 20, 1), 
               rnorm(m, 5, 20)), ncol = 4)
  X = rbind(X, x)
}
X_test = array(data = X, dim = c(n, 10, 10, 1))

Y_test = matrix(sample(labels, n, replace = TRUE), ncol = 1)

library(keras)
# install_keras()

model <- keras_model_sequential() %>% 
  layer_conv_2d(filters = 32, kernel_size = c(3, 3), activation = "relu", 
                input_shape = c(10, 10, 1)) %>% 
  layer_max_pooling_2d(pool_size = c(2, 2)) %>% 
  layer_conv_2d(filters = 64, kernel_size = c(2, 2), activation = "relu") %>% 
  layer_conv_2d(filters = 128, kernel_size = c(1, 1), activation = "relu")

model <- model %>% 
  layer_flatten() %>% 
  layer_dense(units = 64, activation = "relu") %>% 
  layer_dense(units = 1, activation = "sigmoid")

model %>% compile(
  optimizer = optimizer_rmsprop(lr = .001), 
  loss = 'binary_crossentropy',
  metrics = 'accuracy'
)
# train 
history <- model %>% fit(
  X_train,
  Y_train,
  epochs = 50,
  batch_size = 10, 
  validation_split = 0.3,
  verbose = 1
)

model %>% evaluate(X_test, Y_test)
# model %>% predict(X_test)