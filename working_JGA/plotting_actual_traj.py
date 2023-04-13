import matplotlib.pyplot as plt

x_positions = []
y_positions = []
vx_velocities = []
vy_velocities = []
days = []

AU = 149597870.691 #km


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
    vx = float(data[4])
    vy = float(data[5])
    
    days.append(day)
    x_positions.append(x/AU)
    y_positions.append(y/AU)
    vx_velocities.append(vx)
    vy_velocities.append(vy)

# Plot the trajectory
#plt.plot(x_positions, y_positions)
#plt.xlabel('X position')
##plt.ylabel('Y position')
#plt.show()
