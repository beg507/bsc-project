import math
import scipy
from scipy import constants

# stage one varibales

velocity_earth_departure = 0 
earth_departure_position = 0
mass_earth = 0 
semimajor_axis_ship_at_earth = 0
velocity_ship_earth_departure = scipy.sqrt((constants.G*mass_earth)/semimajor_axis_ship_at_earth) 
# ^ escape velocity at the earth SOI

# stage two varibales

# velocity_ship_earth_departure carries over


velocity_jupiter_jupiter_arrival = 0
jupiter_arrival_position = 0

hyp_exc_velocity_jupiter_arrival = velocity_ship_earth_departure - velocity_jupiter_jupiter_arrival
ship_radius_at_jupiter = 0
mass_jupiter = 0

ship_eccentricity = 1 + (((hyp_exc_velocity_jupiter_arrival)**2*ship_radius_at_jupiter)/(constants.G*mass_jupiter))
deflection_angle = 2*scipy.arcsin(1/ship_eccentricity)

velocity_jupiter_jupiter_departure = 0

hyp_exc_velocity_jupiter_departure = ((hyp_exc_velocity_jupiter_arrival*scipy.cos(deflection_angle))+(hyp_exc_velocity_jupiter_arrival*scipy.sin(deflection_angle)))
velocity_ship_jupiter_departure = hyp_exc_velocity_jupiter_departure + velocity_jupiter_jupiter_departure 
# velocity_jupiter_jupiter_departure comes from simulation/looping, set to 0 for now


# stage three
# velocity_ship_jupiter_departure carries over

mass_pluto = 0
radius_pluto = 0
velocity_delta_req_orbit_insertion = scipy.sqrt(((2*constants.G*mass_pluto)/(radius_pluto))+(velocity_ship_jupiter_departure)**2) - scipy.sqrt((constants.G*mass_pluto)/(radius_pluto))#

ship_effective_exhaust_velocity = 0 #depends on engine
mass_ratio = scipy.e**(velocity_delta_req_orbit_insertion/ship_effective_exhaust_velocity)
# mass ratio is initial mass over final mass, from this can determine the mass needed at the point of earth departure

#mass_ship_final = mass_ship_initial - mass_propellant












