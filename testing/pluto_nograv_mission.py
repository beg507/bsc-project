import math
import scipy
from scipy import constants

#values in au
earth_semimajoraxis = 1.00*149597870691
pluto_semimajoraxis = 39.5294*149597870691

spaceship_semimajoraxis_pluto_nograv_mission = (earth_semimajoraxis + pluto_semimajoraxis)/2

#kepler's law T**2=(a^3*4*pi**2)/(G*M_sun)
m_sun = 1.98847*10**30 #kg

#pluto no grav
spaceship_timeperiod_pluto_nograv_mission = (((spaceship_semimajoraxis_pluto_nograv_mission**3)*4*(constants.pi**2))/(constants.G*m_sun))**0.5
pluto_timeperiod = (((pluto_semimajoraxis**3)*4*(constants.pi**2))/(constants.G*m_sun))**0.5
pluto_nograv_mission_time = spaceship_timeperiod_pluto_nograv_mission/2
pluto_nograv_mission_time_ver2 = scipy.pi*scipy.sqrt((spaceship_semimajoraxis_pluto_nograv_mission)**3/(constants.G*m_sun))

#alpha = (2*constants.pi*spaceship_timeperiod)/mars_timeperiod
pluto_nograv_spaceship_arrival_angle = 360 * (pluto_nograv_mission_time/pluto_timeperiod) 
earth_pluto_launch_angle = 180 - pluto_nograv_spaceship_arrival_angle

print("PLUTO MISSION STATS - NO GRAVITY ASSIST")
print("The time period of Pluto is", pluto_timeperiod/(60*60*24*365), "years") # in years
print("The mission will take", pluto_nograv_mission_time/(60*60*24*365), "years") # in years
print("The semimajor axis of the spaceship is", spaceship_semimajoraxis_pluto_nograv_mission, "metres or", spaceship_semimajoraxis_pluto_nograv_mission/149597870691, "AU")
print("Pluto needs to be", pluto_nograv_spaceship_arrival_angle, "degrees from the point of spaceship arrival at the time of launch")
print("Hence, the angle between Earth and Pluto at this time needs to be", earth_pluto_launch_angle, "degrees")
print(pluto_nograv_mission_time_ver2/(60*60*24*365))