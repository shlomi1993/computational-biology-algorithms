# Computational-Biology-Algorithms
This repository documents implementations of algorithms I learned in a computational biology course, and it is divided into three parts. One part is a program that uses a cellular automata to identify the conditions for the spread of an epidemic, The second is the implementation of a self-organizing map, and the third deals with the implementation of genetic algorithms.

## Part 1: CoronaWaves
This is an application that describes the phenomenon of coronavirus waves among the population. The app has a grid that displays the updated results.

### Description
Corona Virus waves are interesting phenomena in which the percentage of those infected in the population increases significantly for a while and then decreases. This rise and fall is repeated several times over time. The phenomenon is known in epidemics in general and in coronavirus in particular. In this project, we created a simulator that depicts this.
![CoronaWaves](https://user-images.githubusercontent.com/60240620/164909293-16bf5bcb-583d-4b0f-985f-ddccd920efd5.png)

### Installation
You can download the code, in the folder, there is an exe file for fast execution by double-clicking on "Corona Waves.exe"

### Usage
The application has a configure bar to study the behavior of the virus among the population. The user can add the values of the number of people in the population, choose how many of them will be infected with the virus at the beginning of the run, how long it takes to create and recover from the disease, and some more features.  
While running, the user receives important information about the system, such as the total percentage of infections, the number of infections, and the likelihood of being infected.
At the end of the run, when the user clicks on the 'Stop' button, a patient behavior graph will appear among the population as a function of duration.
![result1](https://user-images.githubusercontent.com/60240620/164909364-d92edc72-a081-4e59-ab6a-ea25422fdd7f.png)

### Files
* app.py - Document containing the app settings, windows, grid, entries, and buttons.
* automata.py - Document that contains the engine behind the simulator. Calculates the behavior of the creatures inside the grid, their movement in each generation, and their attitude towards the animals around them. Each generation presents the results on the grid.
* state.py - Document that represents automata's states
* style.py - Document that represents a color palette for easy access to pre-defined colors.
* main.py - main function.


## Part 2: Self-Organizing-Map

### Description
In this part, I'll show my implementation of a Self-Oprganized-Map algorithm and I will explain how to use the wrapping app.

### Requirements
There are no unique requirements to run the executable file SOM.exe.  
But if there is a need to run the source code of the program, then the following requirements must be met first:
1. Please make sure that Python 3 is installed on your machine. The program was written using Python version 3.10 but was also tested on Python 3.8.
2. Use pip, or any other Python package manager, to install the packages: 'ntpath', 'tkinter', 'prettytable', 'matplotlib', and 'numpy'.

### Instructions

### Starting the program
If you are using the executable, just double-click on it (or execute it via the terminal) and the program will start.
If you want to run the source code, make sure the requirements above are met. Then, navigate to the programs's main directory (where the main.py file is located), and run the command 'python main.py'.

#### Using the program
After the program starts, the following window will appear:  

![image](https://user-images.githubusercontent.com/72878018/173429746-fe0a90e6-3973-40e5-a85d-eb28ddd2aa29.png)  
  
In this window, you can:  
1. Load an input CSV file (required).
2. Change the number of epochs to run (default is 10).
3.  Choose the error measurement method (default is Quantization Error).
4.   Determine whether the program will show a figure (default is True).

Important Notes:
1. Make sure the input file is valid, i.e., in the attached file "Elec_24.csv".
2. Selecting a high number of epochs may make the program look frozen. Patience, the computation is being done in the background and the output will be displayed when it is finished.

#### Output
The program output is obtained in three forms:
1. A hexagonal diagram will be displayed on the main canvas on the right.
2. A mapping table between the municipality and the representative cell (neuron) will be displayed in the console on the left.
3. A figure describing the errors will be displayed in a new window (if True is set in the settings).

### Screenshots
Below is an example of the program output:  
![image](https://user-images.githubusercontent.com/72878018/173408379-70e5bfd5-f04b-4c99-9ad0-e3cd9090d07d.png)  


## Part 3: GeneticAlgorithms

### Description
In this part, I'll show my implementation of a Genetic Algorithm that solves boards of the Futoshiki game. Then, I will instruct the usage of a CLI-App I have implemented to test this algorithm.

### Requirements
There are no unique requirements to run the executable file (.exe).  
But if there is a need to run the source code of the program, then the following requirements must be met first:
1. Please make sure that Python 3 is installed on your machine. The program was written using Python version 3.10 but was also tested on Python 3.8.
2. Use install the packages 'prettytable', 'matplotlib', and 'keyboard', using pip or any other python package manager.

### Instructions

### Starting the program
If you are using the executable, just double-click on it (or execute it via the terminal) and the program will start.
If you want to run the source code, make sure the requirements above are met, and then navigate to the programs' main directory (where the app.py file is located), and run the command 'python app.py'.

#### Using the program
After the program starts a command-line interface console will appear on the screen and through this console, you can operate the genetic algorithm Futoshiki game solver.  
The commands you can insert into the console are divided into two types:  
  
**Field-assignment** - Insert pairs of keys and values to set the value of a key parameter using the '=' character. For example, to set the experiment number of generations to 1000, you can insert the command 'generations=1000', or shortly 'g=1000'.  
All fields except the input file field are filled with the following default values as follows:  
- Generations: 5000
- Population size: 100
- Elitism: 0.01
- Cross-over: 0.8
- Optimization: None
- Plot: False
  
**Operators** - Insert a single-word operator to make the program do something, such as show the current program settings by inserting the command 'show', or shortly 's'.  
  
There is a special operator 'run' or 'r' that not only runs the algorithm in an attempt to find a solution but also can be combined with field assignments. For example, the command:  
- 'run input=easy5.txt o=lamark g=1234'  
  
will load the file easy5.txt, use Lamark optimization, set the number of generations to 1234, and then run the solver.

Here is information about the available field-assignment and operators:  

**Field-assignments**  
- i or input - Set the path to a game input file (REQUIRED).
- g or generations - Set the number of generations to run.
- p or population - Set the size of the population.
- e or elitism - Set the percentage of elites in the next generation.
- c or crossover - Set the percentage of newborns in the next generation.
- o or optimization - Set an optimization method ("Lamark", "Darwin" or "None").
- f or figure - Show the figure at the end of the experiment (assign "true" or "false").
  
**Operators**  
- r or run - Run genetic solution (input required)
- s or settings - Show current parameters.
- h or help - Show this help message.
- q or quit - Finish the program.
  
To show an information table in the app, simply type 'help', 'h', or '?'.
  

### Screenshots
  
Once started, the CLI will show the following:  
![image](https://user-images.githubusercontent.com/72878018/170319856-3e4f6b3b-143a-4b55-a73e-8a3949b74dbc.png)
  
Then, running the program looks as follows:  
![image](https://user-images.githubusercontent.com/72878018/170320383-16132d06-f12a-430a-8111-53d8cbc0d60b.png)
    
**Note:** The difference between Best fit and Optimal fit is that Best fit is the fitness of the best solution in the current attempt, meanwhile the Optimal fit is the fitness of the best solution found in the whole experiment so far.
