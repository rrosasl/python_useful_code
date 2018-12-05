#Find out ratio of missing values

df2 = []
df2 = df.isnull().sum() #This will create a dataframe with columns and their missing values
df2 = df2.reset_index()
df2['ratio_na'] = df2[0] / df.shape[0]
df2
