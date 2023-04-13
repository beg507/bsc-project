import numpy as np
import matplotlib.pyplot as plt
import math

import ephemeris as eph
import body_data
from body_data import *

     # HELIOCENTRIC
def two_body_ode (t, state): #newton's law of gravitation
    r = state[:2]
    a = (-(body_data.sun_mass *body_data.G_km) * r / np.linalg.norm(r)**3)
    # np.linalg.norm is used to calculate the norm of a vector
    return np.array([state[2], state[3], a[0], a[1]])

def two_body_ode_jupiter (t, state): #newton's law of gravitation
    r = state[:2]
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
enter_count = 0
exit_step = []
exited = 0

inside_hill_sphere_jupiter = False

#JAT LISTS
ship_jat_states = []
earth_jat_states = []
jupiter_jat_states = []
pluto_jat_states = []

def angle_between(x1,y1,x2,y2):
    return math.degrees(math.atan2(y2-y1, x2-x1))

for step in range( steps - 1 ):
    
    states_earth[ step + 1 ] = runge_kutta_4_step(two_body_ode, ets[ step ], states_earth[ step ], dt )
    states_jupiter[ step + 1 ] = runge_kutta_4_step(two_body_ode, ets[ step ], states_jupiter[ step ], dt )
    states_pluto[ step + 1 ] = runge_kutta_4_step(two_body_ode, ets[ step ], states_pluto[ step ], dt )
    
    jupiter_pos = states_jupiter[step + 1, :2]

    print("flag 1:", inside_hill_sphere_jupiter)
    if inside_hill_sphere_jupiter == False:
        print("flag 1.5:", inside_hill_sphere_jupiter)
        states_ship[ step + 1 ] = runge_kutta_4_step(two_body_ode, ets[ step ], states_ship[ step ], dt )
        
        print("flag 2:", inside_hill_sphere_jupiter)
        #print( "ship_pos vs jdt_dist", np.linalg.norm(ship_pos), jdt_dist)

        ship_pos_approach = states_ship[step + 1, :2]
        
        jat_dist = np.linalg.norm(jupiter_pos) - np.linalg.norm(ship_pos_approach) # distance between jupiter and ship at jupiter arrival time

    if abs(jat_dist) < abs(body_data.jupiter_hill_sphere):
        ship_jat_states.append(states_ship[step])
        earth_jat_states.append(states_earth[step])
        jupiter_jat_states.append(states_jupiter[step])
        pluto_jat_states.append(states_pluto[step])
        break
 
print(ship_jat_states)
print(earth_jat_states)
print(jupiter_jat_states)
print(pluto_jat_states)