library(keras)
install_keras()

samples = 1000
timesteps = 5
input_features = 2
x_train = array(data = 0, dim = c(samples, timesteps, input_features)) # samples, timesteps, input_features
for (i in 1:samples) {
  for (t in 1:timesteps) {
    x_train[i, t, ] = rnorm(input_features)
  }
}
y_train = rnorm(samples)

model = keras_model_sequential() %>% 
  layer_simple_rnn(units = 1, input_shape = c(5, 2))

model %>% compile(
  optimizer = "rmsprop",
  loss = list("mean_squared_error"), 
  metrics = list("mean_squared_error")
)

history <- model %>% fit(
  x_train,
  y_train,
  epochs = 10,
  validation_split = 0.1,
  verbose = 1
)

