a = data.frame('col1' = c(1, 2, 3, 4), 'col2' = c('a', 'b', 'c', 'd'))
b = data.frame('col1' = c(5, 6, 1, 2), 'col3' = c('e', 'f', 'g', 'h'))

merge(a, b, by.x = 'col1') # inner
merge(a, b, by.y = 'col1') # inner
merge(a, b, all = TRUE) # outer
merge(a, b, all.x = TRUE) # left
merge(a, b, all.y = TRUE) # right 
