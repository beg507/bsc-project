import scipy
from scipy import constants
G_km = 6.67408e-20  # km^3/(kg*s^2)

AU = 149597870.691 #km
sun_mass = float(1.98892*10**30) #kg
sun_radius = 696340

mercury_radius = 2440 
mercury_mass = 3.302 * 10**23
mercury_a = AU * 0.4
mercury_hill_sphere = mercury_a * (mercury_mass/(3*sun_mass))**(1/3)

venus_radius = 6051.84
venus_mass = 48.685 * 10**23
venus_a = AU * 0.7
venus_hill_sphere = venus_a * (venus_mass/(3*sun_mass))**(1/3)

earth_radius = 6378.137 #km
earth_mass = 5.97219 * 10**24 #kg
earth_a = AU * 1
earth_hill_sphere = earth_a * (earth_mass/(3*sun_mass))**(1/3)

mars_radius = 3389.92
mars_mass = 6.4171 * 10**23
mars_a = AU * 1.5
mars_hill_sphere = mars_a * (mars_mass/(3*sun_mass))**(1/3)

jupiter_radius = 69911
jupiter_mass = 1.89813 *10**27
jupiter_a = AU * 5.2
jupiter_hill_sphere = jupiter_a * (jupiter_mass/(3*sun_mass))**(1/3)

saturn_radius = 58232
saturn_mass = 5.6834 *10**26
saturn_a = AU * 9.6
saturn_hill_sphere = saturn_a * (saturn_mass/(3*sun_mass))**(1/3)

uranus_radius = 25362
uranus_mass = 86.813 *10**24
uranus_a = AU * 19.2
uranus_hill_sphere = uranus_a * (uranus_mass/(3*sun_mass))**(1/3)

neptune_radius = 24624
neptune_mass = 102.409 *10**24
neptune_a = AU * 30
neptune_hill_sphere = neptune_a * (neptune_mass/(3*sun_mass))**(1/3)

pluto_radius = 1188.3
pluto_mass = 1.307 *10**22
pluto_a = AU * 39.5
pluto_hill_sphere = pluto_a * (pluto_mass/(3*sun_mass))**(1/3)
