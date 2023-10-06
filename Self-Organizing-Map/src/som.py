# File: som.py
# Content: Self-Organized-Map algorithm implementation.


import numpy as np
from src.hexagonal import HexagonalGrid
from src.evaluation import quantization_error, topological_error


def init_weights(grid, low, high, length):
    """
    This function gets a hexagonal grid and initialized its neurons to
    randomized vectors of integers.
    :param grid: an instance of HexagonalGrid.
    :param low: the lowest number to sample.
    :param high: the highest number to sample.
    :param length: the dimension of the vector.
    :return:
    """
    for row in grid:
        for cell in row:
            rnd = np.random.randint(low, high, length)
            cell.neuron = np.array(rnd, dtype=np.float64)


def RMSD(V, N):
    """
    Stands for Root-Mean-Square-Deviation. This functions calculates the RMS of
    the difference between to given vectors using NumPy.
    :param V: vector number 1 (from a VotingRecord).
    :param N: vector number 2 (Cell's neuron).
    :return: The root-mean-square of V - N as float.
    """
    return np.sqrt(np.mean(np.square(V - N)))


def find_bmu(grid, vr):
    """
    The Best Matching Unit, or BMU, is the neuron in the grid closest to the
    given vector according to RMSD function.
    :param grid: an instance of HexagonalGrid.
    :param vr: a VotingRecord instance.
    :return: the best cell (BMU) and the second-best cell (validator).
    """
    candidates = []
    for row in grid:
        for cell in row:
            distance = RMSD(V=vr.vector, N=cell.neuron)
            candidates.append((cell, distance))
    candidates.sort(key=lambda tup: tup[1])
    bmu = candidates[0][0]
    validator = candidates[1][0]  # 2nd-best for Topological Error calculation.
    return bmu, validator


def update_weights(grid, reps):
    """
    This function updates the neurons in the grid by applying the update rule
    suggested in the instructions.
    :param grid: an instance of HexagonalGrid.
    :param reps: a map from VR to its representative (or BMU).
    :return: None. But it updates the weights.
    """
    for vr, (bmu, _) in reps.items():
        neighborhood = grid.get_neighborhood_of(bmu.pos[0], bmu.pos[1], 2)
        H = len(neighborhood) / 10
        for i, layer in neighborhood.items():
            h = round(H - i * 0.1, 1)
            for cell in layer:
                cell.neuron = (1 - h) * cell.neuron + h * vr.vector


def train(data, epochs=10):
    """
    This function creates an instance of HexagonalGrid, initializes its neurons
    (or weights), and then trains the model. In the end, it returns the solution
    for each epoch, and the model (i.e., the latest grid). This function also
    calculates the errors in each epoch.
    :param data: parsed and preprocessed data from the given input file.
    :param epochs: the number of iterations to run the network.
    :return: a list of solution per epoch, a model and lists of errors.
    """
    voting_records, _, max_votes = data
    model = HexagonalGrid(size=5)
    init_weights(model, 0, max_votes, len(voting_records[0].vector))
    solutions = []
    q_errors = []
    t_errors = []
    # voting_records.sort(reverse=False, key=lambda v: np.sum(v.vector))
    # voting_records.sort(reverse=True, key=lambda v: np.sum(v.vector))
    for t in range(epochs):
        np.random.shuffle(voting_records)  # to avoid bias.
        reps = {vr: find_bmu(model, vr) for vr in voting_records}
        q_errors.append(quantization_error(reps))
        t_errors.append(topological_error(reps))
        update_weights(model, reps)
        solutions.append(reps)
    return solutions, model, q_errors, t_errors


def analyze(results, positions):
    """
    This function gets a solution resulted by train() function and analyze it.
    :param results: a solution from train() function.
    :param positions: a list of the model's grid position for east access.
    :return: two dictionaries - one maps from a name of a town to a tuple if its
    cluster and the latest BMU, and the seconds maps from a cell position to a
    tuple of the represented vectors and their average cluster number (rounded)
    """
    temp = {}
    town_to_cell = {}
    cell_to_vectors = {}
    for vr, (bmu, _) in results.items():
        if bmu.pos in temp.keys():
            temp[bmu.pos].append(vr)
        else:
            temp[bmu.pos] = [vr]
        town_to_cell[vr.town] = (vr.cluster, bmu)
    for p in positions:
        if p in temp.keys():
            vrs = temp[p]
            average_cluster = round(sum(vr.cluster for vr in vrs) / len(vrs))
            cell_to_vectors[p] = (vrs, average_cluster)
        else:
            cell_to_vectors[p] = ([], 0)
    return town_to_cell, cell_to_vectors
