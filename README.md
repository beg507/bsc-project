# bsc-project

- Current folder
    - `euler_method.py` current running simulation
    - accompanying data files and other attempts
- Dump folder - for no longer needed files
- Refactoring folder - contains dump cache files currently
- Calculations folder
    - `mars_mission.py` contains calculations for a Hohmann transfer to Mars with values that agree with literature
    - `pluto_grav_mission.py` contains calculations for the bi-elliptical transfer (two Hohmann transfers) needed to get from Earth to Pluto with a gravity assist at Jupiter
        - currently, the values for both this file and the nograv mission are too high (mmission time is way too long) and I'm not sure why as I've used the same physics as in `mars_mission.py`
    - `pluto_nograv_mission.py` contains calculations for the Hohmann transfer directly from Earth to Pluto (no gravity assist)
