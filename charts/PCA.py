import mdp
import numpy as np
import matplotlib.pyplot as plt

#Create sample data
var1 = np.random.normal(loc=0., scale=0.5, size=(10,5))
var2 = np.random.normal(loc=4., scale=1., size=(10,5))
var = np.concatenate((var1,var2), axis=0)

#Create the PCA node and train it
pcan = mdp.nodes.PCANode(output_dim=3)
pcar = pcan.execute(var)

#Graph the results
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(pcar[:10,0], pcar[:10,1], 'bo')
ax.plot(pcar[10:,0], pcar[10:,1], 'ro')

#Show variance accounted for
ax.set_xlabel('PC1 (%.3f%%)' % (pcan.d[0]))
ax.set_ylabel('PC2 (%.3f%%)' % (pcan.d[1]))

plt.show()