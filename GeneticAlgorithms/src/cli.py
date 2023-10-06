# File: cli.py
# Content: class and methods to support user interface.


from sys import exit
from os.path import exists
from prettytable import PrettyTable
from src.game import Futoshiki
from src.solver import genetic_solver


# Program's states.
STOPPED = 0
RUNNING = 1


HELP = 'Help message:\n' \
       '* For each field k you can set the value v by assigning k=v.' \
       ' e.g., g=1000.\n' \
       '* You must provide an input file in to the input field.\n' \
       '* The other fields are set to default values.\n' \
       '* Once the fields are set you can run the program by typing \'r\'.\n' \
       '* Once started, you can stop the run by hitting \'ctrl+0\'.\n' \
       '* To view this help message you can type \'h\'.\n' \
       '* To end the program type \'q\'.'


class Command:
    """
    This class represents a command that has a description functionality.
    Implementation inspired by Command Design Pattern.
    """

    def __init__(self, description, action):
        self.description = description
        self.action = action


class FutoshikiCli:
    """
    This class implements the program's command-line interface.
    """

    def __init__(self):
        """
        Constructor. Initializes system variables, experiment parameters, and
        commands dictionary.
        """

        # System variables.
        self.state = STOPPED
        self.file = ''
        self.to_plot = False
        self.game = None

        # Experiment parameters.
        self.generations = 5000
        self.pop_size = 100
        self.elitism = 0.01
        self.crossover = 0.8
        self.optim = None

        # Command dictionary - define commands and their description and action.
        self.commands = {
            'i': Command(
                description='Set the path to a game input file (REQUIRED).',
                action=self.__parse_game),
            'g': Command(
                description='Set the number of generations to run.',
                action=self.__set_generations),
            'p': Command(
                description='Set the size of the population.',
                action=self.__set_pop_size),
            'e': Command(
                description='Set the percentage of elites in the next '
                            'generation.',
                action=self.__set_elitism),
            'c': Command(
                description='Set the percentage of newborns in the next '
                            'generation.',
                action=self.__set_crossover),
            'o': Command(
                description='Set an optimization method (\"Lamark\", '
                            '\"Darwin\" or \"None\").',
                action=self.__set_optim),
            'f': Command(
                description='Show figure in the end of the experiment (assign '
                            '\"true\" or \"false\").',
                action=self.__show_figure),
            'r': Command(
                description='Run genetic solution (input required)',
                action=None),
            's': Command(
                description='Show current parameters.',
                action=None),
            'h': Command(
                description='Show this help message.',
                action=None),
            'q': Command(
                description='Finish the program.',
                action=None),
        }

        # Define aliases for commands flags.
        self.word2key = {
            'input': 'i',
            'generations': 'g',
            'population': 'p',
            'elitism': 'e',
            'crossover': 'c',
            'mutate_prob': 'mp',
            'mutate_rate': 'mr',
            'optimization': 'o',
            'figure': 'f',
            'run': 'r',
            'settings': 's',
            'help': 'h',
            'quit': 'q'
        }
        self.key2word = {self.word2key[k]: k for k in self.word2key.keys()}

    def __parse_game(self, input_file):
        """
        This command action read a given game input file, parse it and create an
        instance of a Futoshiki game.
        :param input_file: a path to a VALID game input file.
        :return: True if succeeded, False otherwise.
        """

        # Verify file existence.
        if not exists(input_file):
            print('File not found. Please provide an input file.')
            return False

        # Read file.
        try:
            with open(input_file, 'r') as file:
                lines = file.readlines()
        except KeyboardInterrupt:
            exit(-1)
        except Exception:
            print('Could not read file. Please provide a valid input file.')
            return False

        # Parse file.
        try:
            offset = 0  # the offset is the current line the method reads.
            mat_size = int(lines[offset])
            offset += 1
            n_given = int(lines[offset])
            offset += 1
            given_digits = []
            for i in range(n_given):
                given_row = lines[offset].split(' ')
                given_tup = int(given_row[0]), int(given_row[1]), int(given_row[2])
                for x in given_tup:
                    if x < 1 or x > mat_size:
                        raise ValueError
                given_digits.append(given_tup)
                offset += 1
            n_relations = int(lines[offset])
            offset += 1
            relations = []
            for i in range(n_relations):
                relation_row = lines[offset].split(' ')
                relation_tup = (int(relation_row[0]), int(relation_row[1]),
                                int(relation_row[2]), int(relation_row[3]))
                for x in relation_tup:
                    if x < 1 or x > mat_size:
                        raise ValueError
                relations.append(relation_tup)
                offset += 1
            split_path = input_file.split('/')
            if len(split_path) == 1:
                split_path = input_file.split('\\')
            self.file = split_path[-1]
            self.game = Futoshiki(mat_size, given_digits, relations)
            print('Game input file successfully parsed.')
            return True
        except KeyboardInterrupt:
            exit(-1)
        except Exception:
            print('Invalid input. Please provide a valid input file.')
            return False

    def __set_generations(self, x):
        """
        This command action sets the number of generations to x if x is a valid
        input.
        :param x: user input - a string that represents a natural number
        :return: True if succeeded, False otherwise.
        """
        try:
            xi = int(x)
            if xi < 1:
                raise ValueError
            self.generations = xi
            print(f'Generation parameter set to {xi}.')
            return True
        except KeyboardInterrupt:
            exit(-1)
        except Exception:
            print('Number of generations should be a positive integer.')
            return False

    def __set_pop_size(self, x):
        """
        This method sets the size of the population to x if it is a valid input.
        :param x: user input - a string that represents a natural number
        :return: True if succeeded, False otherwise.
        """
        try:
            xi = int(x)
            if xi < 1:
                raise ValueError
            self.pop_size = xi
            print(f'Population size parameter set to {xi}')
            return True
        except KeyboardInterrupt:
            exit(-1)
        except Exception:
            print('Population size should be a positive integer')
            return False

    def __set_elitism(self, x):
        """
        This command action sets the elitism parameter to x if x is valid.
        :param x: user input - a string that represents a float between 0 and 1.
        :return: True if succeeded, False otherwise.
        """
        try:
            xf = float(x)
            if xf < 0 or xf > 1:
                raise ValueError
            self.elitism = xf
            print(f'Elitism parameter set to {xf}.')
            return True
        except KeyboardInterrupt:
            exit(-1)
        except Exception:
            print('Elitism should be a float between 0 and 1.')
            return False

    def __set_crossover(self, x):
        """
        This command action sets the cross-over parameter to x if x is valid.
        :param x: user input - a string that represents a float between 0 and 1.
        :return: True if succeeded, False otherwise.
        """
        try:
            xf = float(x)
            if xf < 0 or xf > 1:
                raise ValueError
            self.crossover = xf
            print(f'Cross-over parameter to {xf}.')
            return True
        except KeyboardInterrupt:
            exit(-1)
        except Exception:
            print('Cross-over should be a float between 0 and 1.')
            return False

    def __set_optim(self, x):
        """
        This method sets the optimization to x if it is a valid input.
        :param x: user input - a string that represents an optimization method.
        :return: True if succeeded, False otherwise.
        """
        xl = x.lower()
        if xl == 'lamark' or xl == 'darwin':
            self.optim = xl
            print(f'{x} optimization set.')
            return True
        elif xl == 'none':
            self.optim = None
            print(f'No optimization selected.')
            return True
        else:
            print('Optimization should be \"Lamark\", \"Darwin\" or \"None\".')
            return False

    def __show_figure(self, x):
        """
        This command action makes the program show/hide plot in the end of the
        run according to x.
        :param x: user input - a string that represents True or False.
        :return: True if succeeded, False otherwise.
        """
        xl = x.lower()
        if xl == 'true' or xl == 't':
            self.to_plot = True
            print(f'Plot set to {self.to_plot}')
            return True
        elif xl == 'false' or xl == 'f':
            self.to_plot = False
            print(f'Plot set to {self.to_plot}')
            return True
        else:
            print('Plot assignment should be \"true\" or \"false\".')
            return False

    def __run(self):
        """
        This command action make the experiment running.
        :return: True if succeeded, False otherwise.
        """
        if self.game:

            # Run genetic algorithm on the given parameters.
            stats = genetic_solver(game=self.game,
                                   generations=self.generations,
                                   pop_size=self.pop_size,
                                   elitism=self.elitism,
                                   crossover=self.crossover,
                                   optim=self.optim,
                                   to_plot=self.to_plot)

            # If not stopped by the user, print info and maybe show plot.
            if stats:
                print('\nCalculations completed!')
                stats.correctness = self.game.validate(stats.solution)
                stats.solution_matrix = self.game.matrix
                stats.print_stats()
                if self.to_plot:
                    stats.show_plot()
                return True
            print('\nStopped.')
            return False
        else:
            print('Error! Please provide an input file and then try again.')
            return False

    def __show_params(self):
        """
        This command action display current applied settings and parameters.
        :return: True.
        """
        print(f'Input file:      {self.file}')
        print(f'Generations:     {self.generations}')
        print(f'Population size: {self.pop_size}')
        print(f'Elitism:         {self.elitism}')
        print(f'Cross-over:      {self.crossover}')
        print(f'Optimization:    {self.optim}')
        print(f'Plot:            {self.to_plot}')
        print()
        return True

    def __show_help(self):
        """
        This command action display help message.
        :return: True.
        """
        table = PrettyTable(['Field', 'Input'])
        table.add_row(['-----', '-----'])
        table.align = 'l'
        table.border = False
        for k in self.commands.keys():
            if k == 'r':
                table.add_row(['', ''])
                table.add_row(['Operator', 'Operation'])
                table.add_row(['--------', '---------'])
            table.add_row([f'{k}, {self.key2word[k]}', self.commands[k].description])
        print(HELP, end='\n\n')
        print(table, end='\n\n')
        return True

    def __quit(self):
        """
        This command action terminates the program.
        :return: True.
        """
        self.state = STOPPED
        print('\nGood Bye! ☻')
        return True

    def __process_assignments(self, args):
        """
        This method handle settings/parameters changes by the user.
        :param args: a string represents keys and values separated by '='.
        :return: True if succeeded, False otherwise.
        """
        execute = []
        for arg in args:

            # An argument should be a key=value pair, such as input=f.txt.
            kv = arg.split('=')
            if len(kv) != 2 or len(kv[0]) == 0 or len(kv[1]) == 0:
                print('Invalid input. Use key=value pairs or and operator.')
                return False

            # An argument should represent a possible action.
            k, v = kv
            if k not in self.commands.keys() and k not in self.word2key.keys():
                print('Invalid input. Type \"help\" for help message.')
                return False

            # Handle aliasing. e.g., e=0.8 instead of elitism=0.8.
            if k in self.word2key.keys():
                k = self.word2key[k]

            # A valid argument turns into a command.
            # Add valid commands to an execution list.
            execute.append((k, v))

        # Execute commands from the execution lists.
        for k, v in execute:
            if not self.commands[k].action(v):
                return False

        # Report success.
        return True

    def mainloop(self):
        """
        This method is the mainloop of the command-line interface.
        :return: None.
        """
        print('\nFUTOSHIKI SOLVER CLI APP')
        print('Solve Futoshiki games using a genetic algorithm')
        print()
        self.state = RUNNING
        self.__show_help()
        while self.state == RUNNING:
            args = input('>>> ').lower()
            if args == 'r' or args == 'run':
                self.__run()
            elif args.startswith('r ') or args.startswith('run '):
                args = args.split()[1:]
                if self.__process_assignments(args):
                    self.__run()
            elif args == 's' or args == 'settings':
                self.__show_params()
            elif args == 'h' or args == 'help' or args == '?':
                self.__show_help()
            elif args == 'q' or args == 'quit':
                self.__quit()
            else:
                args = args.split()
                self.__process_assignments(args)
