# How to do violin plots

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Basic
sns.violinplot(data = df, x='categorical', y = 'quatiative') #x and y are the colum names

#ALl the same color

base_color = sns.color_palette()[0]
sns.violinplot(data = df, x='categorical', y = 'quatiative', color = base_color, inner = None)
plt.xticks(rotation = 15)
#inner = 'quartile' puts quartiles

# to change the order of the categories
sns.violinplot(data = df, x='categorical', y = 'quatiative', order = ["cat1","cat2","cat3"])

#box plot

base_color = sns.color_palette()[0]
sns.boxplot(data = df, x='categorical', y = 'quatiative', color = base_color)
plt.xticks(rotation = 15) #optional
