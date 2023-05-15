import math
import scipy
from scipy import constants

#values in au
earth_semimajoraxis = 1.00*149597870691
mars_semimajoraxis = 1.52366*149597870691

spaceship_semimajoraxis_mars_mission = (earth_semimajoraxis + 
                                        mars_semimajoraxis)/2

#kepler's law T**2=(a^3*4*pi**2)/(G*M_sun)
m_sun = 1.98847*10**30 #kg
#mars
spaceship_timeperiod_mars_mission=(((spaceship_semimajoraxis_mars
    _mission**3)*4*(constants.pi**2))/(constants.G*m_sun))**0.5
mars_timeperiod = (((mars_semimajoraxis**3)*4*
        (constants.pi**2))/(constants.G*m_sun))**0.5
mars_mission_time = spaceship_timeperiod_mars_mission/2

# alpha = (2*constants.pi*spaceship_timeperiod)/mars_timeperiod
mars_spaceship_arrival_angle = 360 * (mars_mission_time/mars_timeperiod) 
# angle between earth and mars
earth_mars_launch_angle = 180 - mars_spaceship_arrival_angle 

print("MARS MISSION STATS")
print("The time period of Mars is", mars_timeperiod/(60*60*24*365), 
      "years") # in years
print("The mission will take", mars_mission_time/(60*60*24*365), 
      "years") # in years
print("The semimajor axis of the spaceship is", 
      spaceship_semimajoraxis_mars_mission, "metres or", 
      spaceship_semimajoraxis_mars_mission/149597870691, "AU")
print("Mars needs to be", mars_spaceship_arrival_angle, 
      "degrees from the point of spaceship arrival at the 
      time of launch")
print("Hence, the angle between Earth and Mars at this time 
      needs to be", earth_mars_launch_angle, "degrees")

