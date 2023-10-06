# File: game.py
# Content: a class represents a Futoshiki game and general methods.


class Futoshiki:
    """
    An instance of this class represents a Futoshiki game and its settings. It
    is also allows to set a solution to it represented by a vector of natural
    numbers, and to validate the solution.
    """

    def __init__(self, mat_size, given_digits, relations, stats=None):
        """
        Constructor. Initializes game's settings and constraints.
        :param mat_size: the dimension of the matrix.
        :param given_digits: a list of tuples (i, j, v) where v is a pre-given
               number in the i,j-cell of the matrix.
        :param relations: a list of tuples (a, b, c, d) that defines constraint
               where the value of the a,b-cell must be greater than the value in
               the c,d-cell.
        :param stats: a statistics object that helps gather and analyze info.
        """
        self.dim = mat_size
        self.matrix = [[0 for _ in range(mat_size)] for _ in range(mat_size)]
        self.given = {(i - 1, j - 1): v for i, j, v in given_digits}
        for i, j in self.given.keys():
            self.matrix[i][j] = self.given[(i, j)]
        self.solution_size = mat_size * mat_size - len(given_digits)
        self.relations = [(a-1, b-1, c-1, d-1) for (a, b, c, d) in relations]
        self.n_constraints = 2 * mat_size * mat_size + len(relations)
        self.stats = stats  # Optional.

    def set(self, solution):
        """
        This method get a solution represented by a vector of natural numbers
        and fill the not-occupied cells in the game's matrix.
        :param solution: a vector of natural numbers.
        :return: None.
        """
        k = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if (i, j) not in self.given.keys():
                    self.matrix[i][j] = solution[k]
                    k += 1

    def validate(self, solution):
        """
        This method allows to validate a given solution.
        :param solution: a vector of natural numbers.
        :return: True if the solution is legal, False otherwise.
        """
        self.set(solution)
        for x in range(self.dim):
            for y in range(self.dim):
                v = self.matrix[x][y]
                for i in range(self.dim):
                    if i != x and self.matrix[i][y] == v:
                        return False  # hit row-constraint.
                for j in range(self.dim):
                    if j != y and self.matrix[x][j] == v:
                        return False  # hit column-constraint.
                for a, b, c, d in self.relations:
                    if (x, y) == (a, b) and self.matrix[x][y] <= self.matrix[c][d]:
                        return False  # hit relation-constraint.
        return True  # If all constrains are satisfied.

    def reset(self):
        """
        This method allows removing solution from the game's matrix.
        :return:
        """
        for i in range(self.dim):
            for j in range(self.dim):
                if (i, j) not in self.given.keys():
                    self.matrix[i][j] = 0
