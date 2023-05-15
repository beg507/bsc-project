import numpy as np

def euler_method(x, y, vx, vy, dt, M, G):
    r = ((x ** 2) + (y ** 2)) ** 0.5
    ax = (-G * M * x) / (r ** 3)
    ay = (-G * M * y) / (r ** 3)

    new_vx = vx + ax * dt
    new_vy = vy + ay * dt
    new_x = x + new_vx * dt
    new_y = y + new_vy * dt

    return new_x, new_y, new_vx, new_vy 

def ship_orbit(x, y, vx, vy, dt, m_sun, m_jupiter, m_pluto, G, 
               r_hill_jupiter, r_hill_pluto, x_j, y_j, x_p, y_p):
    r_sun = ((x ** 2) + (y ** 2)) ** 0.5
    r_jupiter = ((x - x_j) ** 2 + (y - y_j) ** 2) ** 0.5
    r_pluto = ((x - x_p) ** 2 + (y - y_p) ** 2) ** 0.5

    if r_jupiter < r_hill_jupiter:
        # orbit jupiter
        ax =( -G * (m_jupiter * (x - x_j)) / (r_jupiter ** 3))
        ay = (-G * (m_jupiter * (y - y_j)) / (r_jupiter ** 3))
        new_vx = vx + ax    *dt
        new_vy = vy + ay    *dt
        new_x = x + new_vx  *dt
        new_y = y + new_vy  *dt

    elif r_pluto < r_hill_pluto:
        # orbit pluto
        ax =( -G * (m_pluto * (x - x_p)) / (r_pluto ** 3))
        ay = (-G * (m_pluto * (y - y_p)) / (r_pluto ** 3))
        new_vx = vx + ax    *dt
        new_vy = vy + ay    *dt
        new_x = x + new_vx  *dt
        new_y = y + new_vy  *dt
    else:
        # orbit sun
        ax = (-G * m_sun * x )/ (r_sun ** 3)
        ay = (-G * m_sun * y) / (r_sun ** 3)
        new_vx = vx + ax * dt
        new_vy = vy + ay * dt
        new_x = x + new_vx * dt
        new_y = y + new_vy * dt

    return new_x, new_y, new_vx, new_vy, dt




