n = 10000
m = 1000
labels = 0:9
X_train = matrix(c(rnorm(n, 0, 1), 
                   rnorm(n, 10, 5), 
                   rnorm(n, 20, 1), 
                   rnorm(n, 5, 20)), ncol = 4)

Y_train = matrix(sample(labels, n, replace = TRUE), ncol = 1)
# Y_train = matrix(c(sample(labels, n, replace = TRUE),
#                    sample(labels, n, replace = TRUE)), ncol = 2)

X_test = matrix(c(rnorm(m, 0, 1), 
                  rnorm(m, 10, 5), 
                  rnorm(m, 20, 1), 
                  rnorm(m, 5, 20)), ncol = 4)

Y_test = matrix(sample(labels, m, replace = TRUE), ncol = 1)
# Y_test = matrix(c(sample(labels, m, replace = TRUE),
#                   sample(labels, m, replace = TRUE)), ncol = 2)
library(keras)
install_keras()

# standardize data
X_train = scale(X_train)
X_test = scale(X_test)

model <- keras_model_sequential() 
model %>%
  layer_dense(units = 400, activation = 'relu',
              input_shape = dim(X_train)[2]) %>%
  layer_dense(units = 200, activation = 'relu') %>%
  layer_dense(units = 100, activation = 'relu') %>% 
  layer_dense(units = 50, activation = 'relu') %>% 
  layer_dense(units = 10, activation = 'softmax')

model %>% compile(
  optimizer = optimizer_rmsprop(lr = .001), 
  loss = 'sparse_categorical_crossentropy',
  metrics = 'accuracy'
)

model %>% fit(X_train, 
              Y_train, 
              epochs = 50,
              validation_split = 0.3)

score <- model %>% evaluate(X_test, Y_test)
probs <- model %>% predict(X_test)
yhats <- model %>% predict_classes(X_test)
