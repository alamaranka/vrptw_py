from cplex.lib.python.docplex.mp.model import Model


class CplexModel:
    def __init__(self, input_data):
        self._model = Model()
        self._vertices = input_data.vertices
        self._vehicles = input_data.vehicles

    def run(self):
        self.set_solver_params()

    def set_solver_param(self):
        self._model.context.cplex_parameters.threads = 1
