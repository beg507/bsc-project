import numpy as np
import matplotlib.pyplot as plt
import math

import ephemeris as eph
import body_data
from body_data import *

     # HELIOCENTRIC
def two_body_ode (t, state): #newton's law of gravitation
    r = state[:3]
    a = (-(body_data.sun_mass *body_data.G_km) * r / np.linalg.norm(r)**3)
    # np.linalg.norm is used to calculate the norm of a vector
    return np.array([state[2], state[3], a[0], a[1]])

def two_body_ode_jupiter (t, state): #newton's law of gravitation
    if inside_hill_sphere_jupiter == True:
        r = states_ship[step,:3]
        a = (-(body_data.jupiter_mass *body_data.G_km) * r / np.linalg.norm(r)**3)
        # np.linalg.norm is used to calculate the norm of a vector
        return np.array([state[2], state[3], a[0], a[1]])
 

def runge_kutta_4_step( f, t, y, h ): # f=function, t= simulation time, y= current state, h= step size
	k1 = f( t, y )
	k2 = f( t + 0.5 * h, y + 0.5 * k1 * h )
	k3 = f( t + 0.5 * h, y + 0.5 * k2 * h )
	k4 = f( t +       h, y +       k3 * h )

	return y + h / 6.0 * ( k1 + 2 * k2 + 2 * k3 + k4 ) # prediction of new state at the next step (position and velocity)

# initial states
statei_ship      = [eph.x_pos_ship, eph.y_pos_ship, eph.x_vel_ship, eph.y_vel_ship ]
statei_earth      = [eph.x_pos_earth, eph.y_pos_earth, eph.x_vel_earth, eph.y_vel_earth ]  # starting state vector (rx, ry, vx, vy)
statei_jupiter      = [eph.x_pos_jupiter, eph.y_pos_jupiter, eph.x_vel_jupiter, eph.y_vel_jupiter]
statei_pluto      = [eph.x_pos_pluto, eph.y_pos_pluto, eph.x_vel_pluto, eph.y_vel_pluto ]

# time and steps
tspan       = 60 * 60 * 24 * 365 *10        # seconds, currently 10y
dt          = 3000                        # seconds
steps       = int( tspan / dt )
ets         = np.zeros( ( steps, 1 ) )

# empty arrays
states_earth      = np.zeros( ( steps, 4 ) )
states_earth[ 0 ] = statei_earth
states_jupiter     = np.zeros( ( steps, 4 ) )
states_jupiter[ 0 ] = statei_jupiter
states_pluto     = np.zeros( ( steps, 4 ) )
states_pluto[ 0 ] = statei_pluto
states_ship     = np.zeros( ( steps, 4 ) )
states_ship[ 0 ] = statei_ship

enter_step = []
entered = 0
exit_step = []
exited = 0

def angle_between(x1,y1,x2,y2):
    return math.degrees(math.atan2(y2-y1, x2-x1))

for step in range( steps - 1 ):
    
    states_earth[ step + 1 ] = runge_kutta_4_step(two_body_ode, ets[ step ], states_earth[ step ], dt )
    states_jupiter[ step + 1 ] = runge_kutta_4_step(two_body_ode, ets[ step ], states_jupiter[ step ], dt )
    states_pluto[ step + 1 ] = runge_kutta_4_step(two_body_ode, ets[ step ], states_pluto[ step ], dt )
    states_ship[ step + 1 ] = runge_kutta_4_step(two_body_ode, ets[ step ], states_ship[ step ], dt )

    ship_pos = states_ship[step + 1, :2]
    jupiter_pos = states_jupiter[step + 1, :2]
    jat_dist = np.linalg.norm(ship_pos - jupiter_pos) # distance between jupiter and ship at jupiter arrival time
    jdt_dist = np.linalg.norm(jupiter_pos) + body_data.jupiter_hill_sphere # distance between far edge of hill sphere and sun T jupiter departure time

    if jat_dist < body_data.jupiter_hill_sphere:
        inside_hill_sphere_jupiter = True
        entered += 1
        if entered >= 1:
            enter_step.append(step)
            jat_jupiter_vx = states_jupiter[enter_step, 2]
            jat_jupiter_vy = states_jupiter[enter_step, 3]
            jat_ship_vx = states_ship[enter_step,2]
            jat_ship_vy = states_ship[enter_step,3]
            jat_hyp_ex_vx_ship = jat_ship_vx - jat_jupiter_vx
            jat_hyp_ex_vy_ship = jat_ship_vy - jat_jupiter_vy

        
            if step == enter_step:
                for jat_step in range( steps - 1 ):
                    states_ship = [states_ship[step, 0], states_ship[step, 1], jat_hyp_ex_vx_ship, jat_hyp_ex_vy_ship]
                    states_ship[ jat_step + 1 ] = runge_kutta_4_step(two_body_ode_jupiter, ets[ jat_step ], states_ship[ jat_step ], dt )

    if jdt_dist < np.linalg.norm(ship_pos):
        inside_hill_sphere_jupiter = False
        exited += 1
        if exited >= 1:
            exit_step.append(step)
            jdt_jup_x = states_jupiter[exit_step, 0]
            jdt_jup_y = states_jupiter[exit_step, 1]
            jdt_ship_x = states_ship[exit_step, 0]
            jdt_ship_y = states_ship[exit_step, 1]

            deflection_angle = angle_between(jdt_jup_x, jdt_jup_y, jdt_ship_x, jdt_jup_y)

            jdt_jupiter_vx = states_jupiter[exit_step, 2]
            jdt_jupiter_vy = states_jupiter[exit_step, 3]

            jdt_hyp_ex_vx_ship = jat_hyp_ex_vx_ship * math.cos(deflection_angle)
            jdt_hyp_ex_vy_ship = jat_hyp_ex_vy_ship * math.sin(deflection_angle)

            jdt_ship_vx = jdt_hyp_ex_vx_ship + jdt_jupiter_vx
            jdt_ship_vy = jdt_hyp_ex_vy_ship + jdt_jupiter_vy

            if step == exit_step:
                for jdt_step in range( steps - 1 ):
                    states_ship = [states_ship[step, 0], states_ship[step, 1], jdt_ship_vx, jdt_ship_vy]
                    states_ship[ jdt_step + 1 ] = runge_kutta_4_step(two_body_ode, ets[ jdt_step ], states_ship[ jdt_step ], dt )


        # print("Ship has entered Jupiter's Hill Sphere at step", step, "and distance to Jupiter is", dist, "km")
        # print("Inside hill sphere Jupiter is", inside_hill_sphere_jupiter)
           
#print( states )
#print("enter step value: ", enter_step)
#print("At Jupiter Arrival Time (JAT):")
#print("x vel ship:", jat_ship_vx, "km/s")
#print("y vel ship:", jat_ship_vy, "km/s")
#print("x vel jupiter:", jat_jupiter_vx, "km/s")
#print("y vel jupiter:", jat_jupiter_vy, "km/s")

#print("exit step value: ", exit_step)
#print("At Jupiter Departure Time (JDT):")
#print("x vel ship:", jdt_ship_vx, "km/s")
#print("y vel ship:", jdt_ship_vy, "km/s")
#print("x vel jupiter:", jdt_jupiter_vx, "km/s")
#print("y vel jupiter:", jdt_jupiter_vy, "km/s")

#print("Deflection angle:",deflection_angle)

print("enter step:", enter_step)
print("exit step:", exit_step)

# PLOTTING
plt.style.use( 'dark_background' )
fig, graph = plt.subplots()

#          BODIES

central_body = plt.Circle((0, 0), radius=body_data.sun_radius, color='yellow')
plt.gca().add_patch(central_body)

x_ship, y_ship, a, b = states_ship.T
graph.plot(x_ship,y_ship, color='white')

x_earth, y_earth, a, b = states_earth.T # splitting array
graph.plot(x_earth,y_earth, color='cyan')

x_jupiter, y_jupiter, a, b= states_jupiter.T
graph.plot(x_jupiter,y_jupiter, color='khaki')

x_pluto, y_pluto, a, b = states_pluto.T
graph.plot(x_pluto,y_pluto, color='indianred')

#           HILL SPHERES

earth_hill_sphere = plt.Circle((x_earth[-1], y_earth[-1]), radius=body_data.earth_hill_sphere, color='cyan', fill=False, linestyle='--')
plt.gca().add_patch(earth_hill_sphere)

jupiter_hill_sphere = plt.Circle((x_jupiter[-1], y_jupiter[-1]), radius=body_data.jupiter_hill_sphere, color='khaki', fill=False, linestyle='--')
plt.gca().add_patch(jupiter_hill_sphere)

pluto_hill_sphere = plt.Circle((x_pluto[-1], y_pluto[-1]), radius=body_data.pluto_hill_sphere, color='indianred', fill=False, linestyle='--')
plt.gca().add_patch(pluto_hill_sphere)


graph.spines.left.set_position('zero')
graph.spines.right.set_color('none')
graph.spines.bottom.set_position('zero')
graph.spines.top.set_color('none')
graph.xaxis.set_ticks_position('bottom')
graph.yaxis.set_ticks_position('left')

graph.set_xlim([-40*149597870.691, 40*149597870.691]) # set to 40AU to see whole solar system up to pluto
graph.set_ylim([-40*149597870.691, 40*149597870.691])

graph.set_aspect('equal', adjustable='box')

#plt.rcParams["figure.figsize"] = (20,20)

plt.show()