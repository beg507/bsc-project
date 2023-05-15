import numpy as np
import matplotlib.pyplot as plt

x_positions = []
y_positions = []
vx_velocities = []
vy_velocities = []
days = []

AU = 149597870.691 #km

new_horizons_velocity_array = []
years = []
# open the text file and read the lines
with open('horizons_results.txt', 'r') as file:
    lines = file.readlines()

# iterate over each line in the text file
for line in lines:
    # strip any whitespace from the line
    line = line.strip()
    
    # check if the line is empty or only contains whitespace
    if not line:
        continue
    
    # split the line into a list using the comma as a delimiter
    data = line.split(',')
    
    # extract the x, y, vx, and vy positions from the list
    day = int(float(data[0]) - 2453755)  # Convert Julian date to day number
    x = float(data[2])
    y = float(data[3])
    vx = float(data[5])
    vy = float(data[6])
    
    days.append(day)
    x_positions.append(x/AU)
    y_positions.append(y/AU)
    vx_velocities.append(vx)
    vy_velocities.append(vy)
    new_horizons_velocity_array.append(((vx**2) + (vy**2))**0.5)
    years.append(day/365)

#plt.plot(years, new_horizons_velocity_array)
#plt.show()

# JUPITER CLOSEST APPROACH OF NEW HORIZONS USING HORIZONS WEB APP
#2007-Feb-28 05:43:00.0000,

jc_nh_x = -3.131742841017537E+08
jc_nh_y = -7.352750401407160E+08
jc_nh_vx = 1.214152321352474E+00
jc_nh_vy = -2.280196846161328E+01

ju_x = -3.111912594350986E+08
ju_y = -7.364191485271670E+08
ju_vx = 1.187367681560053E+01
ju_vy = -4.471119874556948E+00

new_horizonz_jupiter_closest_approach = ((ju_x**2-jc_nh_x**2) + (ju_y**2-jc_nh_y**2))**0.5
print(new_horizonz_jupiter_closest_approach)

# pluto closest approach date 2015-Jul-14 11:49:00.0000,  
pc_nh_x = 1.197735545200908E+09
pc_nh_y = -4.772375483443304E+09
pc_nh_vx = 5.536417311463418E+00
pc_nh_vy = 1.341557290113761E+01

pl_x = 1.197723230713286E+09
pl_y = -4.772375801947201E+09
pl_vx = 5.380120691094567E+00
pl_vy = 1.962096834307356E-01
new_horizonz_pluto_closest_approach = ((pl_x**2 - pc_nh_x**2) + ((pl_y**2 - pc_nh_y**2)))**0.5
print(new_horizonz_pluto_closest_approach)
