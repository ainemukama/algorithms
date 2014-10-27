from collections import defaultdict
from copy import deepcopy

class Graph(object):

    def __init__(self):
        self.path_exists = defaultdict(set)

    def isconnected(self, pair):
        if pair[1] in self.path_exists[pair[0]]:
            return True
        else:
            self.add(pair)
            return False

    def add(self, pair):
        nodes_from_0 = deepcopy(self.path_exists[pair[0]])
        nodes_from_1 = deepcopy(self.path_exists[pair[1]])
        for node in nodes_from_0:
            self.path_exists[node].add(pair[1])
            self.path_exists[pair[1]].add(node)
        for node in nodes_from_1:
            self.path_exists[node].add(pair[0])
            self.path_exists[pair[0]].add(node)

        self.path_exists[pair[0]].add(pair[1])
        self.path_exists[pair[1]].add(pair[0])

graph = Graph()
pairs = [(1,2), (2,3), (1,3), (3,4), (1,4), (1,1)]
for pair in pairs:
    print pair, graph.isconnected(pair)
