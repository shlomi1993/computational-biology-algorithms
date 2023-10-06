# File: parser.py
# Content: A VotingRecord class and a function for parsing input CSV files.


import numpy as np


class VotingRecord:
    """
    This class gather information about a specific voting record.
    """

    def __init__(self, town, cluster, vector):
        """
        Constructor. A voting record contains municipality name, or town, an
        economic cluster, and a voting vector.
        :param town: municipality according to given input file.
        :param cluster: economic cluster according to given input file.
        :param vector: number of votes for each party according to input file.
        """
        self.town = town
        self.cluster = cluster
        self.vector = vector

    def __str__(self):
        """
        This method allows printing and object from this class.
        :return: printing string.
        """
        return f'{self.town} ({self.cluster}): votes{self.vector}'


def parse(file_path):
    """
    This functions parses a given input CSV file.
    :param file_path: the path to the input file.
    :return: a list of Voting Records, a mapper from party index to its name,
    and the maximal number of votes that was found.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    parties = lines[0].split(',')[3:]
    zipped = zip(range(len(parties)), parties)
    mapper = {int(idx): name for idx, name in zipped}
    mapper[len(mapper)] = 'others'  # Save reminders as well.
    voting_records = []
    max_votes = 0
    for line in lines[1:]:
        values = line.split(',')
        municipality = values[0]
        cluster = int(values[1])
        total = int(values[2])
        arr = [int(i) for i in values[3:]]
        arr.append(total - sum(arr))
        vector = np.array(arr, dtype=np.float)
        max_votes = max(max_votes, max(vector))
        voting_records.append(VotingRecord(municipality, cluster, vector))
    return voting_records, mapper, max_votes
