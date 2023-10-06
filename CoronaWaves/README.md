# CoronaWaves

This is an application that describes the phenomenon of corona virus waves among the population. The app has a grid that displays the updated results.

### Description

Corona Virus waves are interesting phenomena in which the percentage of those infected in the population increases significantly for a while and then decreases. This rise and fall is repeated several times over time. The phenomenon is known in epidemics in general and in Corona Virus in particular. In this project we created a simulator that depicts this.
![CoronaWaves](https://user-images.githubusercontent.com/60240620/164909293-16bf5bcb-583d-4b0f-985f-ddccd920efd5.png)

### Installation

You can download the code, in the folder there is an exe file for fast execution by double-clicking on: Corona Waves.exe

### Usage

The application has a configure bar for the purpose of studying the behavior of the virus among the population.
The user can add the values of the number of people in the population, choose how many of them will be infected with the virus at the beginning of the run, how long it takes to create and recover from the disease and somemore features.
While running, the user receives important information about the system, such as the total percentage of infections, the number of infections, and the likelihood of being infected.
At the end of the run, when the user clicks on the 'Stop' button, a patient behavior graph will appear among the population as a function of duration.
![result1](https://user-images.githubusercontent.com/60240620/164909364-d92edc72-a081-4e59-ab6a-ea25422fdd7f.png)


### Dictionary

* app.py - Document containing the app settings, windows, grid, entries and buttons.
* automata.py - Document that containing the engine behind the simulator. Calculates the behavior of the creatures inside the grid, their movement in each generation and the attitude towards the creatures around them. Each generation presents the results on the grid.
* state.py - Document that represents automata's states
* style.py - Document that represents a color palette for easy access to pre-defined colors.
* main.py - main function.

### Credits
In this project we examined the pattern of the corona virus spreading among populations.
The code was written by Itamar Laredo and Shlomi Ben Shushan. 
The project was written as part of a project in Computitional Biology course, Bar-Ilan University.

