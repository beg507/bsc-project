# ----------------------------IMPORTS, DEPENDENCIES AND CONSTANTS----------------------------

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline

import matplotlib.pyplot as plt
import ephemeris as eph
import body_data

from plotting_actual_traj import x_positions
from plotting_actual_traj import y_positions

start_time = 0
end_time = (9 * 365 * 24 * 3600) + (5*31*24*60*60) + (24*24*60*60)

# ------------------------------------------FUNCTIONS------------------------------------------

def euler_method(t, state, M, G):
    x, y, vx, vy = state

    # calculate acceleration due to gravity (newton)
    r = ((x ** 2) + (y ** 2)) ** 0.5
    ax = (-G * M * x) / (r ** 3)
    ay = (-G * M * y) / (r ** 3)

    # return state derivatives as a single array
    return [vx, vy, ax, ay]

def ship_orbit(x, y, vx, vy, dt, m_sun, m_jupiter, G, r_hill_jupiter, x_j, y_j):
    # calculate distance between ship and sun, and ship and jupiter
    r_sun = ((x ** 2) + (y ** 2)) ** 0.5
    r_jupiter = ((x - x_j) ** 2 + (y - y_j) ** 2) ** 0.5
   
    if r_jupiter < r_hill_jupiter:
        ax =( -G * (m_jupiter * (x - x_j)) / (r_jupiter ** 3))
        ay = (-G * (m_jupiter * (y - y_j)) / (r_jupiter ** 3))
        dt = 10
        new_vx = vx + ax    *dt
        new_vy = vy + ay    *dt
        new_x = x + new_vx  *dt
        new_y = y + new_vy  *dt
    else:

        dt=dt
        ax = (-G * m_sun * x )/ (r_sun ** 3)
        ay = (-G * m_sun * y) / (r_sun ** 3)
        new_vx = vx + ax * dt
        new_vy = vy + ay * dt
        new_x = x + new_vx * dt
        new_y = y + new_vy * dt


    return new_x, new_y, new_vx, new_vy, dt

def plot_trajectory(start_time, end_time, x0, y0, vx0, vy0, M, G):
    # initial state
    state0 = [x0, y0, vx0, vy0]

    # solve the differential equations using solve_ivp with dopri5
    solution = solve_ivp(euler_method, [start_time, end_time], state0, args=(M, G), method='DOP853', rtol=1e-12, atol=1e-22)

    # return the solution in the form (t, y) where t is the time and y is [x, y, vx, vy]
    return solution

# ------------------------------------------SOLVING------------------------------------------


# trajectories using plot_trajectory function (take start and end time, initial state, constant values)
ship_trajectory = plot_trajectory(start_time, end_time, eph.x_pos_ship, eph.y_pos_ship, eph.x_vel_ship, eph.y_vel_ship, body_data.sun_mass, body_data.G_km)
earth_trajectory = plot_trajectory(start_time, end_time, eph.x_pos_earth, eph.y_pos_earth, eph.x_vel_earth, eph.y_vel_earth, body_data.sun_mass, body_data.G_km)
jupiter_trajectory = plot_trajectory(start_time, end_time, eph.x_pos_jupiter, eph.y_pos_jupiter, eph.x_vel_jupiter, eph.y_vel_jupiter, body_data.sun_mass, body_data.G_km)
pluto_trajectory = plot_trajectory(start_time, end_time, eph.x_pos_pluto, eph.y_pos_pluto, eph.x_vel_pluto, eph.y_vel_pluto, body_data.sun_mass, body_data.G_km)

distance = []
for n in range(0, (end_time)):
    distance.append(((ship_trajectory.y[0][n]-jupiter_trajectory.y[0][n])**2 + (ship_trajectory.y[1][n]-jupiter_trajectory.y[1][n])**2)**0.5)
print(f"The number of states in ship_trajectory is {len(ship_trajectory.y)}")
print(f"The distances between the ship and Jupiter at each state are: {distance}")

    #print(ship_trajectory.y[0][0]) # first x position
# ------------------------------------------GRAVITY ASSIST------------------------------------------

#if (((ship_trajectory.y[0]-jupiter_trajectory.y[0])**2 + (ship_trajectory.y[1]-jupiter_trajectory.y[])**2) ** 0.5) < body_data.jupiter_hill_sphere:





#     r_jupiter = ((x - x_j) ** 2 + (y - y_j) ** 2) ** 0.5


# ------------------------------------------PLOTTING------------------------------------------
plt.style.use( 'dark_background' )
fig, graph = plt.subplots()

# interpolate jupiter trajectory to match time steps of ship trajectory
jupiter_x = np.interp(ship_trajectory.t, jupiter_trajectory.t, jupiter_trajectory.y[0])
jupiter_y = np.interp(ship_trajectory.t, jupiter_trajectory.t, jupiter_trajectory.y[1])

# compute distance from Jupiter
distance = np.sqrt((ship_trajectory.y[0]-jupiter_x)**2 + (ship_trajectory.y[1]-jupiter_y)**2)

# plot the trajectory with different colors
for x, y, d in zip(ship_trajectory.y[0], ship_trajectory.y[1], distance):
    if d < body_data.jupiter_hill_sphere:
        plt.plot(x, y, 'g')  # green color if within Jupiter's Hill sphere
    else:
        plt.plot(x, y, 'b')  # blue color otherwise


#plt.plot (ship_trajectory.y[0], ship_trajectory.y[1], color='white', label='Ship [NO GA]')
plt.plot(earth_trajectory.y[0], earth_trajectory.y[1], color='cyan', label='Earth')
plt.plot(jupiter_trajectory.y[0], jupiter_trajectory.y[1], color='indianred', label='Jupiter')
plt.plot(pluto_trajectory.y[0], pluto_trajectory.y[1], color='khaki', label='Pluto')


graph.set_xlim([-40*149597870.691, 40*149597870.691]) # set to 40AU to see whole solar system up to pluto
graph.set_ylim([-40*149597870.691, 40*149597870.691])

graph.set_aspect('equal', adjustable='box')

#plt.rcParams["figure.figsize"] = (20,20)
plt.axis('equal')
plt.legend(loc='upper left')
plt.xlabel('x position (km)')
plt.ylabel('y position (km)')
plt.title('Orbits of Earth, Jupiter, Pluto, and Ship around the Sun')

plt.plot(x_positions, y_positions, color='green', label='New Horizons Data')


plt.show()

# ------------------------------------------INVESTIGATING------------------------------------------

    # ARGMIN METHOD
# this method isn't great because it just finds the closest value so if the values are far apart then they're not accurate
# doing t=1 and t=2 gives the same results

# find the index of the closest time point to t = end bracket
index = np.argmin(np.abs(ship_trajectory.t - (60*60*24*366)))

# get the velocity at that time
vx, vy = ship_trajectory.y[2:4, index]

print("WITH SOLVER ONLY: At time t=1 month, the x velocity of the ship is", vx, "and the y velocity of the ship is", vy)
# At time t=1 month, the x velocity of the ship is -25.74809569292693 and the y velocity of the ship is -30.734133989957375

    # INTERPOLATION METHODS 
# this method works better and gives much more accurat results
# get the x and y velocities from the trajectory data
vx_time = ship_trajectory.y[2]
vy_time = ship_trajectory.y[3]

# create an interpolation function for the velocity
interp_func = CubicSpline(ship_trajectory.t, np.column_stack((vx_time, vy_time)), axis=0)

# evaluate the velocity at t = 2.0
vx_interp, vy_interp = interp_func(np.array([(60*60*24*366)]))[0]
print("WITH INTERP: At time t=1 month, the x velocity of the ship is", vx_interp, "and the y velocity of the ship is", vy_interp)

