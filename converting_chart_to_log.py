#How to convert x axis of a chart from linear to logarithmic

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Regular linear graph

bins = np.arange(0,df['colum_of_interest'].max()+10,10)
#will determine the bin size, from 0, to the max of the colum_of_interest +10, in 10 increments

plt.hist(data=df, x = 'colum_of_interest', bins = bins);
#We could also have done df['colum_of_interest'].hist()

#Change to logarithmic
plt.xscale('log')
plt.show()
#problem is that this graph uses default settings which could be hard to interpret

## determine what is the right logarithmic scale to to use as axis
#quick visual way
np.log10(df.colum_of_interest.describe())
#This will calculate the log base 10 of the descriptive statistics (e.g. min, max etc)
#programmatic way

log10_max = np.log10(df.colum_of_interest.max())
log10_min = np.log10(df.colum_of_interest.min())

#new bin sizes
bins = 10 ** np.arange(log10_min, log10_max + 0.1, 0.1) #change the 0.1 depending on the graph you see
#the ** means to the power of
plt.hist(data = df, x = colum_of_interest, bins = bins)
plt.xscale('log')
plt.show()
