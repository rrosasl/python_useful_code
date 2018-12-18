#Couple ways to change values in pandas dataframe

#Mode number 1
old_value = 10 #Example
mask = df['column_x'] == 'value_of_interest' #Find the index of the value you want to change
column_name = 'column_y' #Name of the column where you want the value changed
df.loc[mask,column_name] = old_value * 20 #Change the value however you want

#Mode number2

old_value = 10
new_value = old_value * 20
df[df.column_x == 'value_of_interest'] = df[df.column_x == 'value_of_interest'].replace(old_value,new_value)
