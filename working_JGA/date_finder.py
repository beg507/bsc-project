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
#print(enter_pluto_hill_sphere_date)

course_correction_2_date = start_time + datetime.timedelta(seconds=272985000)
#print(course_correction_2_date)
course_correction_2 = datetime.datetime(2013, 6, 11)
course_correction_2_sec = int((course_correction_2 - start_time).total_seconds())

course_correction_3_date = start_time + datetime.timedelta(seconds=268038199)
#print(course_correction_3_date)
course_correction_3 = datetime.datetime(2014, 7, 20)
course_correction_3_sec = int((course_correction_3 - start_time).total_seconds())

