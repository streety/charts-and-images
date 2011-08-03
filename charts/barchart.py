import csv
import numpy as np
import matplotlib.pyplot as plt

# Data
controlMeans = (-477.6308229, 0.0, -27.88604384)
controlStd = (372.4811512, 0.0, 27.88604384)

hdoseMeans = (56118.8384, 912.78521, 21467.92518)
hdoseStd = (2016.157542, 842.2364632, 6382.225045)


N = 3               # the number of groups
ind = np.arange(N)  # the x locations for the groups
width = 0.4         # the width of the bars

# Setup the figure
fig = plt.figure()
ax = fig.add_subplot(111)

# Plot the data
rectsc = ax.bar(ind, controlMeans, width, color='#ffffff', yerr=controlStd, ecolor='black')
rectsh = ax.bar(ind+width, hdoseMeans, width, color='black', yerr=hdoseStd, ecolor='black')

ax.set_ylabel('Response', size='x-large')

ax.set_xticks(ind+width)
ax.set_xticklabels( ('Group 1', 'Group 2', 'Group 3'), size='x-large' )

# Remove the surrounding lines from the plot
for loc, spine in ax.spines.iteritems():
    if loc in ['right', 'top']:
        spine.set_color('none')

# Display ticks only at the bottom and left        
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('left')

# Switch the position of the ticks to be outside the axes
ax.tick_params(axis='y', direction='out')

ax.legend( (rectsc[0], rectsh[0]), ('Control',  '3.16 ng/ml dDAVP'), loc='upper right' )

plt.show()      
    