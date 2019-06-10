Core = layer_1_old_data(Core)
Core = layer_2_old_data(Core)
Core = layer_1_new_data(Core)
Core = layer_2_new_data(Core)

sum(Core$Test$X2 == Core$Test$Y) / length(Core$Test$Y)

model = knn_caret(Core$Train$X, Core$Train$Y)
yhats = predict(model, newdata = Core$Test$X)

sum(yhats == Core$Test$Y) / length(Core$Test$Y)
