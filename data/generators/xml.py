import xml.dom.minidom as xml_minidom

from data.config import Config
from data.models import Vertex, Vehicle, Order


class XMLReader:
    def __init__(self):
        file_operation = Config.get_file_operation()
        path = file_operation.instance_path + file_operation.instance_name
        self.doc = xml_minidom.parse(path)
        self.nodes = self.doc.getElementsByTagName('node')
        self.requests = self.doc.getElementsByTagName('request')
        self.fleet = self.doc.getElementsByTagName('fleet')

    def get_vertices(self):
        vertices = []
        orders = []
        ids = []
        vertex_types = []
        cx_s = []
        cy_s = []
        order_ids = []
        vertex_ids = []
        quantities = []
        service_times = []
        service_starts = []
        service_ends = []

        for node in self.nodes:
            ids.append(node.getAttribute('id'))
            vertex_types.append(node.getAttribute('type'))
            cx_s.append(node.getElementsByTagName('cx')[0].firstChild.data)
            cy_s.append(node.getElementsByTagName('cy')[0].firstChild.data)

        for request in self.requests:
            order_ids.append(request.getAttribute('id'))
            vertex_ids.append(request.getAttribute('node'))
            quantities.append(request.getElementsByTagName('quantity')[0].firstChild.data)
            service_times.append(request.getElementsByTagName('service_time')[0].firstChild.data)
            time_windows = request.getElementsByTagName('tw')

            for tw in time_windows:
                service_starts.append(tw.getElementsByTagName('start')[0].firstChild.data)
                service_ends.append(tw.getElementsByTagName('end')[0].firstChild.data)

        # no order for depot
        orders.append(None)

        for i in range(len(order_ids)):
            order = Order(
                order_id=int(order_ids[i]),
                vertex_id=int(vertex_ids[i]),
                quantity=float(quantities[i]),
                service_time=float(service_times[i]),
                service_start=float(service_starts[i]),
                service_end=float(service_ends[i])
            )

            orders.append(order)

        for i in range(len(ids)):
            vertex = Vertex(
                vertex_id=int(ids[i]),
                vertex_type=int(vertex_types[i]),
                cx=float(cx_s[i]),
                cy=float(cy_s[i]),
                order=orders[i]
            )

            vertices.append(vertex)

        # returning depot
        max_travel_time = self.fleet[0].getElementsByTagName('vehicle_profile')[0] \
            .getElementsByTagName('max_travel_time')[0].firstChild.data
        returning_depot = vertices[0]
        returning_depot.time_end = max_travel_time
        vertices.append(returning_depot)

        return vertices

    def get_vehicles(self):
        vehicles = []

        vehicle_type = self.fleet[0].getElementsByTagName('vehicle_profile')[0] \
            .getAttribute('type')
        number_of_vehicles = self.fleet[0].getElementsByTagName('vehicle_profile')[0] \
            .getAttribute('number')
        capacity = self.fleet[0].getElementsByTagName('vehicle_profile')[0] \
            .getElementsByTagName('capacity')[0].firstChild.data
        departure_node = self.fleet[0].getElementsByTagName('vehicle_profile')[0] \
            .getElementsByTagName('departure_node')[0].firstChild.data
        arrival_node = self.fleet[0].getElementsByTagName('vehicle_profile')[0] \
            .getElementsByTagName('arrival_node')[0].firstChild.data

        for i in range(int(number_of_vehicles)):
            vehicle = Vehicle(
                vehicle_type=int(vehicle_type),
                capacity=float(capacity),
                departure_node=int(departure_node),
                arrival_node=int(arrival_node)
            )

            vehicles.append(vehicle)

        return vehicles
