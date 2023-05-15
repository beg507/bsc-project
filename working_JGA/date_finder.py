import datetime

# define the starting date and time
start_time = datetime.datetime(2006, 1, 20, 19, 0, 0)

# calculate the timedelta from the starting time to the target time
jupiter_closest_approach_date = start_time + datetime.timedelta(seconds=33430800)
pluto_closest_approach_date = start_time + datetime.timedelta(seconds=238605000)
enter_jupiter_hill_sphere_date = start_time + datetime.timedelta(seconds=30795000)
exit_jupiter_hill_sphere_date = start_time + datetime.timedelta(seconds=35996200)

jan_28_2006_course_correction = datetime.datetime(2006, 1, 28)
jan_30_2006_course_correction = datetime.datetime(2006, 1, 30)
mar_9_2006_course_correction = datetime.datetime(2006, 3, 9)
sep_25_2007_course_correction = datetime.datetime(2007, 9, 25)

jan_28_2006_course_correction_sec = int((jan_28_2006_course_correction - start_time).total_seconds()) + (24*60*60)
jan_30_2006_course_correction_sec = int((jan_30_2006_course_correction - start_time).total_seconds()) + (24*60*60)
mar_9_2006_course_correction_sec = int((mar_9_2006_course_correction - start_time).total_seconds()) + (24*60*60)
sep_25_2007_course_correction_sec = int((sep_25_2007_course_correction - start_time).total_seconds()) + (24*60*60)

course_correction = datetime.datetime(2006, 11, 1)
course_correction_sec = int((course_correction - start_time).total_seconds())

enter_pluto_hill_sphere_date = start_time + datetime.timedelta(seconds=272970900)

course_correction_2_date = start_time + datetime.timedelta(seconds=272985000)
#print(course_correction_2_date)
course_correction_2 = datetime.datetime(2013, 6, 11)
#(2013, 6, 10) gives approach at pluto 2000m
#(2013, 6, 11) gives approach at pluto  4129.00254638237
course_correction_2_sec = int((course_correction_2 - start_time).total_seconds())

course_correction_3_date = start_time + datetime.timedelta(seconds=268038199)
#print(course_correction_3_date)
course_correction_3 = datetime.datetime(2014, 7, 20)
course_correction_3_sec = int((course_correction_3 - start_time).total_seconds())

# FINDING FINAL DATES USING OUTPUT FILES

o1_entered_jhs_time = 31978400
o1_jup_closest_approach_time = 34844200
o1_exited_jhs_time = 37710200
o1_pluto_closest_approach_time = 346100400
print("Output 1: Enter Jupiter hill sphere at time", o1_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o1_entered_jhs_time))
print("Output 1: Jupiter closest approach at time", o1_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o1_jup_closest_approach_time))
print("Output 1: Exit Jupiter hill sphere at time", o1_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o1_exited_jhs_time))
print("Output 1: Pluto closest approach at time", o1_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o1_pluto_closest_approach_time))

o2_entered_jhs_time = 31978400
o2_jup_closest_approach_time = 34745000
o2_exited_jhs_time = 37434400
o2_pluto_closest_approach_time = 208183200
print("Output 2: Enter Jupiter hill sphere at time", o2_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o2_entered_jhs_time))
print("Output 2: Jupiter closest approach at time", o2_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o2_jup_closest_approach_time))
print("Output 2: Exit Jupiter hill sphere at time", o2_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o2_exited_jhs_time))
print("Output 2: Pluto closest approach at time", o2_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o2_pluto_closest_approach_time))


o3_entered_jhs_time = 32021600
o3_jup_closest_approach_time = 34819200
o3_exited_jhs_time = 37532800
o3_entered_phs_time = 268047800
o3_pluto_closest_approach_time = 268491000
o3_exited_phs_time = 268934000
print("Output 3: Enter Jupiter hill sphere at time", o3_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o3_entered_jhs_time))
print("Output 3: Jupiter closest approach at time", o3_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o3_jup_closest_approach_time))
print("Output 3: Exit Jupiter hill sphere at time", o3_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o3_exited_jhs_time))
print("Output 3: Enter Pluto hill sphere at time", o3_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o3_entered_phs_time))
print("Output 3: Pluto closest approach at time", o3_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o3_pluto_closest_approach_time))
print("Output 3: Exit Pluto hill sphere at time", o3_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o3_exited_phs_time))

o4_entered_jhs_time = 32021600
o4_jup_closest_approach_time = 34819200
o4_exited_jhs_time = 37532800
o4_entered_phs_time = 268491800
o4_pluto_closest_approach_time = 268491800
o4_exited_phs_time = 269990600
print("Output 4: Enter Jupiter hill sphere at time", o4_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o4_entered_jhs_time))
print("Output 4: Jupiter closest approach at time", o4_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o4_jup_closest_approach_time))
print("Output 4: Exit Jupiter hill sphere at time", o4_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o4_exited_jhs_time))
print("Output 4: Enter Pluto hill sphere at time", o4_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o4_entered_phs_time))
print("Output 4: Pluto closest approach at time", o4_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o4_pluto_closest_approach_time))
print("Output 4: Exit Pluto hill sphere at time", o4_entered_jhs_time, "seconds which corresponds to date", start_time + datetime.timedelta(seconds=o4_exited_phs_time))
