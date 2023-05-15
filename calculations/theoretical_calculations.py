import math
import numpy as np
G_km = 6.67408e-20  # km^3/(kg*s^2)
jupiter_mass = 1.89813 *10**27

# JAT values are values entering hill sphere
# JDT values are calues leaving hill sphere

# comment out either output two values or output three/four values to run code


# OUTPUT TWO VALUES, NO COURSE CORRECTION
    # ship enters hill sphere at time 31978400 (step 159892)
#vx_ship_vel_jat = 0.233787031778129
#vy_ship_vel_jat = -19.63300884533
#vx_jupiter_vel_jat = 11.638640211062812
#vy_jupiter_vel_jat = -4.999904464107486
#jupiter_closest_approach = 555092.724524873 - 69911
    # ship leaves hill sphere at time 37710200 (step 188551)
#vx_jupiter_vel_jdt = 12.08210334761807
#vy_jupiter_vel_jdt = -3.9569593159833683

# OUTPUT THREE AND FOUR VALUES (WITHOUT/WITH ORBIT INSERT ION) ARE
# THE SAME FOR THE JUPITER ENCOUNTER (differ only after the brake)
    # ship enters hill sphere at time 32021600 (step 160108)
vx_ship_vel_jat = 0.187482379864687
vy_ship_vel_jat = -19.4513459230544
vx_jupiter_vel_jat = 11.64249050008641
vy_jupiter_vel_jat = -4.99183045695306
jupiter_closest_approach = 2020278.340628 - 69911
    # ship leaves hill sphere at time 37532800 (step 187664)
vx_jupiter_vel_jdt = 12.08929351033046
vy_jupiter_vel_jdt = -3.937739524925537



# CALCULATION CODE
ship_vel_jat = ((vx_ship_vel_jat)**2+(vy_ship_vel_jat)**2)**0.5 # no eq, just resolving
jupiter_vel_jat = ((vx_jupiter_vel_jat)**2+(vy_jupiter_vel_jat)**2)**0.5 # same
jupiter_vel_jdt = ((vx_jupiter_vel_jdt)**2+(vy_jupiter_vel_jdt)**2)**0.5 # same
print(ship_vel_jat, jupiter_vel_jat, jupiter_vel_jdt)

#converting to juipiter reference frame
hyp_exc_vel_jat_vx = vx_ship_vel_jat - vx_jupiter_vel_jat
hyp_exc_vel_jat_vy = vy_ship_vel_jat - vy_jupiter_vel_jat
print("aaaa", hyp_exc_vel_jat_vx, hyp_exc_vel_jat_vy)
alpha = np.arctan(hyp_exc_vel_jat_vy/hyp_exc_vel_jat_vx)
alpha_d = math.degrees(alpha)
print("alpha", alpha_d)
# hyperbolic excess velocity at jupiter arrival time is ship velocity 
# at JAT minus jupiter velocity at JAT (change of reference frame)
hyp_exc_vel_jat = ship_vel_jat - jupiter_vel_jat
print("hyp", hyp_exc_vel_jat)

# eccentricity of ship orbit around jupiter
e = 1 + (((hyp_exc_vel_jat**2)*jupiter_closest_approach)/(G_km*jupiter_mass))

# deflection angle
theta = 2*np.arcsin(1/e)
theta_d = math.degrees(theta)

beta_d = alpha_d + theta_d
print("beta", beta_d)
# hyperbolic excess velocity at jupiter departure time is determined using theta
hyp_exc_vel_jdt = hyp_exc_vel_jat_vx*np.cos(beta_d) + hyp_exc_vel_jat_vy*np.sin(beta_d)

# moving back to heliocentric reference frame
ship_velocity_post_jat = hyp_exc_vel_jdt + jupiter_vel_jdt

print("The hyperbolic excess velocity at JAT is:", hyp_exc_vel_jat)
print("The eccentricity of the ship orbit during the Jupiter encounter is:", e)
print("The angle of deflection around Jupiter is:", theta_d)
print("The hyerbolic excess velocity at JDT is:", hyp_exc_vel_jdt)
print("The heliocentric velocity of the ship after the Jupiter encounter is:", ship_velocity_post_jat)

