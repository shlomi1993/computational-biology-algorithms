from src.game import Futoshiki
from src.solver import *


def parse_game(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    offset = 0
    mat_size = int(lines[offset])
    offset += 1
    n_given = int(lines[offset])
    offset += 1
    given_digits = []
    for i in range(n_given):
        given_row = lines[offset].split(' ')
        given_tup = int(given_row[0]), int(given_row[1]), int(given_row[2])
        given_digits.append(given_tup)
        offset += 1
    n_relations = int(lines[offset])
    offset += 1
    relations = []
    for i in range(n_relations):
        relation_row = lines[offset].split(' ')
        relation_tup = (int(relation_row[0]), int(relation_row[1]),
                        int(relation_row[2]), int(relation_row[3]))
        relations.append(relation_tup)
        offset += 1
    return Futoshiki(mat_size, given_digits, relations)


def debug():
    game = parse_game('./arg2.txt')
    st = genetic_solver(game, 100000, 100, 0.01, 0.8, 'lamark')
    st.print_stats()


debug()


# print_matrix(game.matrix)
# print(f'Validation: {game.validate(st.solution)}, fitness: {st.fitness}')
# true_solution = [5, 1, 2, 3, 2, 5, 3, 1, 4, 4, 3, 5, 1, 3, 1, 5, 4, 2, 1, 2, 4, 3, 5]
# print(f'Validation: {game.validate(true_solution)}, fitness: {fitness(game, true_solution)}')
# calibrate(game)

# def print_matrix(matrix):
#     for x in range(len(matrix)):
#         for y in range(len(matrix[0])):
#             print(matrix[x][y], end=' ')
#         print()
#     print()
#
# def calibrate(game):
#     elitism = [0.0, 0.01, 0.03, 0.05]
#     crossover = [i * 0.1 for i in range(1, 10)]
#     # optim = [None, 'lamark', 'darwin']
#     params = []
#     for a in elitism:
#         for b in crossover:
#             try:
#                 st = genetic_solver(game, 100000, 100, a, b)
#                 params.append(st)
#             except Exception:
#                 pass
#     best1 = min(params, key=lambda s: s.fitness)
#     best2 = min(params, key=lambda s: s.generations)
#     corr1 = True if best1.fitness == 58 else False
#     corr2 = True if best2.fitness == 58 else False
#     best1.print_stats(corr1, game.matrix)
#     best2.print_stats(corr2, game.matrix)
#     return best1

# from multiprocessing import Process
#
#
# def solver_wrapper(game, generations, pop_size, elitism, crossover, optim, outputs, idx):
#     outputs[idx] = genetic_solver(game, generations, pop_size, elitism, crossover, optim)
#
#
# def parallel_search(game, generations, pop_size, elitism, crossover, optim):
#     outputs = {}
#     pros = []
#     for i in range(5):
#         print('Thread Started')
#         p = Process(
#             target=solver_wrapper,
#             args=(game, generations, pop_size, elitism, crossover, optim, outputs, i)
#         )
#         pros.append(p)
#         p.start()
#
#     for t in pros:
#         t.join()
#
#     max_fitness = 0
#     result = None
#     for k, v in outputs.items():
#         if v.fitness > max_fitness:
#             max_fitness = v.fitness
#             result = v
#     return result
