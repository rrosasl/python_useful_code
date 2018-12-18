#Want all values in the column to have the same length?
#.pad can help add additional values to the left to achieve a specific number of character

df['column_x'] = df['column_x'].str.pad(5,fillchar='0') #5 is the number of characters you want to have
#fillchar says what you want to replace it wit
