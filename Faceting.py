# Faceting helps create multiple graphs side by side

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

g = sns.FacetGrid(data = df, col = 'column_1')
# In this case column_1 is categorical and this will create one graph for each category

g.map(plt.hist, 'column_2')

#If there are too many graphs horizontally it can be tricky
# For this reason we can force the new graphs to go to a new role

g.map(plt.hist, 'column_2', col_wrap = 3) # This means that after 3 graphs the new one will go into a new column 

#If you want the graphs to have DIFFERENT Y axis

g.map(plt.hist, 'column_2', sharey = False)
