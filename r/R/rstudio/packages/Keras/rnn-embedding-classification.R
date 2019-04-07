library(keras)
install_keras()

max_features = 10000
maxlen = 20

imdb = dataset_imdb(num_words = max_features)
c(c(x_train, y_train), c(x_test, y_test)) %<-% imdb

# input m sentences each with 20 words
x_train = pad_sequences(x_train, maxlen = maxlen)
x_test = pad_sequences(x_test, maxlen = maxlen)

model <- keras_model_sequential() %>% 
  # 10,000 words in the dictionary
  # a 10 dimensional dictionary lookup
  layer_embedding(input_dim = 10000, output_dim = 10, input_length = maxlen) %>% 
  # look up the sentence. it'll give a n_word x 10 vector
  # it trains the 10000 x 10 matrix of parameters
  layer_flatten() %>% 
  # flatten the vector
  layer_dense(units = 1, activation = "sigmoid")
  # this is a binary classification, so units = 1 

model %>% compile(
  optimizer = "rmsprop",
  loss = "binary_crossentropy", 
  metrics = c("acc")
)

history = model %>% fit(
  x_train, y_train,
  epochs = 2, 
  batch_size = 32, 
  validation_split = 0.2
)
