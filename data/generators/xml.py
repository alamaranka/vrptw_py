import xml.dom.minidom as xml_minidom
import copy

from data.config import Config
from data.models import Vertex, Vehicle, Order
from helpers.helpers import Helper


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

        for request in self.requests:
            order_id = int(request.getAttribute('id'))
            vertex_id = int(request.getAttribute('node'))
            quantity = float(request.getElementsByTagName('quantity')[0].firstChild.data)
            service_time = float(request.getElementsByTagName('service_time')[0].firstChild.data)
            time_window = request.getElementsByTagName('tw')[0]
            tw_start = float(time_window.getElementsByTagName('start')[0].firstChild.data)
            tw_end = float(time_window.getElementsByTagName('end')[0].firstChild.data)

            order = Order(order_id=order_id,
                          vertex_id=vertex_id,
                          quantity=quantity,
                          service_time=service_time,
                          tw_start=tw_start,
                          tw_end=tw_end)

            orders.append(order)

        for node in self.nodes:
            vertex_id = int(node.getAttribute('id'))
            vertex_type = int(node.getAttribute('type'))
            cx = float(node.getElementsByTagName('cx')[0].firstChild.data)
            cy = float(node.getElementsByTagName('cy')[0].firstChild.data)
            order = Helper.get_first_or_default([o for o in orders if o.vertex_id == vertex_id])

            vertex = Vertex(vertex_id=vertex_id,
                            vertex_type=vertex_type,
                            cx=cx, cy=cy, order=order)

            vertices.append(vertex)

        # prepare depots
        depots = [v for v in vertices if v.vertex_type == 0]
        for depot in depots:
            depot.order = Order(vertex_id=depot.vertex_id)
            vertices.append(copy.deepcopy(depot))

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
        max_travel_time = self.fleet[0].getElementsByTagName('vehicle_profile')[0] \
            .getElementsByTagName('max_travel_time')[0].firstChild.data

        for i in range(int(number_of_vehicles)):
            vehicle = Vehicle(
                vehicle_type=int(vehicle_type),
                capacity=float(capacity),
                departure_node=int(departure_node),
                arrival_node=int(arrival_node),
                tw_end=float(max_travel_time)
            )

            vehicles.append(vehicle)

        return vehicles
