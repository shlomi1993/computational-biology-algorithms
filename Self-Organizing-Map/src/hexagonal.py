# File: hexagonal.py
# Content: Cell and Hexagonal data-structures implementation.


class Cell:
    """
    A cell is the component of which the hexagonal grid is composed. It has a
    position in (i, j) coordinates, a neuron which is a pointer to a vector, and
    a list of neighboring cells.
    """
    def __init__(self, i, j):
        """
        Constructor. Creates a Cell instance by the given i, j coordinates.
        :param i: hexagonal grid's row i.
        :param j: hexagonal grid's column j.
        """
        self.pos = (i, j)
        self.neuron = None  # Initializes when the size of the grid is known.
        self.neighbors = []

    def __str__(self):
        """
        This method allows printing and object from this class.
        :return: printing string.
        """
        return f'Cell {self.pos} holds: neuron{self.neuron}'

    def is_in(self, group):
        """
        This method checks if the cell in a member of the given list or set.
        :param group: a list or a set.
        :return: True of yes, False otherwise.
        """
        for x in group:
            if x.pos == self.pos:
                return True
        return False


class HexagonalGrid:
    """
    This data-structure was designed to complete the assignment. It is made up
    of cells, row-by row.
    """

    def __init__(self, size):
        """
        Constructor. Creates an instance of a HexagonalGrid.
        :param size: the number of cells in the edge of the grid.
        """

        # Create the first row and connects its cells.
        first_row = [Cell(0, j) for j in range(size)]
        for j in range(size - 1):
            first_row[j].neighbors.append(first_row[j + 1])
            first_row[j + 1].neighbors.append(first_row[j])
        self.rows = [first_row]

        # For each row, create the next row with an additional cell and connect
        # each of the new cells between themselves and their parents.
        for i in range(1, size):
            new_row = [Cell(i, j) for j in range(size + i)]
            for j in range(size + i - 1):
                new_row[j].neighbors.append(self.rows[i - 1][j])
                new_row[j + 1].neighbors.append(self.rows[i - 1][j])
                new_row[j].neighbors.append(new_row[j + 1])
                new_row[j + 1].neighbors.append(new_row[j])
                self.rows[i - 1][j].neighbors.append(new_row[j])
                self.rows[i - 1][j].neighbors.append(new_row[j + 1])
            self.rows.append(new_row)

        # Once 'size' rows created, for each row, create the next row with one
        # less cell, and connect each of the new cells between themselves and
        # their parents.
        max_size = len(self.rows[-1])
        k = 1
        for i in range(size, max_size):
            new_row = [Cell(i, j) for j in range(max_size - k)]
            k += 1
            for j in range(len(new_row)):
                new_row[j].neighbors.append(self.rows[i - 1][j])
                new_row[j].neighbors.append(self.rows[i - 1][j + 1])
                if j < len(new_row) - 1:
                    new_row[j].neighbors.append(new_row[j + 1])
                if j > 0:
                    new_row[j].neighbors.append(new_row[j - 1])
                self.rows[i - 1][j].neighbors.append(new_row[j])
                self.rows[i - 1][j + 1].neighbors.append(new_row[j])
            self.rows.append(new_row)

        # Store a list of possible coordinates as an attribute for easy access.
        self.positions = []
        for row in self.rows:
            for cell in row:
                self.positions.append(cell.pos)

    def __str__(self):
        """
        This method allows printing and object from this class.
        :return: printing string.
        """
        string = ''
        for i, row in zip(range(len(self.rows)), self.rows):
            string += f'Row {i}:\n'
            for j, cell in zip(range(len(row)), row):
                string += f'  Col {j}: ' + cell.__str__() + '\n'
            string += '\n'
        return string

    def __iter__(self):
        """
        This method sets the data-structure's iterator as the grid's iterator.
        :return: an iterator for easy traversing.
        """
        self.iter = self.rows.__iter__()
        return self

    def __next__(self):
        """
        Additional method for iterator implementation.
        """
        return self.iter.__next__()

    def __getitem__(self, item):
        """
        This method allows easy access to an item in the hexagonal grid.
        :param item: an item, or a Cell.
        :return: an item from the attribute "rows".
        """
        return self.rows.__getitem__(item)

    def get_neighbors_of(self, i, j):
        """
        This method returns a list of the neighbors of the i,j-cell.
        :param i: row coordinate.
        :param j: column coordinate.
        :return:
        """
        return self.rows[i][j].neighbors

    def get_neighborhood_of(self, i, j, k):
        """
        This method returns a dictionary of k lists, where the key (0 <= x <= k)
        maps to a list of all the neighbors of the i,j-cell from the x'th ring.
        :param i: row coordinate.
        :param j: column coordinate.
        :param k: The number of layers (rings) of neighbors to extract.
        :return:
        """

        # Layer 0 -- contains the cell itself.
        neighborhood = {0: [self.rows[i][j]]}
        if k == 0:
            return neighborhood

        # Layer 1 -- contains the <6 immediate neighbors of the cell.
        neighborhood[1] = self.get_neighbors_of(i, j)
        if k == 1:
            return neighborhood

        # Layer x -- contains all the neighbors of the cells collected so far,
        # without the cells collected so far.
        collected = neighborhood[0] + neighborhood[1]
        for x in range(2, k + 1):
            next_layer = []
            prev_layer = neighborhood[x - 1]
            for n in prev_layer:
                mid_set = self.get_neighbors_of(n.pos[0], n.pos[1])
                for nn in mid_set:
                    if not nn.is_in(prev_layer) and not nn.is_in(collected):
                        next_layer.append(nn)
                        collected.append(nn)
            neighborhood[x] = next_layer

        # Return k-layers neighborhood.
        return neighborhood
