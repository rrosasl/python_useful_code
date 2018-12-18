#This code will help remove all non-number characters chars from a column
#The column needs to be a string (obviously)
df['colum_x'] = df['colum_x'].str.replace(r'\D+', '') #the r'\D+' is something called regex
