import enum


class AlgorithmType(enum.Enum):
    Invalid = 0
    Cplex = 1
    IterativeLocalSearch = 2
    TabuSearch = 3
    SimulatedAnnealing = 4


class DataSourceType(enum.Enum):
    NA = 0
    XML = 1
    SQL = 2


class VertexType(enum.Enum):
    Depot = 0,
    Customer = 1
