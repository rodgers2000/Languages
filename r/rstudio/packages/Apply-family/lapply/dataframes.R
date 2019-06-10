dfs = vector("list", length = 5)

for (i in 1:5) {
  a = rnorm(10)
  b = rnorm(10)
  dfs[[i]] = data.frame(a, b)
}

do.call(rbind, dfs)
