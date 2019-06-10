#' A Location, Spread, Shape Calculation
#'
#' This function performs NA analysis and calculates basic statistics for any feature column. All you need is to imput tidy data.
#' @param tidy.df Is your data tidy? Defaults to the IRIS dataset
#' @keywords stats
#' @export
#' @examples
#' calc.location.spread.shape()

my.stats = function(col.vec) {
  # this allows for dates, characters, and factors to be in the calculation
  if (is.factor(col.vec)) {
    col.vec = as.double(col.vec)
  }
  if (is.character(col.vec)) {
    col.vec = as.double(as.factor(col.vec))
  }
  # number of obs
  n = length(col.vec)
  # location
  mean = mean(col.vec, na.rm = TRUE)
  min = min(col.vec, na.rm = TRUE)
  median= median(col.vec, na.rm = TRUE)
  max = max(col.vec, na.rm = TRUE)
  # spread 
  std = sd(col.vec, na.rm = TRUE)
  var = var(col.vec, na.rm = TRUE)
  # shape 
  skewness = moments::skewness(col.vec, na.rm = TRUE)
  kurtosis = moments::kurtosis(col.vec, na.rm = TRUE)
  # now we check for NA's
  n_na = sum(is.na(col.vec))
  prc_na = n_na / length(col.vec)
  # create df
  this_df = data.frame(n, n_na, prc_na, mean, min, median, max, std, var, skewness, kurtosis)
  return(this_df)
}

calc.location.spread.shape <- function(tidy.df = datasets::iris) {
  #############################
  # input a tidy data frame, a.k.a: obs x variables
  #############################
  # now the we apply this function to each column of numeric values
  results = apply(tidy.df, 2, my.stats)
  ###################################################################
  # now we tidy the data 
  ###################################################################
  features = length(results)
  feat.names = names(results)
  final.df = data.frame()
  for (layer0 in seq_along(results)) {
    # save the name of the feature 
    results[[layer0]]$feature = feat.names[layer0]
    # append it to the dataframe
    final.df = rbind(final.df, results[[layer0]])
  }
  # we want the feature, then stat
  final.df = final.df[, c(12, 1:11)]
  return(final.df)
}

# library(datasets)
# ds = cbind(iris[, 1:4], c(1:145, NA, NA, NA, NA, NA))
# colnames(ds) = c(colnames(iris)[-4], "last_col")
# 
# a = calc.location.spread.shape(vec)
