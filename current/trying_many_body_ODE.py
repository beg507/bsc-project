import numpy as np
import matplotlib.pyplot as plt
import math
plt.style.use( 'dark_background' )

import ephemeris as eph
import body_data
from body_data import *

def two_body_ode_sun( t, state ): #newton's law of graviataion 
	r = state[ :3 ]
	a = (-(body_data.sun_mass*body_data.G_km) * r / np.linalg.norm( r ) ** 3)
	# np.linalg.norm is used to calculate the norm of a vector
	return np.array( [ state[ 2 ], state[ 3 ], a[ 0 ], a[ 1 ]] ) # (vx, vy, ax, ay) returned state vector using statei

def two_body_ode_jupiter( t, state ): #newton's law of graviataion 
	r = state[ :3 ]
	a = (-(body_data.jupiter_mass*body_data.G_km) * r / np.linalg.norm( r ) ** 3)
	# np.linalg.norm is used to calculate the norm of a vector
	return np.array( [ state[ 2 ], state[ 3 ], a[ 0 ], a[ 1 ]] ) # (vx, vy, ax, ay) returned state vector using statei

def runge_kutta_4_step( f, t, y, h ): # f=function, t= simulation time, y= current state, h= step size
	k1 = f( t, y )
	k2 = f( t + 0.5 * h, y + 0.5 * k1 * h )
	k3 = f( t + 0.5 * h, y + 0.5 * k2 * h )
	k4 = f( t +       h, y +       k3 * h )

	return y + h / 6.0 * ( k1 + 2 * k2 + 2 * k3 + k4 ) # prediction of new state at the next step (rx, ry, vx, vy)

# initial states (sun centric)
statei_ship      = [eph.x_pos_earth, eph.y_pos_earth, -11.2+eph.x_vel_earth, eph.y_vel_earth ]
statei_earth      = [eph.x_pos_earth, eph.y_pos_earth, eph.x_vel_earth, eph.y_vel_earth ]  # starting state vector (rx, ry, vx, vy)
statei_jupiter      = [eph.x_pos_jupiter, eph.y_pos_jupiter, eph.x_vel_jupiter, eph.y_vel_jupiter]
statei_pluto      = [eph.x_pos_pluto, eph.y_pos_pluto, eph.x_vel_pluto, eph.y_vel_pluto ]

# initial states (jupiter centric)
ship_jupiter_distance =  abs(math.sqrt(( eph.x_pos_earth - eph.x_pos_jupiter)**2 + ( eph.y_pos_earth - eph.y_pos_jupiter)**2) )
ship_jupiter_distance_x = eph.x_pos_earth - eph.x_pos_jupiter
ship_jupiter_distance_y = eph.y_pos_earth - eph.y_pos_jupiter

statei_ship_j = [ship_jupiter_distance_x, ship_jupiter_distance_y, -11.2+eph.x_vel_earth, eph.y_vel_earth  ]


# time and steps
tspan       = 60 * 60 * 24 * 365 * 10              # seconds, currently 1 y 1 m
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
states_ship_j     = np.zeros( ( steps, 4 ) )
states_ship_j[ 0 ] = statei_ship_j

for step in range( steps - 1 ):
    # gives new positions and velocities for plotting
    states_earth[ step + 1 ] = runge_kutta_4_step(two_body_ode_sun, ets[ step ], states_earth[ step ], dt )
    states_jupiter[ step + 1 ] = runge_kutta_4_step(two_body_ode_sun, ets[ step ], states_jupiter[ step ], dt )
    states_pluto[ step + 1 ] = runge_kutta_4_step(two_body_ode_sun, ets[ step ], states_pluto[ step ], dt )
    #states_ship[ step + 1 ] = runge_kutta_4_step(two_body_ode_sun, ets[ step ], states_ship[ step ], dt )
    
    # gives the distance between the bodies (earth and jupiter for example)
    states_ship_j[ step + 1 ] = runge_kutta_4_step(two_body_ode_jupiter, ets[ step ], states_ship_j[ step ], dt )




# plotting
fig, graph = plt.subplots()

x_earth, y_earth, a, b = states_earth.T # splitting array
graph.plot(x_earth,y_earth)

x_jupiter, y_jupiter, a, b= states_jupiter.T
graph.plot(x_jupiter,y_jupiter)

x_pluto, y_pluto, a, b = states_pluto.T
graph.plot(x_pluto,y_pluto)

x_ship, y_ship, a, b = states_ship.T
graph.plot(x_ship,y_ship)

central_body = plt.Circle((0, 0), radius=body_data.sun_radius, color='yellow')
plt.gca().add_patch(central_body)

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