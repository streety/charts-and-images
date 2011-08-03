import numpy as np
import matplotlib.pyplot as plt

#Generate sample data
var = np.random.random_sample((40,2))

fig = plt.figure()
for i in range(4):
    ax = fig.add_subplot(220 + i + 1)
    start = i * 10
    ax.plot(var[start:start+10,0], var[start:start+10,1], 'bo')
    
    #Hide the x axis on the top row of charts
    if i in [0,1]:
        ax.set_xticklabels(ax.get_xticklabels(), visible=False)
        
    #Hide the y axis on the right column of charts
    if i in [1,3]:
        ax.set_yticklabels(ax.get_yticklabels(), visible=False)
    
    #Set the axis range
    ax.axis([0,1,0,1])
plt.show()