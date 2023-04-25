
import numpy as np
import body_data
from body_data import *
import matplotlib.pyplot as plt

x_ship=1028971996.8728954
y_ship=-4769430029.226835
vx_ship=5.63170960560951
vy_ship=-17.266519596117277
x_pluto=1029079093.5016124
y_pluto=-4777103001.815765
vx_pluto=5.416074969261827
vy_pluto=0.045715612348158255

# pluto at (0,0)
x_ship_rel_pluto = x_ship - x_pluto
y_ship_rel_pluto = y_ship - y_pluto
vx_ship_rel_pluto = (vx_ship - vx_pluto)*0.01
vy_ship_rel_pluto = (vy_ship - vy_pluto)*0.01


def euler_method(x, y, vx, vy, dt, M, G):
    # calculate acceleration due to gravity (newton)
    r = ((x ** 2) + (y ** 2)) ** 0.5
    ax = (-G * M * x) / (r ** 3)
    ay = (-G * M * y) / (r ** 3)

    # update velocity and position using Euler method
    new_vx = vx + ax * dt
    new_vy = vy + ay * dt
    new_x = x + new_vx * dt
    new_y = y + new_vy * dt

    return new_x, new_y, new_vx, new_vy # new positions and velocities

# dt = time step, t_max is simulation duration
dt = 10  # seconds
#t_max = (9 * 365 * 24 * 3600) + (5*31*24*60*60) + (24*24*60*60)  # 9y 5m 25d
t_max = (1 * 365 * 24 * 3600)  # 12y
#t_max = 268481400


t_array = np.arange(0, t_max, dt) # array from 0 to t_max with steps of dt (start, stop, step)
n_steps = len(t_array) # length of the t_array is the number of steps
#print(t_array/31536000)
# initialize arrays to store positions and velocities

# SHIP WITH GRAVITY ASSIST
x_ship_array = np.zeros(n_steps)
y_ship_array = np.zeros(n_steps)
x_ship_array[0] = x_ship_rel_pluto
y_ship_array[0] = y_ship_rel_pluto
vx_ship_array = np.zeros(n_steps)
vy_ship_array = np.zeros(n_steps)
vx_ship_array[0] = vx_ship_rel_pluto
vy_ship_array[0] = vy_ship_rel_pluto

for step in range(1, n_steps):

    x_ship_array[step], y_ship_array[step], vx_ship_array[step], vy_ship_array[step] = euler_method(
        x_ship_array[step-1], y_ship_array[step-1], vx_ship_array[step-1], vy_ship_array[step-1], dt, body_data.pluto_mass, body_data.G_km)
    

fig, graph = plt.subplots()



# ships
plt.plot(x_ship_array, y_ship_array, color='black',  label='Ship (JGA)')


# centering
graph.spines.left.set_position('zero')
graph.spines.right.set_color('none')
graph.spines.bottom.set_position('zero')
graph.spines.top.set_color('none')
graph.xaxis.set_ticks_position('bottom')
graph.yaxis.set_ticks_position('left')


graph.set_aspect('equal', adjustable='box')

#plt.rcParams["figure.figsize"] = (20,20)

plt.axis('equal')
plt.legend(loc='upper left')
plt.xlabel('x position (km)')
plt.ylabel('y position (km)')
plt.title('Heliocentric Orbits of the Considered Bodies')
plt.show()