import scipy as sp
import scipy.stats as sps
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
x = np.random.random(20)
y = x + np.random.normal(size=(20))


 
# Setup the figure
fig = plt.figure()
ax = fig.add_subplot(111)

# Setup the linear regression line
linregress = sps.linregress(x, y)

def fit(linregress, x):
    return linregress[1]+linregress[0]*x

xfit = np.array([np.amin(x), np.amax(x)])

# Plot both the values and the linear regression line
ax.plot(x, y, 'k.', xfit, fit(linregress, xfit), 'k-', lw=2)

# Write the R value on the plot
ax.text(0.7, -1., 'R = %.2f' % linregress[2], fontsize='x-large')


# Remove the surrounding lines from the plot
for loc, spine in ax.spines.iteritems():
    if loc in ['right', 'top']:
        spine.set_color('none')

# Display ticks only at the bottom and left
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Switch the position of the ticks to be outside the axes
ax.tick_params(direction='out')

ax.set_xlabel('x', size='x-large')
ax.set_ylabel('y', size='x-large')

plt.show()