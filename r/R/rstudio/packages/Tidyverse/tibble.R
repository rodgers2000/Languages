library(tidyverse)
x = 1:10
y = x^2
df = tibble(x, y)

# tibbles are made this way. tibbles are list references 
# each column is put into a list
# list[1] points to a smaller list
# list[[1]] point to the data in the list
# that's why list[1, ] works and list[, 1] does not work

# loop for elements
for (row in 1:nrow(df)) {
  for (col in 1:ncol(df)) {
    cat(df[[row, col]], " ")
  }
  cat('\n')
}

# extract column vector
df$x
df[[1, ]]

# extract row, column tibble
df[1, ]
df[, 1]

# extract column
data = c()
for (row in 1:nrow(df)) {
  data = c(data, df[[row, 2]])
}
