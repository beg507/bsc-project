import numpy as np

def euler_method(x, y, vx, vy, dt_sun, M, G):
    # calculate acceleration due to gravity (newton)
    r = ((x ** 2) + (y ** 2)) ** 0.5
    ax = (-G * M * x) / (r ** 3)
    ay = (-G * M * y) / (r ** 3)

    # update velocity and position using Euler method
    new_vx = vx + ax * dt_sun
    new_vy = vy + ay * dt_sun
    new_x = x + new_vx * dt_sun
    new_y = y + new_vy * dt_sun

    return new_x, new_y, new_vx, new_vy # new positions and velocities

flags = [] # using to monitor which loops the code goes into

def ship_orbit(x, y, vx, vy, dt_sun, dt_jupiter, m_sun, m_jupiter, G, r_hill_jupiter, x_j, y_j):
    # calculate distance between ship and sun, and ship and jupiter
    r_sun = ((x ** 2) + (y ** 2)) ** 0.5
    r_jupiter = ((x - x_j) ** 2 + (y - y_j) ** 2) ** 0.5
    #print(r_jupiter)

    # if the distance between ship and jupiter is less than the radius of jupiter's hill sphere, then the ship is inside the hill sphere
    # and influenced by jupiter's gravity
    if r_jupiter < r_hill_jupiter:
        #flags.append(1)
        
        # calculate acceleration due to sun and jupiter's gravity
        #ax = -G * (((m_sun) * x / (r_sun ** 3)) + (m_jupiter * (x - x_j) / (r_jupiter ** 3)))
        #ay = -G * (((m_sun) * y / (r_sun ** 3)) + (m_jupiter * (y - y_j) / (r_jupiter ** 3)))
        ax =( -G * (m_jupiter * (x - x_j)) / (r_jupiter ** 3))
        ay = (-G * (m_jupiter * (y - y_j)) / (r_jupiter ** 3))
        new_vx = vx + ax    *dt_jupiter
        new_vy = vy + ay    *dt_jupiter
        new_x = x + new_vx  *dt_jupiter
        new_y = y + new_vy  *dt_jupiter 
    else:
        # calculate acceleration due to the sun's gravity only
        #flags.append(2)
        ax = (-G * m_sun * x )/ (r_sun ** 3)
        ay = (-G * m_sun * y) / (r_sun ** 3)
        new_vx = vx + ax * dt_sun
        new_vy = vy + ay * dt_sun
        new_x = x + new_vx * dt_sun
        new_y = y + new_vy * dt_sun

    # update velocity and position using Euler method
  
    

    return new_x, new_y, new_vx, new_vy


np.savetxt("flags.txt", flags)