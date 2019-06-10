library(R6)

GaussianMixture <- R6Class("GaussianMixture", list(
  # data 
  univariate = NA, 
  mclustobj = NA, 
  modelName = NA, 
  attributes = list(),
  # methods
  initialize = function(univariate) {
    library(mclust)
    self$univariate = univariate
  },
  fitGMM = function(G = 1:9, modelNames = "V") {
    self$modelName = modelNames
    self$mclustobj = Mclust(data = self$univariate, 
                            G = G, 
                            modelNames = modelNames)
  }, 
  fitDensity = function(obs = 200) {
    x_min = min(self$univariate)
    x_max = max(self$univariate)
    x = seq(x_min, x_max, length.out = obs)
    probs = dens(self$modelName, x, parameters = self$mclustobj$parameters)
    # store data
    self$attributes$x = x 
    self$attributes$y = probs
  }
))

# generate data 
n1 = rnorm(100, 0, 1)
n2 = rnorm(100, 5, 1)
n3 = rnorm(100, 15, 1)

X = c(n1, n2, n3)

mjr = GaussianMixture$new(X)
mjr$fitGMM()
mjr$fitDensity()

df = data.frame(domain = mjr$attributes$x, probs = mjr$attributes$y)

library(ggplot2)
ggplot(df, aes(x=domain, y=probs)) + geom_point() + geom_line() + 
  labs(title = "GMM", x = "Domain (X)", y = "Probability")
