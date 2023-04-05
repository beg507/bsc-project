import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('closest_appraoch_array.txt')

# create an array of x values

# create an array of zeros with the same length as x
y = np.zeros_like(data)

# plot the data
plt.plot(data, y)

# add a label to the x axis
plt.xlabel('X values')

# add a title to the plot
plt.title('Plotting only x values')

# display the plot  
plt.show()
