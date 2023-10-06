# File: optim.py
# Content: an implementation of the optimization method.


from random import choice, randint
from src.utils import Solution


def create_truth_matrix(game, solution):
    """
    This function creates a "truth" matrix which holds in the i,j-cell the
    number of unsatisfied constraints by the given solution in the given game.
    :param game: a Futoshiki game object.
    :param solution: a Solution object.
    :return: the described matrix.
    """

    # First, set the solution.
    game.set(solution.vector)
    truth_matrix = []

    # Check constraints' satisfaction - for each constraint.
    for x in range(game.dim):
        row = []
        for y in range(game.dim):
            v = game.matrix[x][y]
            not_satisfied = 0

            # Check row-constraint.
            for i in range(game.dim):
                if i != x and game.matrix[i][y] == v:
                    not_satisfied += 1
                    break

            # Check column-constraint.
            for j in range(game.dim):
                if j != y and game.matrix[x][j] == v:
                    not_satisfied += 1
                    break

            # Check relation-constraint.
            for a, b, c, d in game.relations:
                if (x, y) == (a, b) and game.matrix[x][y] <= game.matrix[c][d]:
                    not_satisfied += 1
                    break

            row.append(not_satisfied)
        truth_matrix.append(row)
    return truth_matrix


def find_unsatisfied_cells(game, solution):
    """
    This function finds all the cells in the game matrix that are not satisfied
    by the given solution, using a "truth" matrix.
    :param game: a Futoshiki game object.
    :param solution: a Solution object.
    :return: a list of tuples (i, j, u) where i,j are the cell position and u is
             the number of unsatisfied constraints by the value in this cell.
    """
    truth_matrix = create_truth_matrix(game, solution)
    unsatisfied_cells = []

    # Fill a list with unsatisfied cells by the truth_matrix.
    for x in range(game.dim):
        for y in range(game.dim):
            if truth_matrix[x][y] > 0:
                unsatisfied_cells.append((x, y, truth_matrix[x][y]))

    # Filter out game's given numbers.
    for i, j, u in unsatisfied_cells:
        if (i, j) in game.given.keys():
            unsatisfied_cells.remove((i, j, u))

    return unsatisfied_cells


def find_optimizations(game, cells):
    """
    This function finds a list of optimization options sorted by urgency.
    :param game: a Futoshiki game object.
    :param cells: a list of tuples (i,j,u) where the i,j-cell hit u constraints.
    :return: a list of tuples (x, y, [O], t) where the x,y-cell can be optimized
             by setting a value in it from the list [O] and currently this cell
             is not satisfying u constraints.
    """
    optimizations = []
    count = 0

    # For 'limit' unsatisfied cells in urgency order...
    for x, y, u in cells:
        v = game.matrix[x][y]

        # Initialize a list of allowed values.
        allowed = [i + 1 for i in range(game.dim)]

        # Remove from 'allowed' the values in the cell's row.
        for i in range(game.dim):
            if i != x and game.matrix[i][y] in allowed:
                allowed.remove(game.matrix[i][y])

        # Remove from 'allowed' the values in the cell's column.
        for j in range(game.dim):
            if j != y and game.matrix[x][j] in allowed:
                allowed.remove(game.matrix[x][j])

        # Remove from 'allowed' values according to relation constraints.
        for a, b, c, d in game.relations:
            u = game.matrix[c][d]
            if (x, y) == (a, b) and v <= u:
                for av in allowed:
                    if av <= u:
                        allowed.remove(av)

        # If there are any allowed values left, add a tuple to the return list.
        if len(allowed) > 0:
            optimizations.append((x, y, allowed, u))
            count += 1

    return optimizations


def optimize(game, solution):
    """
    This function is the optimization function. The rest of the function in
    this module are auxiliary functions.
    :param game: a Futoshiki game object.
    :param solution: a Solution object.
    :return: an optimized Solution object.
    """

    # Check for unsatisfied cells.
    unsatisfied_cells = find_unsatisfied_cells(game, solution)
    if len(unsatisfied_cells) == 0:
        return solution

    # For the unsatisfied cells, find potential optimizations.
    available_optimizations = find_optimizations(game, unsatisfied_cells)
    if len(available_optimizations) == 0:
        return solution

    # Limit the number of optimizations, but handle the most urgent first.
    available_optimizations.sort(key=lambda tup: tup[3], reverse=True)
    available_optimizations = available_optimizations[:randint(2, game.dim)]

    # Create and optimized vector for a Solution object
    array = solution.vector.copy()
    for x, y, allowed_values, _ in available_optimizations:
        allowed = choice(allowed_values)
        k = 0
        broken = False
        for i in range(game.dim):
            if broken:
                break
            for j in range(game.dim):
                if (i, j) not in game.given.keys():
                    if (i, j) == (x, y):
                        array[k] = allowed
                        broken = True
                        break
                    k += 1

    return Solution(game, array)
