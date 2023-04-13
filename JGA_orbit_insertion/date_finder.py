import datetime

# define the starting date and time
start_time = datetime.datetime(2006, 1, 20, 19, 0, 0)

# calculate the timedelta from the starting time to the target time
jupiter_closest_approach_date = start_time + datetime.timedelta(seconds=33430800)
pluto_closest_approach_date = start_time + datetime.timedelta(seconds=238605000)
enter_jupiter_hill_sphere_date = start_time + datetime.timedelta(seconds=30795000)
exit_jupiter_hill_sphere_date = start_time + datetime.timedelta(seconds=35996200)
