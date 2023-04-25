import math

pluto_closest_approach = 4129.00254638237
hyp_exc_vel_at_pluto_enter_hill_sphere = 18.17051930186136
# v= sqrt(GM/r_orbit)
pluto_radius = 1188.3
pluto_mass = 1.307 *10**22
G_km = 6.67408e-20  # km^3/(kg*s^2)

target_velocity_at_closest_approach = math.sqrt((G_km*pluto_mass)/pluto_closest_approach)
print(target_velocity_at_closest_approach)
print(target_velocity_at_closest_approach/18.17051930186136)

# eq before 12-10
v_t_ins = math.sqrt(((2*G_km*pluto_mass)/pluto_closest_approach)+18.134303363828355**2)
print(v_t_ins)

delta_v_t_ins = math.sqrt(((2*G_km*pluto_mass)/pluto_closest_approach)+18.134303363828355**2) - math.sqrt((G_km*pluto_mass)/pluto_closest_approach)
print(delta_v_t_ins)

print(v_t_ins-delta_v_t_ins)

v_e = 210
m_i = 	478 # new horizons launch mass
m_f = m_i / (math.exp(delta_v_t_ins/v_e))
#print(m_f)

v = math.sqrt((G_km*pluto_mass)/2070.3015574265105)
print(v)

d_v = 18.15273597884579 - v
print(d_v)