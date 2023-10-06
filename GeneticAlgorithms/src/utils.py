# File: utils.py
# Content: class and functions to support genetic algorithms.


from random import randint, shuffle, sample


class Solution:
    """
    This class wraps the representation of a solution for the game. A solution
    is represented by a vector of natural numbers, and each solution has a score
    calculated by a fitness function.
    """
    def __init__(self, game, vector=None):
        """
        Constructor. Initialize a random vector of natural numbers or a setting
        the given vector as the Solution's vector. Then calculate the vector's
        fitness and save it to an attribute.
        :param game: a Futoshiki game object.
        :param vector: a vector of natural numbers repressing a solution.
        """
        if vector:
            self.vector = vector
        else:
            self.vector = [randint(1, game.dim) for _ in range(game.solution_size)]
        self.fitness = fitness(game, self.vector)


def gather_info(population):
    """
    This function calculates the fitness score of the best, worst and average
    solutions in the given population.
    :param population: a list of Solution objects.
    :return: maximum, minimum and average fitness values of the population.
    """
    total = 0
    maximum = 0
    minimum = float('inf')
    for s in population:
        total += s.fitness
        if s.fitness > maximum:
            maximum = s.fitness
        if s.fitness < minimum:
            minimum = s.fitness
    return maximum, minimum, round(total / len(population), 2)


def make_bias_array(population):
    """
    This function creates a bias array that aid to make a biased selection.
    :param population: a list of Solution objects.
    :return: a bias array (as shown in class).
    """
    bias_array = []
    for i, s in zip(range(len(population)), population):
        for j in range(s.fitness):
            bias_array.append(i)
    shuffle(bias_array)  # to reduce programmatic biases.
    return bias_array


def mutate(game, solution):
    """
    This function is the implementation of mutation function. It flips a 3-sides
    coin and choose mutation tactics in a uniform distribution. The tactics are
    swapping two random numbers in the vector that represents the solution,
    swapping two adjacent numbers in it, or to choose a random index i and a
    random number k and assign solution[i]=k.
    :param game: a Futoshiki game object.
    :param solution: a Solution object.
    :return: new mutated solution.
    """
    game.stats.mutate_calls += 1

    # Flip a 3-sided coin...
    coin = randint(1, 3)

    # Tactic 1 -- swapping two random indexes.
    if coin == 1:
        indexes = [i for i in range(len(solution))]
        i, j = sample(indexes, 2)
        array = solution.copy()
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

    # Tactic 2 -- swapping two adjacent indexes (randomly).
    elif coin == 2:
        i = randint(1, len(solution) - 1)
        j = i - 1
        array = solution.copy()
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

    # Tactic 3 -- changing one number in the vector.
    else:
        array = solution.copy()
        array[randint(0, len(solution) - 1)] = randint(1, game.dim)

    # Create a new solution based on the new array and return it.
    return Solution(game, array)


def cross_over(game, solution1, solution2):
    """
    Thi function implements the Cross-Over method as shown in class.
    :param game: a Futoshiki game object.
    :param solution1: a Solution object - parent 1.
    :param solution2: a Solution object - parent 2.
    :return: a cross-overed solution - a newborn.
    """
    game.stats.cross_over_calls += 1
    sep = randint(0, len(solution1) - 1)
    array = solution1[:sep] + solution2[sep:]
    return Solution(game, array)


def fitness(game, solution):
    """
    This function is the fitness evaluation score function. By given a solution,
    it calculates the number of constraints is satisfies in the given game's
    board (matrix).
    :param game: a Futoshiki game object.
    :param solution: a Solution object.
    :return: fitness score - the number of satisfied constraints.
    """
    game.stats.fitness_calls += 1
    game.set(solution)
    score = game.n_constraints
    for x in range(game.dim):
        for y in range(game.dim):
            v = game.matrix[x][y]
            for i in range(game.dim):
                if i != x and game.matrix[i][y] == v:
                    score -= 1  # doesn't satisfies row-constraint.
                    break
            for j in range(game.dim):
                if j != y and game.matrix[x][j] == v:
                    score -= 1  # doesn't satisfies column-constraint.
                    break
    for a, b, c, d in game.relations:
        if game.matrix[a][b] <= game.matrix[c][d]:
            score -= 1  # doesn't satisfies relation-constraint.
    return score
