# appending velocites from files to arrays for plotting

with open('ship_velocity_array_course_correction.txt', 'r') as f:
    course_correction_velocities = []
    for line in f:
        course_correction_velocities.append(float(line.strip()))

with open('ship_velocity_array_no_course_correction.txt', 'r') as f:
    no_course_correction_velocities = []
    for line in f:
        no_course_correction_velocities.append(float(line.strip()))