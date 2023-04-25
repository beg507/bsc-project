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

course_correction_date = start_time + datetime.timedelta(seconds=35996200*1.5)
#print(course_correction_date)
course_correction_after_JGA = datetime.datetime(2007, 10, 7)
course_correction_after_JGA_sec = int((course_correction_after_JGA - start_time).total_seconds())

course_correction_pluto_hill_sphere = datetime.datetime(2010, 10, 7)
course_correction_pluto_hill_sphere_sec = int((course_correction_pluto_hill_sphere - start_time).total_seconds())
