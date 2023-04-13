import math

def angle_between_points(point1, point2, reference_point):
    dx1 = point1[0] - reference_point[0]
    dy1 = point1[1] - reference_point[1]
    dx2 = point2[0] - reference_point[0]
    dy2 = point2[1] - reference_point[1]
    angle1 = math.atan2(dy1, dx1)
    angle2 = math.atan2(dy2, dx2)
    angle = angle2 - angle1
    if angle > math.pi:
        angle -= 2 * math.pi
    elif angle < -math.pi:
        angle += 2 * math.pi
    return angle

point1 = (-313046084.30704147, -678870375.791085)
point2 = (-274408471.6827583, -805260831.0182734)
reference_point = (-275714122.82955503, -748480519.2781678)

angle = angle_between_points(point1, point2, reference_point)
print(f"The angle between the two points is {angle} radians.") #2.672318756100329
print(f"The angle between the two points is {angle*(180/math.pi)} degrees.") #153.11258623819887
print(f"The turning angle is therefore {(angle*(180/math.pi))/2} degrees.") #76.55629311909944