import numpy as np
import matplotlib.pyplot as plt

#Generate sample data
var = np.random.random_sample((10,2))

#Plot data with labels
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(var[0:5,0], var[0:5,1], 'bo', label="First half")
ax.plot(var[5:10,0], var[5:10,1], 'r^', label="Second half")
ax.legend(numpoints=1)
plt.show()