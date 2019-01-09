import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Most basic method
df.hist()

#With matplotlib
plt.hist(data = df, x = 'variable_of_interest') #By default there will be 10 bins

#Change bins parameter
plt.hist(data = df, x = 'variable_of_interest', bins = 20)

# Align bin size with tickmarks
 bins = np.arange(0,df['variable_of_interest'].max() + 5, 5)
  # The plus five is to make sure that all values are represented
  # The 5 at the end reflects the bin size

plt.hist(data = df, x = 'variable_of_interest', bins = bin)

#Seaborn also has its own way with more default bins
sns.distplot(df['variable_of_interest'])
    # Without density curve
    sns.distplot(df['variable_of_interest'],kde= False) #Kde stands for kernel density
