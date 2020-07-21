from config import Config
from data.xml_reader import XmlReader
from heuristics.initial import InitialSolutionConstructor

config = Config()
data = XmlReader().prepare_input_data()
initial_solution = InitialSolutionConstructor(data)
routes = initial_solution.run()

print('end of line...')

