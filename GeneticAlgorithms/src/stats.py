# File: stats.py
# Content: a class of statistics and info about the algorithm and the solutions.


from prettytable import PrettyTable
from matplotlib import pyplot as plt


class Statistics:
    """
    An object from this class collects information about the experiment and
    allows to print it to a table or plot it to a graph.
    """

    def __init__(self):
        """
        Constructor. Initializes the object's knowledge-base.
        """
        self.solution_array = None
        self.solution_matrix = None
        self.correctness = False
        self.fitness = 0
        self.runtime = 0
        self.max_fitness = []
        self.avg_fitness = []
        self.min_fitness = []
        self.fitness_calls = 0
        self.mutate_calls = 0
        self.cross_over_calls = 0
        self.restarts = 0
        self.generations = 0
        self.figure = plt.figure()

    def print_stats(self):
        """
        Print information and statistic using PrettyTable.
        :return: None.
        """
        if self.solution_matrix:
            print()
            stats = PrettyTable(['Item', 'Value(s)'])
            stats.align = 'l'
            board = ''
            for row in self.solution_matrix:
                board += f'{row}\n'
            board = board.replace(',', '').replace('[', '').replace(']', '')
            stats.add_row(['Solution:', board[:-1]])
            stats.add_row(['Correctness:', self.correctness])
            stats.add_row(['Fitness:', self.fitness])
            stats.add_row(['Runtime:', self.runtime])
            stats.add_row(['Generations:', self.generations])
            stats.add_row(['Fitness Calls:', self.fitness_calls])
            stats.add_row(['Mutate Calls:', self.mutate_calls])
            stats.add_row(['X-Over Calls:', self.cross_over_calls])
            stats.add_row(['Restarts:', self.restarts])
            print(stats, end='\n\n')
        else:
            print('Error: Could not print statistics.')

    def save_plot(self):
        """
        This method allows saving a plot of current situation to a variable
        attribute for later show.
        :return: None. But it creates plot figure.
        """
        plt.clf()
        title = 'Fitness per generation\n'
        title += f'Attempt: {self.restarts + 1} | '
        title += f'Fitness calls: {self.fitness_calls} | '
        title += f'Runtime: {self.runtime}'
        plt.title(title)
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        x = list(range(len(self.min_fitness)))
        plt.plot(x, self.min_fitness, label='Minimal fitness')
        plt.plot(x, self.max_fitness, label='Maximal fitness')
        plt.plot(x, self.avg_fitness, label='Average fitness')
        plt.legend()

    def show_plot(self):
        """
        This method shows the saved plot.
        :return: None.
        """
        self.figure.show()

    def reset(self):
        """
        This method re-initializes all object's attributes.
        :return: None.
        """
        self.solution_array = None
        self.solution_matrix = None
        self.correctness = False
        self.fitness = 0
        self.runtime = 0
        self.max_fitness.clear()
        self.avg_fitness.clear()
        self.min_fitness.clear()
        self.fitness_calls = 0
        self.mutate_calls = 0
        self.cross_over_calls = 0
        self.restarts = 0
        self.generations = 0
