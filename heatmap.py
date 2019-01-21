#Doing a heatmap in python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Good for quatiative vs quantitative variable or good for discrete vs discrete
# Bin sizes are very important

plt.hist2d(data = df, x = 'independent_var', y = 'dependent_var')
plt.colorbar() # This will put on the right the legend that equates color with count
plt.xlabel('independent_var')
plt.ylabel('dependent_var')

#to establish minimum of counts to be colored

plt.hist2d(data = df, x = 'independent_var', y = 'dependent_var', cmin = 0.5)
#The 0.5 guarantees that there needs to be at least 1 count

# To chnage the color palette
plt.hist2d(data = df, x = 'independent_var', y = 'dependent_var', cmap = 'viridis_r')
#More colors in the documentation of hist2d

#Changing bin size
#Check what size is appropriate
df[['independent_var','dependent_var']].describe()

min_x = 0.6
max_x = 7 + 0.3
step_x = 0.3 
bins_x = np.arange(min_x, max_x, step_x)
bins_y = np.arange(min_y, max_y, step_y)
plt.hist2d(data = df, x = 'independent_var', y = 'dependent_var', bins = [bins_x, bins_y])
