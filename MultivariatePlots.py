
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#This code will show how to encode third variables without using positioning

# Using Shape (2 quant 1 categorical)
#Starting point: a scatter plot with 2 quantitative variables

sns.regplot(data = df, x = 'variable_1', y = 'variable_2', fit_reg = False)
plt.xlabel('variable_1')
plt.ylabel('variable_2')

#Adding shape
# To add shape we need to do it one by one, so we need a loop

ttype_markers = [['cat_1','o],['cat_2', '^']]

for ttype_marker in ttype_markers:
        plot_data = df.loc[df.variable_3 == ttype]

        sns.regplot(data = plot_data, x = 'variable_1', y = 'variable_2', fit_reg = False, marker = )
plt.xlabel('variable_1')
plt.ylabel('variable_2')
plt.legend(['cat_1','cat_2'])

# Changing size of Scatterplot
# Three quantitative variables

sns.regplot(data = df, x = 'variable_1', y = 'variable_2', fit_reg = False, scatter_kws = {'s': df['variable_3'/2]}) #The two in this case can be changed to adjust the size
plt.xlabel('variable_1')
plt.ylabel('variable_2')

## To create a legend of the bubble size

sizes = [200, 300, 500]
base_color = sns.color_palette[0]
legend_obj = []
for s in sizes:
    legend_obj.append(plt.scatter([],[], s = s/2, color = base_color))

plt.legend(legend_obj, sizes, title = 'variable_3')

#Working with colors

## Working with nominal variables
# A good way with seaborn is to use the Facet grid

g = sns.FacetGrid(data = df, hue = 'nominal_variable')
g.map(sns.regplot, 'variable_1','variable_2', fit_reg = False))

# Additionally you can change the hue order

g = sns.FacetGrid(data = df, hue = 'nominal_variable', hue_order = ['category_1','category_2'])
g.addlegend()
g.map(sns.regplot, 'variable_1','variable_2', fit_reg = False))

## Working with ordinal data (e.g. from low to high)
g = sns.FacetGrid(data = df, hue = 'ordinal_variable', palette = 'viridis_r' )
g.add_legend()
g.map(sns.regplot, 'variable_1','variable_2', fit_reg = False))

## Working with quantitative variables (FacetGrid hue expects categorical data)
plt.scatter(data = df, x = 'variable_1', y = 'variable_2', c = 'variable_3', cmap = 'viridis_r') #We use c = instead of hue
plt.colorbar (label = 'variable_3')

## Using facetting (multiple graphs side-by-sde)

g = sns.FacetGrid(data - df, col ='categorical_variable', row = 'variable_3', margin_title = True) #This last part makes the graph more readable. The 'row' is optional
g.map(plt.scatter, 'variable_1', 'variable_2')

# Using facetting with box plots
g = sns.FacetGrid(data = df, col = 'cat_var1', size = 4)
g.map(sns.boxplot, 'cat_var2', 'num_var2')
