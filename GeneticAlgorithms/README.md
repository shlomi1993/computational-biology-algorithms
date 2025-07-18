# GeneticAlgorithms
Computational Biology - Assignment 2
Solved by Shlomi Ben-Shushan.

## Description
In this ReadMe file, I will describe the programmatic implementation of a Genetic Algorithm that solves boards of Futoshiki game. Then, I will instruct the usage of a CLI-App I have implemented to test this algorithm.

## Requirements
There are no unique requirements to run the executable file (.exe).  
But if there is a need to run the source code of the program, then the following requirements must be met first:
1. Please make sure that Python 3 is installed in your machine. The program was written using Python version 3.10 but was also tested on Python 3.8.
2. Use install the packages 'prettytable', 'matplotlib', and 'keyboard', using pip or any other python package manager.

## Instructions
### Starting the program
If you are using the executable, just double click on it (or execute it via terminal) and the program will start.
If you want to run the source code, make sure the requirements above met, and then navigate to the programs's main directory (where app.py file is located), and run the command 'python app.py'.

### Using the program
After the program starts a command-line interface console will appear on the screen and through this console you can operate the genetic algorithm Futoshiki game solver.  
The commands you can insert to the console are divided to two types:  
  
**Field-assignment** - Insert pairs of key and values to set the value of a key parameter using '=' character. For example, to set the experiment number of generations to 1000, you can insert the command 'generations=1000', or shortly 'g=1000'.  
All fields except the input file field are filled with the following default values as follows:  
- Generations: 5000
- Population size: 100
- Elitism: 0.01
- Cross-over: 0.8
- Optimization: None
- Plot: False
  
**Operators** - Insert single-word operator to make the program do something, such as show the corrent program settings by inserting the command 'show', or shortly 's'.  
  
There is a special operator 'run' or 'r' that not only run the algorithm in an attempt to find a solution, but also can be combined with field-assignments. For example, the command:  
- 'run input=easy5.txt o=lamark g=1234'  
  
will load the file easy5.txt, use lamark optimization, set the number of generations to 1234, and then run the solver.

Here is information about the avilable field-assignment and operators:  

**Field-assignments**  
- i or input - Set the path to a game input file (REQUIRED).
- g or generations - Set the number of generations to run.
- p or population - Set the size of the population.
- e or elitism - Set the percentage of elites in the next generation.
- c or crossover - Set the percentage of newborns in the next generation.
- o or optimization - Set an optimization method ("Lamark", "Darwin" or "None").
- f or figure - Show figure in the end of the experiment (assign "true" or "false").
  
**Operators**  
- r or run - Run genetic solution (input required)
- s or settings - Show current parameters.
- h or help - Show this help message.
- q or quit - Finish the program.
  
To show an information table in the app, simply type 'help', 'h' or '?'.
  

## Screenshots
  
Once started, the CLI will show the follows:  
![image](https://user-images.githubusercontent.com/72878018/170319856-3e4f6b3b-143a-4b55-a73e-8a3949b74dbc.png)
  
Then, running the program looks as follows:  
![image](https://user-images.githubusercontent.com/72878018/170320383-16132d06-f12a-430a-8111-53d8cbc0d60b.png)
    
**Note:** The difference is between Best fit and Optimal fit is that Best fit is the fitness of the best solution in the current attempt, meanwhile the Optimal fit is the fitness of the best solution found in the whole experiment so far.
