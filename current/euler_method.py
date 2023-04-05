import numpy as np
import matplotlib.pyplot as plt

import ephemeris as eph
import body_data
from body_data import *
from functions import euler_method
from functions import ship_orbit


# dt = time step, t_max is simulation duration
dt = 300  # seconds
t_max = 10 * 365 * 24 * 3600  # 10 years in seconds

# initialize arrays to store positions
t_array = np.arange(0, t_max, dt) # array from 0 to t_max with steps of dt (start, stop, step)
n_steps = len(t_array) # length of the t_array is the number of steps

x_ship_array = np.zeros(n_steps)
y_ship_array = np.zeros(n_steps)
x_ship_array[0] = eph.x_pos_ship
y_ship_array[0] = eph.y_pos_ship

x_earth_array = np.zeros(n_steps)
y_earth_array = np.zeros(n_steps)
x_earth_array[0] = eph.x_pos_earth
y_earth_array[0] = eph.y_pos_earth

x_jupiter_array = np.zeros(n_steps)
y_jupiter_array = np.zeros(n_steps)
x_jupiter_array[0] = eph.x_pos_jupiter
y_jupiter_array[0] = eph.y_pos_jupiter

x_pluto_array = np.zeros(n_steps)
y_pluto_array = np.zeros(n_steps)
x_pluto_array[0] = eph.x_pos_pluto
y_pluto_array[0] = eph.y_pos_pluto

ship_jup_dist = [] # monitoring distance between ship and jupiter

# over the simulation duration (should be around 10 years for new horizons)
# hover over functions to view their inputs
for step in range(1, n_steps):
    
    # calculate new position and velocity of earth using euler_method function
    x_earth_array[step], y_earth_array[step], eph.x_vel_earth, eph.y_vel_earth = euler_method(
        x_earth_array[step-1], y_earth_array[step-1], eph.x_vel_earth, eph.y_vel_earth, dt, body_data.sun_mass, body_data.G_km)

    # calculate new position and velocity of jupiter using euler_method function
    x_jupiter_array[step], y_jupiter_array[step], eph.x_vel_jupiter, eph.y_vel_jupiter = euler_method(
        x_jupiter_array[step-1], y_jupiter_array[step-1], eph.x_vel_jupiter, eph.y_vel_jupiter, dt, body_data.sun_mass, body_data.G_km)

    # calculate new position and velocity of pluto using euler_method function
    x_pluto_array[step], y_pluto_array[step], eph.x_vel_pluto, eph.y_vel_pluto = euler_method(
        x_pluto_array[step-1], y_pluto_array[step-1], eph.x_vel_pluto, eph.y_vel_pluto, dt, body_data.sun_mass, body_data.G_km)
    
    # calculate new position and velocity of ship using ship_orbit function
    x_ship_array[step], y_ship_array[step], eph.x_vel_ship, eph.y_vel_ship = ship_orbit(
        x_ship_array[step-1], y_ship_array[step-1], eph.x_vel_ship, eph.y_vel_ship, dt, body_data.sun_mass,
        body_data.jupiter_mass, body_data.G_km, body_data.jupiter_hill_sphere, x_jupiter_array[step-1], y_jupiter_array[step-1])
    
    ship_jup_dist.append(((x_ship_array[step] - x_jupiter_array[step])**2 + (y_ship_array[step] - y_jupiter_array[step])**2)**0.5)


np.savetxt("ship_jup_dist.txt", ship_jup_dist)

#plot the orbits
plt.style.use( 'dark_background' )
fig, graph = plt.subplots()


plt.plot(x_earth_array, y_earth_array, color='cyan', label='Earth')
plt.plot(x_jupiter_array, y_jupiter_array, color='indianred', label='Jupiter')
plt.plot(x_pluto_array, y_pluto_array, color='khaki', label='Pluto')
plt.plot(x_ship_array, y_ship_array, color='white', label='Ship')


graph.set_xlim([-40*149597870.691, 40*149597870.691]) # set to 40AU to see whole solar system up to pluto
graph.set_ylim([-40*149597870.691, 40*149597870.691])

graph.set_aspect('equal', adjustable='box')

#plt.rcParams["figure.figsize"] = (20,20)
plt.axis('equal')
plt.legend(loc='upper left')
plt.xlabel('x position (km)')
plt.ylabel('y position (km)')
plt.title('Orbits of Earth, Jupiter, Pluto, and Ship around the Sun')
plt.show()
