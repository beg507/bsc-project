import numpy as np

def euler_method(x, y, vx, vy, dt, m2, G):
    # calculate acceleration due to gravity (newton)
    r = ((x ** 2) + (y ** 2)) ** 0.5
    ax = -G * m2 * x / (r ** 3)
    ay = -G * m2 * y / (r ** 3)

    # update velocity and position using Euler method
    new_vx = vx + ax * dt
    new_vy = vy + ay * dt
    new_x = x + new_vx * dt
    new_y = y + new_vy * dt

    return new_x, new_y, new_vx, new_vy # new positions and velocities

flags = [] # using to monitor which loops the code goes into

def ship_orbit(x, y, vx, vy, dt, m_sun, m_jupiter, G, r_hill_jupiter, x_j, y_j):
    # calculate distance between ship and sun, and ship and jupiter
    r_sun = ((x ** 2) + (y ** 2)) ** 0.5
    r_jupiter = ((x - x_j) ** 2 + (y - y_j) ** 2) ** 0.5
    #print(r_jupiter)

    # if the distance between ship and jupiter is less than the radius of jupiter's hill sphere, then the ship is inside the hill sphere
    # and influenced by jupiter's gravity
    if r_jupiter < r_hill_jupiter:
        flags.append(1)
        
        # calculate acceleration due to sun and jupiter's gravity
        ax = -G * (((m_sun) * x / (r_sun ** 3)) + (m_jupiter * (x - x_j) / (r_jupiter ** 3)))
        ay = -G * (((m_sun) * y / (r_sun ** 3)) + (m_jupiter * (y - y_j) / (r_jupiter ** 3)))
        #ax = -G * (m_jupiter * (x - x_j) / (r_jupiter ** 3))
        #ay = -G * (m_jupiter * (y - y_j) / (r_jupiter ** 3))
    else:
        # calculate acceleration due to the sun's gravity only
        flags.append(2)
        ax = -G * m_sun * x / (r_sun ** 3)
        ay = -G * m_sun * y / (r_sun ** 3)

    # update velocity and position using Euler method
    new_vx = vx + ax * dt
    new_vy = vy + ay * dt
    new_x = x + new_vx * dt
    new_y = y + new_vy * dt

    return new_x, new_y, new_vx, new_vy


np.savetxt("flags.txt", flags)