class Vertex:
    def __init__(self, vertex_id=0, vertex_type=None,
                 route_id=0, cx=0, cy=0, order=None):
        self.vertex_id = vertex_id
        self.vertex_type = vertex_type
        self.route_id = route_id
        self.cx = cx
        self.cy = cy
        self.order = order


class Order:
    def __init__(self, order_id=0, vertex_id=0,
                 quantity=0, service_time=0,
                 tw_start=0, tw_end=0, service_start=0):
        self.order_id = order_id
        self.vertex_id = vertex_id
        self.quantity = quantity
        self.service_time = service_time
        self.service_start = service_start
        self.tw_start = tw_start
        self.tw_end = tw_end


class InputData:
    def __init__(self, vertices=None, vehicles=None):
        self.vertices = vertices
        self.vehicles = vehicles


class Route:
    def __init__(self, route_id=0, vertices=None,
                 vehicle=None, load=0, distance=0):
        self.route_id = route_id
        self.vertices = vertices
        self.vehicle = vehicle
        self.load = load
        self.distance = distance


class Solution:
    def __init__(self, routes=None, cost=0):
        self.routes = routes
        self.cost = cost


class Vehicle:
    def __init__(self, capacity=0, vehicle_type=None,
                 departure_node=0, arrival_node=0):
        self.capacity = capacity
        self.vehicle_type = vehicle_type
        self.departure_node = departure_node
        self.arrival_node = arrival_node
