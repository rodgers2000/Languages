Person <- R6Class("Person", list(
  name = NA, 
  age = NA, 
  initialize = function(name, age) {
    self$name = name
    self$age = age
  }
))

michael <- Person$new("Michael", age = 22)