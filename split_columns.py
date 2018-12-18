#First method: in this case the values were in this format "2u - 4u" which was a range
#I wanted to have two columns, one with 2u and one with 4u
#Create two new columns by separating the string, mind the space in ' - '. the 1 in .split tells how many splits should there be.
#For me it made no difference if I used the 1, but since its in the solution I will leave it
#Without the .str at the end it returns an error. not sure why

df['new_column_1'],df['new_column_2'] = df['old_column'].str.split(' - ',1).str
