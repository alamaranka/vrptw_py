import enum


class Algorithm(enum.Enum):
    Invalid = 0
    Cplex = 1
    IterativeLocalSearch = 2
    TabuSearch = 3
    SimulatedAnnealing = 4


class VertexType(enum.Enum):
    Depot = 0,
    Customer = 1