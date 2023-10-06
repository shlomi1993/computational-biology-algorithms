# File: evaluation.py
# Content: Functions for evaluating the results of the SOM.


import src.som as som
import matplotlib.pyplot as plt


def quantization_error(solution):
    """
    This function calculates the average distance between an input vector and
    the neuron that represents it.
    :param solution: a map from VRs to BMUs.
    :return: the quantization error
    """
    error = 0
    for vr, (bmu, _) in solution.items():
        error += som.RMSD(vr.vector, bmu.neuron)
    return error / len(solution)


def topological_error(solution):
    """
    This function counts the number of BMUs that their second-best neuron is not
    their neighbor (counts "bad" mapping).
    :param solution: a map from VRs to BMUs.
    :return: the topological error
    """
    miss = 0
    for bmu, validator in solution.values():
        if not bmu.is_in(validator.neighbors):
            miss += 1
    return miss / len(solution)


def plot(q_errors, t_errors, best_epoch, evaluator):
    """
    This function creates a plot portraying quantization and topological errors
    for each calculated epoch.
    :param q_errors: a list of quantization error per epoch.
    :param t_errors: a list of topological error per epoch.
    :param best_epoch: the epoch in which the best solution was found.
    :param evaluator: the evaluation method according to which the best
                      solution was determined.
    :return: None.
    """
    title = f'Error per Epochs\nBest epoch by {evaluator} was {best_epoch}'
    x_values = list(range(len(q_errors)))
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex='all')
    fig.suptitle(title)
    ax1.set(ylabel='Quantization Error')
    ax1.plot(x_values, q_errors, '-mo', markevery=[best_epoch])
    ax2.set(xlabel='Epoch', ylabel='Topological Error')
    ax2.plot(x_values, t_errors, '-ro', markevery=[best_epoch])
    fig.show()
