import numpy as np
import ephemeris as eph

# dt = time step, t_max is simulation duration
dt = 200  # seconds
t_max = (9 * 365 * 24 * 3600) + (5*31*24*60*60) + (24*24*60*60)  # 9y 5m 25d


t_array = np.arange(0, t_max, dt) # array from 0 to t_max with steps of dt (start, stop, step)
n_steps = len(t_array) # length of the t_array is the number of steps
#print(t_array/31536000)
# initialize arrays to store positions and velocities

# SHIP WITH GRAVITY ASSIST
x_ship_array = np.zeros(n_steps)
y_ship_array = np.zeros(n_steps)
x_ship_array[0] = eph.x_pos_ship
y_ship_array[0] = eph.y_pos_ship
vx_ship_array = np.zeros(n_steps)
vy_ship_array = np.zeros(n_steps)
#-0.2 for x and -0.4 for y gives the look of the no jupiter trajectory
##-0.2 for x and -0.6 for y follows NH trajectory but overshoots pluto
vx_ship_array[0] = eph.x_vel_ship-0.2 
vy_ship_array[0] = eph.y_vel_ship-0.6

v_ship = (((eph.x_vel_ship-0.2)**2) +  ((eph.y_vel_ship-0.6)**2))**0.5
#print(v_ship)

# SHIP WITHOUT GRAVITY ASSIST
x_ship_array_n = np.zeros(n_steps)
y_ship_array_n = np.zeros(n_steps)
x_ship_array_n[0] = eph.x_pos_ship
y_ship_array_n[0] = eph.y_pos_ship
vx_ship_array_n = np.zeros(n_steps)
vy_ship_array_n = np.zeros(n_steps)
vx_ship_array_n[0] = eph.x_vel_ship
vy_ship_array_n[0] = eph.y_vel_ship

# MERCURY
x_mercury_array = np.zeros(n_steps)
y_mercury_array = np.zeros(n_steps)
x_mercury_array[0] = eph.x_pos_mercury
y_mercury_array[0] = eph.y_pos_mercury
vx_mercury_array = np.zeros(n_steps)
vy_mercury_array = np.zeros(n_steps)
vx_mercury_array[0] = eph.x_vel_mercury
vy_mercury_array[0] = eph.y_vel_mercury

# VENUS
x_venus_array = np.zeros(n_steps)
y_venus_array = np.zeros(n_steps)
x_venus_array[0] = eph.x_pos_earth
y_venus_array[0] = eph.y_pos_earth
vx_venus_array = np.zeros(n_steps)
vy_venus_array = np.zeros(n_steps)
vx_venus_array[0] = eph.x_vel_earth
vy_venus_array[0] = eph.y_vel_earth

# EARTH
x_earth_array = np.zeros(n_steps)
y_earth_array = np.zeros(n_steps)
x_earth_array[0] = eph.x_pos_earth
y_earth_array[0] = eph.y_pos_earth
vx_earth_array = np.zeros(n_steps)
vy_earth_array = np.zeros(n_steps)
vx_earth_array[0] = eph.x_vel_earth
vy_earth_array[0] = eph.y_vel_earth

# MARS
x_mars_array = np.zeros(n_steps)
y_mars_array = np.zeros(n_steps)
x_mars_array[0] = eph.x_pos_mars
y_mars_array[0] = eph.y_pos_mars
vx_mars_array = np.zeros(n_steps)
vy_mars_array = np.zeros(n_steps)
vx_mars_array[0] = eph.x_vel_mars
vy_mars_array[0] = eph.y_vel_mars

# JUPITER
x_jupiter_array = np.zeros(n_steps)
y_jupiter_array = np.zeros(n_steps)
x_jupiter_array[0] = eph.x_pos_jupiter
y_jupiter_array[0] = eph.y_pos_jupiter
vx_jupiter_array = np.zeros(n_steps)
vy_jupiter_array = np.zeros(n_steps)
vx_jupiter_array[0] = eph.x_vel_jupiter
vy_jupiter_array[0] = eph.y_vel_jupiter

# SATURN
x_saturn_array = np.zeros(n_steps)
y_saturn_array = np.zeros(n_steps)
x_saturn_array[0] = eph.x_pos_saturn
y_saturn_array[0] = eph.y_pos_saturn
vx_saturn_array = np.zeros(n_steps)
vy_saturn_array = np.zeros(n_steps)
vx_saturn_array[0] = eph.x_vel_saturn
vy_saturn_array[0] = eph.y_vel_saturn

# URANUS
x_uranus_array = np.zeros(n_steps)
y_uranus_array = np.zeros(n_steps)
x_uranus_array[0] = eph.x_pos_uranus
y_uranus_array[0] = eph.y_pos_uranus
vx_uranus_array = np.zeros(n_steps)
vy_uranus_array = np.zeros(n_steps)
vx_uranus_array[0] = eph.x_vel_uranus
vy_uranus_array[0] = eph.y_vel_uranus

# NEPTUNE
x_neptune_array = np.zeros(n_steps)
y_neptune_array = np.zeros(n_steps)
x_neptune_array[0] = eph.x_pos_neptune
y_neptune_array[0] = eph.y_pos_neptune
vx_neptune_array = np.zeros(n_steps)
vy_neptune_array = np.zeros(n_steps)
vx_neptune_array[0] = eph.x_vel_neptune
vy_neptune_array[0] = eph.y_vel_neptune

# PLUTO
x_pluto_array = np.zeros(n_steps)
y_pluto_array = np.zeros(n_steps)
x_pluto_array[0] = eph.x_pos_pluto
y_pluto_array[0] = eph.y_pos_pluto
vx_pluto_array = np.zeros(n_steps)
vy_pluto_array = np.zeros(n_steps)
vx_pluto_array[0] = eph.x_vel_pluto
vy_pluto_array[0] = eph.y_vel_pluto

