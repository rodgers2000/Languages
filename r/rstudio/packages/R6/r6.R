library(R6)

Test2 <- R6Class("Test2", 
                 public = list(
                   print_a = function() {
                     cat(self$a)
                   }
                 ))


Test <- R6Class("Test",
                inherit = Test2,
                public = list(
                  a = NA, 
                  b = NA,
                  initialize = function(a, b) {
                    self$a = a
                    self$b = b
                    cat('Welcome!!!')
                  },
                  print_data = function() {
                    cat(paste0('a = ', self$a, ' and b = ', self$b))
                  }
                ))

# note: you can get and set attributes without methods. this is cause of public
# note: you can use self.a on an inherited class. this is good
michael = Test$new(10, 69)
michael$a = 11
michael$print_data()
michael$print_a()

