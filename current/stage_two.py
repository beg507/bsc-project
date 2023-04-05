import numpy as np
import matplotlib.pyplot as plt
import math

import ephemeris as eph
import body_data
from body_data import *


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
ship_jat_states_rel_sun      = [-3.13046084e+08, -6.78870376e+08,  2.28774961e-01, -1.96452835e+01] #stage_one.ship_jat_states
statei_jupiter      = [-3.45601297e+08, -7.22285635e+08,  1.16332927e+01, -5.01119309e+00]#stage_one.jupiter_jat_states
ship_jat_states_rel_jupiter = [-3.13046084e+08+3.45601297e+08, -6.78870376e+08+7.22285635e+08,  2.28774961e-01+1.16332927e+01, -1.96452835e+01+5.01119309e+00]
#ship_jat_states_rel_sun - statei_jupiter
print(ship_jat_states_rel_jupiter)
# time and steps
tspan       = 60 * 60 * 24 *20      # seconds, currently 10y
dt          = 3000                        # seconds
steps       = int( tspan / dt )
ets         = np.zeros( ( steps, 1 ) )

# empty arrays

states_ship     = np.zeros( ( steps, 4 ) )
states_ship[ 0 ] = ship_jat_states_rel_jupiter

#JAT LISTS
ship_jat_states = []
earth_jat_states = []
jupiter_jat_states = []
pluto_jat_states = []

def angle_between(x1,y1,x2,y2):
    return math.degrees(math.atan2(y2-y1, x2-x1))

for step in range( steps - 1 ):
    
    states_ship[ step + 1 ] = runge_kutta_4_step(two_body_ode_jupiter, ets[ step ], states_ship[ step ], dt )
    

#PLOTTING
plt.style.use( 'dark_background' )
fig, graph = plt.subplots()

#          BODIES

central_body = plt.Circle((0, 0), radius=body_data.jupiter_radius, color='blue')
plt.gca().add_patch(central_body)

x_ship, y_ship, a, b = states_ship.T
graph.plot(x_ship,y_ship, color='red')



graph.spines.left.set_position('zero')
graph.spines.right.set_color('none')
graph.spines.bottom.set_position('zero')
graph.spines.top.set_color('none')
graph.xaxis.set_ticks_position('bottom')
graph.yaxis.set_ticks_position('left')

graph.set_xlim([-50000000, 50000000]) # set to 40AU to see whole solar system up to pluto
graph.set_ylim([-50000000, 50000000])

graph.set_aspect('equal', adjustable='box')

#plt.rcParams["figure.figsize"] = (20,20)

plt.show()