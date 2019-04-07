# this is your numeric data
df = data.frame(1:10, (1:10)^2, rnorm(10))
# this is your labeled data
labels1 = sample(c("m", "r"), 10, replace = TRUE)
labels2 = sample(c("j", "s"), 10, replace = TRUE)
colnames(df) = letters[1:3]
# this is the functions you want to call for each column
my_stats <- function(x) {
  
  mean = mean(x)
  median = median(x)
  std = sd(x)
  
  number = c(mean, median, std)
  stat = c("mean", "median", "sd")
  
  return(data.frame(stat, number))
  }

# this is how we calculate the stats based on labels
my_tapply <- function(x) {
  tapply(x, labels1, my_stats)  
}

# this is how we apply the stats to each label for each column (notice the 2)!
a = apply(df, 2, my_tapply)

# export to dataframe now
my_df = data.frame()

layer0_names = names(a)
for (outer_index in seq_along(a)) {
  layer1 = a[[outer_index]]
  layer1_names = names(layer1)
  for (inner_index in seq_along(layer1)) {
    a[[outer_index]][[inner_index]]$feature = layer0_names[outer_index]
    a[[outer_index]][[inner_index]]$subgroup = layer1_names[inner_index]
    my_df = rbind(my_df, a[[outer_index]][[inner_index]])
  }
}


print(my_df)
