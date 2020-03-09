from data.generators.xml import XMLReader
from data.models import Dataset

xml_reader = XMLReader()

data = Dataset(
    vertices=xml_reader.get_vertices(),
    vehicles=xml_reader.get_vehicles()
)

print('end of line...')

