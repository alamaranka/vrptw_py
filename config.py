class ConnectionString:
    Server = ''
    Username = ''
    Password = ''
    Database = ''


class FileOperation:
    InstancePath = 'data/xml/'
    InstanceName = 'C109_025.xml'
    OutputPath = ''
    OutputName = 'output.json'


class SolverParam:
    TimeLimit = 1800
    MIPGap = 0.05
    Threads = 1


class InitialSolutionParam:
    Alpha_1 = 0.5
    Alpha_2 = 0.5
    Mu = 1
    Beta = 0


class SimulatedAnnealingParam:
    IterationCount = 1000
    InitialTemperature = 0.95
    Alpha = 200


class TabuSearchParam:
    TabuListSize = 5


class DiversificationParam:
    NumberOfNonImprovingIters = 2
    MinCustomersToRemove = 4
    MaxCustomersToRemove = 8


class HeuristicsParam:
    IterationCount = 200
    InitialSolutionParam = InitialSolutionParam()
    SimulatedAnnealingParam = SimulatedAnnealingParam()
    TabuSearchParam = TabuSearchParam()
    DiversificationParam = DiversificationParam()


class Config:
    SolverType = None  # solver type enum
    DataSource = None  # dat source enum
    ConnectionString = ConnectionString()
    FileOperation = FileOperation()
    SolverParam = SolverParam()
    HeuristicsParam = HeuristicsParam()

