import scipy
from scipy import constants
G_km = constants.G * 10**-9 # km**3/ kg / s**2

# SOI eqn 12-2 in textbook
# r_SOI = (m_planet/m_sun)**(2/5) * a_planet

# caculate semimajor axis from time period
# a = (GM ((T/2pi)**2))**(1/3)

AU = 149597870.691 #km
sun_mass = 1.98892*10**30 #kg
sun_radius = 696340

mercury_radius = 2440 
mercury_mass = 3.302 * 10**23
mercury_a = AU * 0.4

venus_radius = 6051.84
venus_mass = 48.685 * 10**23
venus_a = AU * 0.7

earth_radius = 6378.137 #km
earth_mass = 5.97219 * 10**24 #kg
earth_a = AU * 1

mars_radius = 3389.92
mars_mass = 6.4171 * 10**23
mars_a = AU * 1.5

jupiter_radius = 69911
jupiter_mass = 189818722 *10**22
jupiter_a = AU * 5.2
print(jupiter_a)
jupiter_SOI = (jupiter_mass/sun_mass)**(2/5) * jupiter_a

saturn_radius = 58232
saturn_mass = 5.6834 *10**26
saturn_a = AU * 9.6

uranus_radius = 25362
uranus_mass = 86.813 *10**24
uranus_a = AU * 19.2

neptune_radius = 24624
neptune_mass = 102.409 *10**24
neptune_a = AU * 30

pluto_radius = 1188.3
pluto_mass = 1.307 *10**22
pluto_a = AU * 39.5

#planets = [sun, mercury 0.4, venus 0.7, earth 1, mars 1.5, jupiter 5.2, saturn 9.6, uranus 19.2, neptune 30, pluto 39.5]