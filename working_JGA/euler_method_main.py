import numpy as np
import matplotlib.pyplot as plt

import ephemeris as eph
import body_data
from body_data import *
from functions import euler_method
from functions import ship_orbit
from plotting_actual_traj import x_positions
from plotting_actual_traj import y_positions

import array_file
from array_file import *

import date_finder
from date_finder import *

ship_jup_dist = [] # monitoring distance between ship and jupiter
ship_velocity_array = [] 
jupiter_closest_approach_array = []
ship_pluto_dist = [] # monitoring distance between ship and pluto
pluto_closest_approach_array = []
jupiter_hill_sphere_step = []

# over the simulation duration (should be around 10 years for new horizons)
# hover over functions to view their inputs
for step in range(1, n_steps):
    
    # calculating the new position and velocities of the planets using the euler function, and the ship using the ship orbit function
    
    # PLANETS IN ORDER
    x_mercury_array[step], y_mercury_array[step], vx_mercury_array[step], vy_mercury_array[step] = euler_method(
        x_mercury_array[step-1], y_mercury_array[step-1], vx_mercury_array[step-1], vy_mercury_array[step-1], dt, body_data.sun_mass, body_data.G_km)
    
    x_venus_array[step], y_venus_array[step], vx_venus_array[step], vy_venus_array[step] = euler_method(
        x_venus_array[step-1], y_venus_array[step-1], vx_venus_array[step-1], vy_venus_array[step-1], dt, body_data.sun_mass, body_data.G_km)
    
    x_earth_array[step], y_earth_array[step], vx_earth_array[step], vy_earth_array[step] = euler_method(
        x_earth_array[step-1], y_earth_array[step-1], vx_earth_array[step-1], vy_earth_array[step-1], dt, body_data.sun_mass, body_data.G_km)

    x_mars_array[step], y_mars_array[step], vx_mars_array[step], vy_mars_array[step] = euler_method(
        x_mars_array[step-1], y_mars_array[step-1], vx_mars_array[step-1], vy_mars_array[step-1], dt, body_data.sun_mass, body_data.G_km)
    
    x_jupiter_array[step], y_jupiter_array[step], vx_jupiter_array[step], vy_jupiter_array[step] = euler_method(
        x_jupiter_array[step-1], y_jupiter_array[step-1], vx_jupiter_array[step-1], vy_jupiter_array[step-1], dt, body_data.sun_mass, body_data.G_km)
    
    x_saturn_array[step], y_saturn_array[step], vx_saturn_array[step], vy_saturn_array[step] = euler_method(
        x_saturn_array[step-1], y_saturn_array[step-1], vx_saturn_array[step-1], vy_saturn_array[step-1], dt, body_data.sun_mass, body_data.G_km)
    
    x_uranus_array[step], y_uranus_array[step], vx_uranus_array[step], vy_uranus_array[step] = euler_method(
        x_uranus_array[step-1], y_uranus_array[step-1], vx_uranus_array[step-1], vy_uranus_array[step-1], dt, body_data.sun_mass, body_data.G_km)

    x_neptune_array[step], y_neptune_array[step], vx_neptune_array[step], vy_neptune_array[step] = euler_method(
        x_neptune_array[step-1], y_neptune_array[step-1], vx_neptune_array[step-1], vy_neptune_array[step-1], dt, body_data.sun_mass, body_data.G_km)

    x_pluto_array[step], y_pluto_array[step], vx_pluto_array[step], vy_pluto_array[step] = euler_method(
        x_pluto_array[step-1], y_pluto_array[step-1], vx_pluto_array[step-1], vy_pluto_array[step-1], dt, body_data.sun_mass, body_data.G_km)
    
    # SHIP WITH GRAVITY ASSIST
    x_ship_array[step], y_ship_array[step], vx_ship_array[step], vy_ship_array[step], dt = ship_orbit(
        x_ship_array[step-1], y_ship_array[step-1], vx_ship_array[step-1], vy_ship_array[step-1], dt, body_data.sun_mass,
        body_data.jupiter_mass, body_data.pluto_mass, body_data.G_km, body_data.jupiter_hill_sphere, body_data.pluto_hill_sphere,
        x_jupiter_array[step-1], y_jupiter_array[step-1], 
         x_pluto_array[step-1], y_pluto_array[step-1])
    
    # SHIP WITHOUT GRAVITY ASSIST
    x_ship_array_n[step], y_ship_array_n[step], vx_ship_array_n[step], vy_ship_array_n[step] = euler_method(
        x_ship_array_n[step-1], y_ship_array_n[step-1], vx_ship_array_n[step-1], vy_ship_array_n[step-1], dt, body_data.sun_mass, body_data.G_km)


    # SHIP VELOCITY AT EACH STEP (JGA)
    ship_velocity_array.append((((vx_ship_array[step])**2) + ((vy_ship_array[step])**2))**0.5)

    # this small section checks the distance between the ship and jupiter to make sure the ship does not enter jupiter's atmosphere
    ship_jup_dist = (((x_ship_array[step] - x_jupiter_array[step])**2 + (y_ship_array[step] - y_jupiter_array[step])**2)**0.5)
    jupiter_closest_approach_array.append([ship_jup_dist, step])
    if ship_jup_dist < body_data.jupiter_radius:
        print("Crashed into Jupiter")
        break
    if ship_jup_dist < body_data.jupiter_hill_sphere:
        jupiter_hill_sphere_step.append(step)
        
    
    # this does the same for pluto
    ship_pluto_dist = (((x_ship_array[step] - x_pluto_array[step])**2 + (y_ship_array[step] - y_pluto_array[step])**2)**0.5)
    pluto_closest_approach_array.append([ship_pluto_dist, step])
    if ship_pluto_dist < body_data.pluto_radius:
        print("Crashed into Pluto")
        break

    #ship_pluto_dist.append(((x_ship_array[step] - x_pluto_array[step])**2 + (y_ship_array[step] - y_pluto_array[step])**2)**0.5)
    
#   JUPITER CLOSEST APPROACH
    # finding minimum value in closest approach array
jupiter_closest_approach_r = jupiter_closest_approach_array[0][0] # assume the first element has the minimum x value
for i in range(1, len(jupiter_closest_approach_array)): # iterate over the remaining elements
    if jupiter_closest_approach_array[i][0] < jupiter_closest_approach_r: # compare x value with current minimum
        jupiter_closest_approach_r = jupiter_closest_approach_array[i][0] # update minimum x value
    # finding corresponding y value (the step)
for i in jupiter_closest_approach_array:
    if i[0] == jupiter_closest_approach_r:
        jupiter_closest_approach_t = i[1] # this is the STEP not the seconds
        break


print("----------ENTER JUPITER HILL SPHERE----------")
print("Ship entered Jupiter's hill sphere at step:", jupiter_hill_sphere_step[0])
print("Ship entered Jupiter's hill sphere at time (s):", t_array[jupiter_hill_sphere_step[0]])
print("Ship entered Jupiter's hill sphere on:", enter_jupiter_hill_sphere_date.strftime('%Y-%m-%d %H:%M:%S'))
print("Ship entered Jupiter's hill sphere at x (km):", x_ship_array[jupiter_hill_sphere_step[0]])
print("Ship entered Jupiter's hill sphere at y (km):", y_ship_array[jupiter_hill_sphere_step[0]])
print("Ship entered Jupiter's hill sphere at vx (km/s):", vx_ship_array[jupiter_hill_sphere_step[0]])
print("Ship entered Jupiter's hill sphere at vy (km/s):", vy_ship_array[jupiter_hill_sphere_step[0]])
print("Ship entered Jupiter's hill sphere at v (km/s):", ((((vx_ship_array[jupiter_hill_sphere_step[0]])**2) + ((vy_ship_array[jupiter_hill_sphere_step[0]])**2))**0.5))
print("----------JUPITER CLOSEST APPROACH----------")
print("Jupiter closest approach r (km):", jupiter_closest_approach_r) 
print("Jupiter closest approach t (s):", t_array[jupiter_closest_approach_t])
print("Jupiter closest approach x (km):", x_ship_array[jupiter_closest_approach_t])
print("Jupiter closest approach y (km):", y_ship_array[jupiter_closest_approach_t])
print("Jupiter closest approach vx (km/s):", vx_ship_array[jupiter_closest_approach_t])
print("Jupiter closest approach vy (km/s):", vy_ship_array[jupiter_closest_approach_t])
print("Jupiter closest approach v (km/s):", ((((vx_ship_array[jupiter_closest_approach_t])**2) + ((vy_ship_array[jupiter_closest_approach_t])**2))**0.5))
print("Jupiter closest appraoch date:", jupiter_closest_approach_date.strftime('%Y-%m-%d %H:%M:%S'))
print("----------EXIT JUPITER HILL SPHERE----------")
print("Ship exited Jupiter's hill sphere at step:", jupiter_hill_sphere_step[-1])
print("Ship exited Jupiter's hill sphere at time (s):", t_array[jupiter_hill_sphere_step[-1]])
print("Ship exited Jupiter's hill sphere on:", exit_jupiter_hill_sphere_date.strftime('%Y-%m-%d %H:%M:%S'))
print("Ship exited Jupiter's hill sphere at x (km):", x_ship_array[jupiter_hill_sphere_step[-1]])
print("Ship exited Jupiter's hill sphere at y (km):", y_ship_array[jupiter_hill_sphere_step[-1]])
print("Ship exited Jupiter's hill sphere at vx (km/s):", vx_ship_array[jupiter_hill_sphere_step[-1]])
print("Ship exited Jupiter's hill sphere at vy (km/s):", vy_ship_array[jupiter_hill_sphere_step[-1]])
print("Ship exited Jupiter's hill sphere at v (km/s):", ((((vx_ship_array[jupiter_hill_sphere_step[-1]])**2) + ((vy_ship_array[jupiter_hill_sphere_step[-1]])**2))**0.5))
print("Velocity increase (km/s) due to JGA:", ((((vx_ship_array[jupiter_hill_sphere_step[-1]])**2) + ((vy_ship_array[jupiter_hill_sphere_step[-1]])**2))**0.5) - ((((vx_ship_array[jupiter_hill_sphere_step[0]])**2) + ((vy_ship_array[jupiter_hill_sphere_step[0]])**2))**0.5))


#   PLUTO CLOSEST APPROACH
    # finding minimum value in closest approach array
pluto_closest_approach_r = pluto_closest_approach_array[0][0] # assume the first element has the minimum x value
for i in range(1, len(pluto_closest_approach_array)): # iterate over the remaining elements
    if pluto_closest_approach_array[i][0] < pluto_closest_approach_r: # compare x value with current minimum
        pluto_closest_approach_r = pluto_closest_approach_array[i][0] # update minimum x value
    # finding corresponding y value (the step)
for i in pluto_closest_approach_array:
    if i[0] == pluto_closest_approach_r:
        pluto_closest_approach_t = i[1] # this is the STEP not the seconds
        break

print("----------PLUTO CLOSEST APPROACH----------")
print("Pluto closest approach r (km):", pluto_closest_approach_r) 
print("Pluto closest approach t (s):", t_array[pluto_closest_approach_t])
print("Pluto closest approach x (km):", x_ship_array[pluto_closest_approach_t])
print("Pluto closest approach y (km):", y_ship_array[pluto_closest_approach_t])
print("Pluto closest approach vx (km/s):", vx_ship_array[pluto_closest_approach_t])
print("Pluto closest approach vy (km/s):", vy_ship_array[pluto_closest_approach_t])
print("Pluto closest approach v (km/s):", ((((vx_ship_array[pluto_closest_approach_t])**2) + ((vy_ship_array[pluto_closest_approach_t])**2))**0.5))
print("Pluto closest appraoch date:", pluto_closest_approach_date.strftime('%Y-%m-%d %H:%M:%S'))



#plot the orbits
#plt.style.use( 'dark_background' )
fig, graph = plt.subplots()

# planets
plt.plot(x_mercury_array/AU, y_mercury_array/AU, color='brown', label='Mercury')
plt.plot(x_venus_array/AU, y_venus_array/AU, color='orange', label='Venus')
plt.plot(x_earth_array/AU, y_earth_array/AU, color='cyan', label='Earth')
plt.plot(x_mars_array/AU, y_mars_array/AU, color='red', label='Mars')
plt.plot(x_jupiter_array/AU, y_jupiter_array/AU, color='indianred', label='Jupiter')
plt.plot(x_saturn_array/AU, y_saturn_array/AU, color='brown', label='Saturn')
plt.plot(x_uranus_array/AU, y_uranus_array/AU, color='dodgerblue', label='Uranus')
plt.plot(x_neptune_array/AU, y_neptune_array/AU, color='blue', label='Neptune')
plt.plot(x_pluto_array/AU, y_pluto_array/AU, color='khaki', label='Pluto')

# ships
plt.plot(x_ship_array/AU, y_ship_array/AU, color='black',  label='Ship (JGA)')
plt.plot(x_ship_array_n/AU, y_ship_array_n/AU, color='grey', label='Ship (NO JGA)')
plt.plot(x_positions, y_positions, color='green', label='New Horizons Data')

# centering
graph.spines.left.set_position('zero')
graph.spines.right.set_color('none')
graph.spines.bottom.set_position('zero')
graph.spines.top.set_color('none')
graph.xaxis.set_ticks_position('bottom')
graph.yaxis.set_ticks_position('left')

 # axes
graph.set_xlim([-40*AU, 40*AU]) # set to 40AU to see whole solar system up to pluto
graph.set_ylim([-40*AU, 40*AU])

graph.xaxis.set_major_locator(plt.MaxNLocator(20))
graph.yaxis.set_major_locator(plt.MaxNLocator(20))

graph.set_aspect('equal', adjustable='box')

#plt.rcParams["figure.figsize"] = (20,20)

plt.axis('equal')
plt.legend(loc='upper left')
plt.xlabel('x position (km)')
plt.ylabel('y position (km)')
plt.title('Heliocentric Orbits of the Considered Bodies')
plt.show()

#plt.plot(vx_ship_array, vy_ship_array, color='white',  label='Ship (JGA)')
#plt.show()

#new_horizons_velocity_array = []
#t_array = t_array[:-1]
#y_array = t_array/31536000
#plt.plot(y_array, ship_velocity_array, color='black',  label='Ship (JGA)')
#plt.xlabel('Time (Years)')
#plt.ylabel('Velocity (km/s)') 
#plt.show()