AU = 149597870.691 #km

ship_x = 7.9
ship_y = 31.6
pluto_x = 8.0
pluto_y = 31.9

import numpy as np

distance = np.sqrt((pluto_x-ship_x)**2 + (pluto_y - ship_y)**2)

print(distance*AU)