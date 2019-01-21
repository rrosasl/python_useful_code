#Creating Scatter plots

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.scatter(data = df, x = 'independent_var', y ='dependent_var')
plt.xlabel('independent_var')
plt.ylabel('dependent_var')
plt.show().

#in seaborn

sns.regplot(data = df, x = 'independent_var', y ='dependent_var')
plt.xlabel('independent_var')
plt.ylabel('dependent_var')
plt.show()

## For discrete relationships where a lot of data can be confusing
#Using jitter
sns.regplot(data = df, x = 'independent_var', y ='dependent_var', x_jitter = 0.3)

# using transparency
sns.regplot(data = df, x = 'independent_var', y ='dependent_var', scatter_kws = {'alpha': 1/20})
