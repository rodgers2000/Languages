library(R6)

Accumulator <- R6Class("Accumulator", list(
  sum = 0, 
  add = function(x = 1) {
    self$sum = self$sum + x
    # invisible(self)
  }
))

x = Accumulator$new()

x$add(10)$add(10)$sum
