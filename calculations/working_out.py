vx = 5.624321351590395 
vy = -17.2852972747014 
v = 18.177307076152815
dv = 17.503628379780427
nv = 0.6491075990653649
import numpy as np
v_attempt = np.sqrt((vx-5)**2 + (vy+17.465)**2)
print(v_attempt)
print(nv)

percent = 0.6491075990653649/18.177307076152815
print(percent)

import math

# Define the mass of the spacecraft (in kg)
m_ship = 500
m_pluto = 1.307 *10**22

# Define the initial velocity and position of the spacecraft (in m/s and m, respectively)
vx_ship = 5.631765042992041
vy_ship = -17.266556422953517
x_ship = 1028983287.4247708
y_ship = -4769429780.580613

# Define the initial velocity and position of Pluto (in m/s and m, respectively)
vx_pluto = 5.416075437506788
vy_pluto = 0.045713438697991764
x_pluto = 1029076927.0715779
y_pluto = -4777103020.101793
   
# Define the angle of approach for the spacecraft (in radians)
theta = math.pi / 4.0

# Calculate the total velocity of the spacecraft (in m/s)
v_ship = math.sqrt(vx_ship**2 + vy_ship**2)

# Calculate the angle of the spacecraft's velocity vector (in radians)
phi = math.atan2(vy_ship, vx_ship)

# Calculate the relative velocity of the spacecraft and Pluto (in m/s)
vx_rel = vx_ship - vx_pluto
vy_rel = vy_ship - vy_pluto
v_rel = math.sqrt(vx_rel**2 + vy_rel**2)

# Calculate the angle of the relative velocity vector (in radians)
alpha = math.atan2(vy_rel, vx_rel)
print(alpha)

# Calculate the impact parameter (in m)
b = math.sin(alpha - theta) * v_rel * (m_ship / (m_ship + m_pluto))

# Calculate the impact energy (in joules)
E = 0.5 * m_ship * v_ship**2

# Calculate the radius of the impact crater (in m)
r = 0.25 * abs(b)

# Print the results
print("Impact energy: ", E)
print("Radius of impact crater: ", r)