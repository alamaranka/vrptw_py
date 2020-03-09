import json


class Config:

    @staticmethod
    def get_solver_type():
        return ConfigData.get_config()['SolverType']

    @staticmethod
    def get_data_source():
        return ConfigData.get_config()['DataSource']

    @staticmethod
    def get_connection_string():
        parent = ConfigData.get_config()['ConnectionString']
        return ConnectionString(
            dns=parent['DNS'],
            port=parent['Port'],
            db_name=parent['DBName'],
            user_name=parent['Username'],
            password=parent['Password']
        )

    @staticmethod
    def get_file_operation():
        parent = ConfigData.get_config()['FileOperation']
        return FileOperation(
            instance_path=parent['InstancePath'],
            instance_name=parent['InstanceName'],
            output_path=parent['OutputPath'],
            output_name=parent['OutputName']
        )

    @staticmethod
    def get_solver_param():
        parent = ConfigData.get_config()['SolverParam']
        return SolverParam(
            time_limit=parent['TimeLimit'],
            mip_gap=parent['MIPGap'],
            threads=parent['Threads']
        )

    @staticmethod
    def get_heuristics_param():
        parent = ConfigData.get_config()['HeuristicsParam']
        return HeuristicsParam(
            iteration_count=parent['IterationCount'],
            initial_solution_param=Config.get_initial_solution_param(parent),
            simulated_annealing_param=Config.get_simulated_annealing_param(parent),
            tabu_search_param=Config.get_tabu_search_param(parent),
            diversification_param=Config.get_diversification_param(parent)
        )

    @staticmethod
    def get_initial_solution_param(parent):
        child = parent['InitialSolutionParam']
        return InitialSolutionParam(
            alpha1=child['Alpha1'],
            alpha2=child['Alpha2'],
            mu=child['Mu'],
            beta=child['Beta']
        )

    @staticmethod
    def get_simulated_annealing_param(parent):
        child = parent['SimulatedAnnealingParam']
        return SimulatedAnnealingParam(
            iteration_count=child['IterationCount'],
            initial_temperature=child['InitialTemperature'],
            alpha=child['Alpha']
        )

    @staticmethod
    def get_tabu_search_param(parent):
        child = parent['TabuSearchParam']
        return TabuSearchParam(
            tabu_list_size=child['TabuListSize']
        )

    @staticmethod
    def get_diversification_param(parent):
        child = parent['DiversificationParam']
        return DiversificationParam(
            number_of_nonimproving_iters=child['NumberOfNonImprovingIters'],
            min_customers_to_remove=child['MinCustomersToRemove'],
            max_customers_to_remove=child['MaxCustomersToRemove']
        )


class ConnectionString:
    def __init__(self, dns='', port='', db_name='',
                 user_name='', password=''):
        self.dns = dns
        self.port = port
        self.db_name = db_name
        self.user_name = user_name
        self.password = password


class FileOperation:
    def __init__(self, instance_path='', instance_name='',
                 output_path='', output_name=''):
        self.instance_path = instance_path
        self.instance_name = instance_name
        self.output_path = output_path
        self.output_name = output_name


class SolverParam:
    def __init__(self, time_limit=0, mip_gap=0, threads=0):
        self.time_limit = time_limit
        self.mip_gap = mip_gap
        self.threads = threads


class HeuristicsParam:
    def __init__(self, iteration_count=0, initial_solution_param=None,
                 simulated_annealing_param=None, tabu_search_param=None,
                 diversification_param=None):
        self.iteration_count = iteration_count
        self.initial_solution_param = initial_solution_param
        self.simulated_annealing_param = simulated_annealing_param
        self.tabu_search_param = tabu_search_param
        self.diversification_param = diversification_param


class InitialSolutionParam:
    def __init__(self, alpha1=0, alpha2=0, mu=0, beta=0):
        self.alpha1 = alpha1
        self.alpha2 = alpha2
        self.mu = mu
        self.beta = beta


class SimulatedAnnealingParam:
    def __init__(self, iteration_count=0, initial_temperature=0, alpha=0):
        self.iteration_count = iteration_count
        self.initial_temperature = initial_temperature
        self.alpha = alpha


class TabuSearchParam:
    def __init__(self, tabu_list_size=0):
        self.tabu_list_size = tabu_list_size


class DiversificationParam:
    def __init__(self, number_of_nonimproving_iters=0,
                 min_customers_to_remove=0,
                 max_customers_to_remove=0):
        self.number_of_nonimproving_iters = number_of_nonimproving_iters
        self.min_customers_to_remove = min_customers_to_remove
        self.max_customers_to_remove = max_customers_to_remove


class ConfigData:

    @staticmethod
    def get_config():
        with open('config.json') as json_data_file:
            return json.load(json_data_file)
