import math
import scipy
from scipy import constants

#values in AU
earth_semimajoraxis = 1.00*149597870691
mars_semimajoraxis = 1.52366*149597870691
spaceship_semimajoraxis = (earth_semimajoraxis + mars_semimajoraxis)/2

#kepler's law T**2=(a^3*4*pi**2)/(G*M_sun)
m_sun = 1.98847*10**30 #kg
spaceship_timeperiod = (((spaceship_semimajoraxis**3)*4*(constants.pi**2))/(constants.G*m_sun))**0.5
mars_timeperiod = (((mars_semimajoraxis**3)*4*(constants.pi**2))/(constants.G*m_sun))**0.5

mission_time = spaceship_timeperiod/2

#alpha = (2*constants.pi*spaceship_timeperiod)/mars_timeperiod
alpha = 360 * (mission_time/mars_timeperiod) # this is the angle between mars at B and at C (angle of mars from C)
beta = 180 - alpha # angle between earth and mars

print("The time period of mars is", mars_timeperiod/(60*60*24*365), "years") # in years
print("The mission will take", mission_time/(60*60*24*365), "years") # in years
print("Mars needs to be", alpha, "degrees from the point of spaceship arrival at the time of launch")
print("Hence, the angle between Earth and Mars at this time needs to be", beta, "degrees")