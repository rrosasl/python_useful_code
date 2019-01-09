import seaborn as sns
import matplotlib.pyplot as plt

#Bar Chart
sns.countplot(data = df, x = 'variable_to_plot');

#Color palette

sns.color_palette

#Plot bar chart with everything on same color
base_color = sb.color_palette()[0] #This would return a touple with all different types of colors. The [0] index is the blue
sns.countplot(data = df, x = 'variable_to_plot', color=base_color);

#to change order, e.g. largest to smallest
# order_df = df['variable_of_interest'].value_counts().index

sns.countplot(data = df, x = 'variable_to_plot', order = order_df);


#All togehter
sns.countplot(data = df, x = 'variable_to_plot', color=base_color, order = order_df);

# Unreadable labels
# Rotate labels

plt.xticks(rotation = 90)

# Or do it horizontal Just change X to Y
sns.countplot(data = df, y = 'variable_to_plot', color=base_color, order = order_df);

# bar chart proportion / relative frequency

## First we need to create the ticks

total_number = df.shape[0]
max_type_count = df['variable_of_interest'].value_counts()[0] #We do this to tell how long the bar chart should be
max_prop = max_type_count / total_number

tick_props = np.arange(0,max_prop,0.02) #move in intervals of 2%
tick_names = ['{:0.2f}.format(v) for v in tick_props]

plt.xticks(tick_props * total_number,tick_names) #We need to multiply to get the correct number
plt.xlabel('proportion')

#THis is for horizontal charts

#Add percentage text on on the bars
type_counts = df['variable_of_interest'].value_counts()
for i in range(type_counts.shape[0]):
	count = type_counts[i]
	pct_string = '{:0.1f}%.format(100*count/df.shape[0])
	plt.text(count +1, i, pct_str, va = 'center')
