import math
import scipy
from scipy import constants

#values in au https://www.windows2universe.org/our_solar_system/planets_orbits_table.html
earth_semimajoraxis = 1.00*149597870691
pluto_semimajoraxis = 39.5294*149597870691
jupiter_semimajoraxis = 5.2028*149597870691

spaceship_semimajoraxis_pluto_grav_mission_EtoJ = (earth_semimajoraxis + jupiter_semimajoraxis)/2
spaceship_semimajoraxis_pluto_grav_mission_JtoP = (jupiter_semimajoraxis + pluto_semimajoraxis)/2

#kepler's law T**2=(a^3*4*pi**2)/(G*M_sun)
m_sun = 1.98847*10**30 #kg

#pluto no grav
#spaceship_timeperiod_pluto_nograv_mission = (((spaceship_semimajoraxis_pluto_nograv_mission**3)*4*(constants.pi**2))/(constants.G*m_sun))**0.5
pluto_timeperiod = (((pluto_semimajoraxis**3)*4*(constants.pi**2))/(constants.G*m_sun))**0.5
jupiter_timeperiod = (((jupiter_semimajoraxis**3)*4*(constants.pi**2))/(constants.G*m_sun))**0.5

earth_to_jupiter_mission_time = scipy.pi*scipy.sqrt((spaceship_semimajoraxis_pluto_grav_mission_EtoJ)**3/(constants.G*m_sun)) 
jupiter_to_pluto_mission_time = scipy.pi*scipy.sqrt((spaceship_semimajoraxis_pluto_grav_mission_JtoP)**3/(constants.G*m_sun))
pluto_grav_mission_time = earth_to_jupiter_mission_time + jupiter_to_pluto_mission_time

#alpha = (2*constants.pi*spaceship_timeperiod)/mars_timeperiod

pluto_grav_spaceship_arrival_at_jupiter_angle = 360 * (earth_to_jupiter_mission_time/jupiter_timeperiod) 
pluto_grav_spaceship_arrival_at_pluto_angle = 360 * (pluto_grav_mission_time/pluto_timeperiod) 
earth_pluto_launch_angle = 180 - pluto_grav_spaceship_arrival_at_pluto_angle

print("PLUTO MISSION STATS - GRAVITY ASSIST")
print("The time period of Pluto is", pluto_timeperiod/(60*60*24*365), "years") # in years
print("It takes", earth_to_jupiter_mission_time/(60*60*24*365) , "years to get from Earth to Jupiter")
print("It takes", jupiter_to_pluto_mission_time/(60*60*24*365) , "years to get from Jupiter to Pluto")
print("The mission will take", pluto_grav_mission_time/(60*60*24*365), "years") # in years
print("Jupiter needs to be", pluto_grav_spaceship_arrival_at_jupiter_angle, "degrees from the point of spaceship arrival at the time of launch")
print("Pluto needs to be", pluto_grav_spaceship_arrival_at_pluto_angle, "degrees from the point of spaceship arrival at the time of launch")
print("Hence, the angle between Earth and Pluto at this time needs to be", earth_pluto_launch_angle, "degrees")
