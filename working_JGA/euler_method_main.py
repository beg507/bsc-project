import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import math

import ephemeris as eph
import body_data
from body_data import *
from functions import euler_method
from functions import ship_orbit
from plotting_actual_traj import x_positions
from plotting_actual_traj import y_positions
from plotting_actual_traj import new_horizons_velocity_array
from plotting_actual_traj import years

import array_file
from array_file import *

import date_finder
from date_finder import *

ship_jup_dist = [] # monitoring distance between ship and jupiter
ship_velocity_array = [] 
ship_velocity_array_n = [] 
jupiter_closest_approach_array = []
ship_pluto_dist = [] # monitoring distance between ship and pluto
pluto_closest_approach_array = []

jupiter_hill_sphere_step = []
pluto_hill_sphere_step = []

enter_pluto_hill_sphere = False
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
    # SHIP VELOCITY AT EACH STEP (NO JGA)
    ship_velocity_array_n.append((((vx_ship_array_n[step])**2) + ((vy_ship_array_n[step])**2))**0.5)


# FOR OURPUT ONE: COMMENT ALL COURSE CORRECTIONS OUT, ENSURE SHIP IS USING EULER_METHOD NOT SHIP_ORBIT
# FOR OUTPUT TWO: COMMENT ALL COURSE CORRECTIONS OUT, ENSURE SHIP IS USING SHIP_ORBIT
# FOR OUTPUT THREE: COMMENT OUT COURSE CORRECTION THRE, ENSURE SHIP IS USING SHIP_ORBIT
# FOR OUTPUT FOUR: INCLUDE ALL COURSE CORRECTIONS, ENSURE SHIP IS USING SHIP_ORBIT
    if t_array[step] == course_correction_sec: 
        print("COURSE CORRECTION ONE")
        # -0.053 and 0.17 are pretty good
        #v = (vx_ship_array[step]**2 + vy_ship_array[step]**2)**0.5
        #vx_ship_array[step] += -0.053
        #vy_ship_array[step] += 0.1705
        #vf = (vx_ship_array[step]**2 + vy_ship_array[step]**2)**0.5
        #print(vf-v)
    

    if t_array[step] == course_correction_2_sec: 
        print("COURSE CORRECTION TWO")
        #vy_ship_array[step] += -2


    if t_array[step] == 268491000: # closest approach time
        print("COURSE CORRECTION THREE")
        a = vx_ship_array[step]
        b = vy_ship_array[step]
        #vx_ship_array[step] *= 0.02529551834068018
        #vy_ship_array[step] *= 0.02529551834068018
        c = vx_ship_array[step]
        d = vy_ship_array[step]


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
        #break
    if ship_pluto_dist < body_data.pluto_hill_sphere:
        enter_pluto_hill_sphere = True
        pluto_hill_sphere_step.append(step)

np.savetxt("vx_ship_array.txt", vx_ship_array)
np.savetxt("vy_ship_array.txt", vy_ship_array)
    
np.savetxt("pluto_closest_approach_array.txt", pluto_closest_approach_array)

#   JUPITER CLOSEST APPROACH
    # finding minimum value in closest approach array
jupiter_closest_approach_r = jupiter_closest_approach_array[0][0] # assume the first element has the minimum r value
for i in range(1, len(jupiter_closest_approach_array)): # iterate over the remaining elements
    if jupiter_closest_approach_array[i][0] < jupiter_closest_approach_r: # compare r value with current minimum
        jupiter_closest_approach_r = jupiter_closest_approach_array[i][0] # update minimum r value
    
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
print("Jupiter closest approach r (km):", jupiter_closest_approach_r-body_data.jupiter_radius) 
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

if enter_pluto_hill_sphere == True:
    print("----------ENTER PLUTO HILL SPHERE----------")
    print("Ship entered Pluto's hill sphere at step:", pluto_hill_sphere_step[0])
    print("Ship entered Pluto's hill sphere at time (s):", t_array[pluto_hill_sphere_step[0]])
    #print("Ship entered Pluto's hill sphere on:", enter_pluto_hill_sphere_date.strftime('%Y-%m-%d %H:%M:%S'))
    print("Ship entered Pluto's hill sphere at x (km):", x_ship_array[pluto_hill_sphere_step[0]])
    print("Ship entered Pluto's hill sphere at y (km):", y_ship_array[pluto_hill_sphere_step[0]])
    print("Ship entered Pluto's hill sphere at vx (km/s):", vx_ship_array[pluto_hill_sphere_step[0]])
    print("Ship entered Pluto's hill sphere at vy (km/s):", vy_ship_array[pluto_hill_sphere_step[0]])
    print("Ship entered Pluto's hill sphere at v (km/s):", ((((vx_ship_array[pluto_hill_sphere_step[0]])**2) + ((vy_ship_array[pluto_hill_sphere_step[0]])**2))**0.5))

print("----------PLUTO CLOSEST APPROACH----------")
print("Pluto closest approach r (km):", pluto_closest_approach_r-body_data.pluto_radius) 
print("Pluto closest approach t (s):", t_array[pluto_closest_approach_t])
print("Pluto closest approach x (km):", x_ship_array[pluto_closest_approach_t])
print("Pluto closest approach y (km):", y_ship_array[pluto_closest_approach_t])
print("Pluto closest approach vx (km/s):", vx_ship_array[pluto_closest_approach_t])
print("Pluto closest approach vy (km/s):", vy_ship_array[pluto_closest_approach_t])
print("Pluto closest approach v (km/s):", ((((vx_ship_array[pluto_closest_approach_t])**2) + ((vy_ship_array[pluto_closest_approach_t])**2))**0.5))
print("Pluto closest approAch date:", pluto_closest_approach_date.strftime('%Y-%m-%d %H:%M:%S'))

if enter_pluto_hill_sphere == True:

    print("----------EXIT PLUTO HILL SPHERE----------")
    print("Ship exited Pluto's hill sphere at step:", pluto_hill_sphere_step[-1])
    print("Ship exited Pluto's hill sphere at time (s):", t_array[pluto_hill_sphere_step[-1]])
    #print("Ship exited Pluto's hill sphere on:", exit_pluto_hill_sphere_date.strftime('%Y-%m-%d %H:%M:%S'))
    print("Ship exited Pluto's hill sphere at x (km):", x_ship_array[pluto_hill_sphere_step[-1]])
    print("Ship exited Pluto's hill sphere at y (km):", y_ship_array[pluto_hill_sphere_step[-1]])
    print("Ship exited Pluto's hill sphere at vx (km/s):", vx_ship_array[pluto_hill_sphere_step[-1]])
    print("Ship exited Pluto's hill sphere at vy (km/s):", vy_ship_array[pluto_hill_sphere_step[-1]])
    print("Ship exited Pluto's hill sphere at v (km/s):", ((((vx_ship_array[pluto_hill_sphere_step[-1]])**2) + ((vy_ship_array[pluto_hill_sphere_step[-1]])**2))**0.5))
    print("Velocity increase (km/s) due to PGA:", ((((vx_ship_array[pluto_hill_sphere_step[-1]])**2) + ((vy_ship_array[pluto_hill_sphere_step[-1]])**2))**0.5) - ((((vx_ship_array[pluto_hill_sphere_step[0]])**2) + ((vy_ship_array[pluto_hill_sphere_step[0]])**2))**0.5))

#print("2: JAT jupiter vx:", vx_jupiter_array[159892])
#print("2: JAT jupiter vy:", vy_jupiter_array[159892])
#print("2:JDT jupiter vx:", vx_jupiter_array[187172])
#print("2: JDT jupiter vx:", vy_jupiter_array[187172])

print("3: JAT jupiter vx:", vx_jupiter_array[160108])
print("3: JAT jupiter vy:", vy_jupiter_array[160108])
print("3:JDT jupiter vx:", vx_jupiter_array[187664])
print("3: JDT jupiter vx:", vy_jupiter_array[187664])


fig, graph = plt.subplots()

# below 15 and 15 for jupiter encounter graphgs, 15 adn 10 for whole solar system
fig.set_figheight(15)
fig.set_figwidth(15)
#plt.rcParams["figure.figsize"] = (2560/2, 1440)
#2560 1440
# planets
#plt.plot(x_mercury_array/AU, y_mercury_array/AU, color='brown', label='Mercury')
#plt.plot(x_venus_array/AU, y_venus_array/AU, color='orange', label='Venus')
#plt.plot(x_earth_array/AU, y_earth_array/AU, color='cyan', label='Earth')
#plt.plot(x_mars_array/AU, y_mars_array/AU, color='red', label='Mars')
#plt.plot(x_jupiter_array/AU, y_jupiter_array/AU, color='indianred', label='Jupiter')
#plt.plot(x_saturn_array/AU, y_saturn_array/AU, color='brown', label='Saturn')
#plt.plot(x_uranus_array/AU, y_uranus_array/AU, color='dodgerblue', label='Uranus')
#plt.plot(x_neptune_array/AU, y_neptune_array/AU, color='blue', label='Neptune')
plt.plot(x_pluto_array/AU, y_pluto_array/AU, color='khaki', label='Pluto')

# ships
plt.scatter(x_ship_array/AU, y_ship_array/AU, color='black',  label='Ship (JGA)', s=1, marker='X')
plt.plot(x_ship_array/AU, y_ship_array/AU, color='black', label='Ship (JGA)')

#plt.plot(x_ship_array_n/AU, y_ship_array_n/AU, color='grey', label='Ship (NO JGA)')
#plt.plot(x_positions, y_positions, color='green', label='New Horizons Data')


# centering
graph.spines.left.set_position('zero')
graph.spines.right.set_color('none')
graph.spines.bottom.set_position('zero')
graph.spines.top.set_color('none')
graph.xaxis.set_ticks_position('bottom')
graph.yaxis.set_ticks_position('left')

 # axes
# for whole solar system
#graph.set_xlim([-40, 40])
#graph.set_ylim([-40, 40])


graph.xaxis.set_major_locator(plt.MaxNLocator(20))
graph.yaxis.set_major_locator(plt.MaxNLocator(20))

graph.set_aspect('equal', adjustable='box')

# for zoom at jupiter encounter
#graph.set_xlim(-2.10, -2.07)
#graph.set_ylim(-4.94, -4.90)
#graph.spines['left'].set_position(('data', -2.10))
#graph.spines['bottom'].set_position(('data', -4.94))

# for zoom at pluto insertion
#graph.set_xlim(6.8953078*AU, 6.8955038*AU)
#graph.set_ylim(-31.9328357*AU, -31.9326293*AU)
#graph.spines['left'].set_position(('data', 6.8953078*AU))
#graph.spines['bottom'].set_position(('data', -31.9328357*AU))
#graph.get_xaxis().get_major_formatter().set_useOffset(False)
#graph.get_yaxis().get_major_formatter().set_useOffset(False)
#graph.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
#graph.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
# for zoom at pluto insertion

# points of interest
# output two
#plt.plot(-312894207.437159/AU, -735563204.958764/AU, 'X', color='blue', label="Jupiter Closest Approach")

# output three and four
#plt.plot(-313237799.494571/AU, -735048532.817679/AU, 'X', color='blue', label="Jupiter Closest Approach")
    # output three
#plt.plot(1031535499.08331/AU, -4777081873.87396/AU, 'X', color='blue', label="Pluto Closest Approach at 4100km")

#plt.axis('equal')
plt.legend(loc='upper right')
#plt.legend(loc='lower right')
plt.xlabel('Distance from Sun in x-direction (AU)', x=0.57, fontsize=11)
plt.ylabel('Distance from Sun in y-direction (AU)', loc='bottom', fontsize=11)
#plt.title('Heliocentric Orbits of the Considered Bodies')
plt.xticks(rotation=90)
plt.show()
#fig.savefig('output three jupiter encounter.png', format='png', dpi=1200)



fig, graph = plt.subplots()

fig.set_figheight(8)
fig.set_figwidth(8) #6 for zoom, 8 for normal
t_array = t_array[:-1]
y_array = t_array/31536000 # in years

# for zoom at velocity increase for output two
#graph.set_xlim(0.9, 1.3)
#graph.set_ylim(17.5, 34)
#graph.spines['left'].set_position(('data', 0.9))
#graph.spines['bottom'].set_position(('data', 17.5))

# for zoom at velocity increase for output three
#graph.set_xlim(0.7, 1.3)
#graph.set_ylim(19, 25)
#graph.spines['left'].set_position(('data', 0.7))
#graph.spines['bottom'].set_position(('data', 19))

# for zoom at velocity increase for velocity comparison graph
#graph.set_xlim(1, 1.2)
#graph.set_ylim(17, 33.5)
#graph.spines['left'].set_position(('data', 1))
#graph.spines['bottom'].set_position(('data', 17))



#from velocity_comparison_graph import course_correction_velocities
#from velocity_comparison_graph import no_course_correction_velocities
#plt.plot(y_array, no_course_correction_velocities, color='blue',  label='Ship (JGA, no course correction)')
#plt.plot(y_array, course_correction_velocities, color='gold',  label='Ship (JGA, course correction')

plt.plot(y_array, ship_velocity_array, color='red',  label='Ship (JGA)')
plt.plot(y_array, ship_velocity_array_n, color='blue',  label='Ship (NO JGA)')
plt.plot(years, new_horizons_velocity_array, color='black', label='New Horizons')
plt.legend(fontsize=11, loc='upper right')
plt.xlabel('Time Since Launch (Years)', fontsize=11)
plt.ylabel('Heliocentric Velocity (km/s)', fontsize=11) 
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.show()
#fig.savefig('output four brake velocity.png', format='png', dpi=1200)