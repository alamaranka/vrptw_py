from data.generators.xml import XMLReader
from data.models import InputData
from exact.cplex import CplexModel

xml_reader = XMLReader()

input_data = InputData(
    vertices=xml_reader.get_vertices(),
    vehicles=xml_reader.get_vehicles()
)

# initial_solution = InitialSolutionConstructor(input_data)
# routes = initial_solution.run()

cplex_model = CplexModel(input_data)
cplex_model.run()

print('end of line...')

