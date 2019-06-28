a = as.Date("2000-09-06")
a + 1

a = strptime("2010-01-15 13:55:23.975", format="%Y-%m-%d %H:%M:%OS")
options(digits.secs = 3)


mjr = list()
for (i in 1:10){
  mjr[[paste(i)]] = rnorm(1)
}  

for (i in names(mjr)) {
  print(mjr[[i]])
}
if (sum(names(mjr) %in% 11) == 0) {
  mjr[[paste(11)]] = 69
}

