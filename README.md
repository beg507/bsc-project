# bsc-project

- The wokring simulation files are found in the **"working_JGA"** folder and are the files that generated the results shown in the BSc Project Report
    - The folder **"formatted for report"** contains these files as shown in the appendix of the BSc Report (where necessary) and removes code that was used for plotting or investigation of the main code i.e. these files are a clean version of those in **"working_JGA"**, formatted for insertion into the A4 report PDF

- The following folders are NOT needed for the simulation to run
    - **"calculations"** folder: contains files used to calculate the Hohmann transfer times from Earth to Mars and Earth to Pluto, as well as orbit insertion invesitgations and the theoretical calculations needed for the final trajectory's JGA
    - **"dump"** folder: contains redundant files from throughout the project life cycle with old methods and their iterations. These files were kept in case it became necessary to revert to a previously attempted method

# Main Project Folder - working_JGA
**The main file to run the simulation is `euler_method_main.py`**. This file relies on imports from various Python libraries as well as the files:
- `ephemeris.py` which contains the initial positions and velocities of the bodies in the simulation
- `body_data.py` which contains the key data related to each of the bodies in the solar system
- `functions.py` which contains the Euler-Methods functions required to iterate over the solution
- `array_file.py` which contains the initialised arrays for the simulated bodies as well as the time array and step size 
- `date_finder.py` which is used to specify the time to implement the course corrections/brake in `euler_method_main.py`
in addition to some other files that have been generated solely for plotting purposes (these do not affect the running of the code and can be commented out accordingly).
Comments are provided in `euler_method_main.py` explaining which code requires commenting out in order to run the different simulations as shown in the subsections of the Results of the BSc Project Report