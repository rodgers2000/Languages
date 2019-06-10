library(readr)
files = list.files("data")

Data = lapply(paste0("data/", files), read_csv)
names(Data) = 1:length(Data)

files = stringr::str_sub(files, 2, 5)

for (i in 1:length(Data)) {
  temp_df = Data[[i]]
  ticker = rep(files[i], nrow(temp_df))
  temp_df$ticker = ticker
  Data[[i]] = temp_df
}

# QUEEN LOLA
# now we have labels for the points!

NewData = data.frame()

for (i in 1:length(Data)) {
  temp_df = Data[[i]]
  NewData = rbind(NewData, temp_df)
}
