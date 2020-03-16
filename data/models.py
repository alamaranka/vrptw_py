class Vertex:
    def __init__(self, vertex_id=0, vertex_type=None,
                 route_id=0, cx=0, cy=0, order=None):
        self.vertex_id = vertex_id
        self.vertex_type = vertex_type
        self.route_id = route_id
        self.cx = cx
        self.cy = cy
        self.order = order


class Vehicle:
    def __init__(self, capacity=0, vehicle_type=None,
                 departure_node=0, arrival_node=0,
                 tw_start=0, tw_end=0):
        self.capacity = capacity
        self.vehicle_type = vehicle_type
        self.departure_node = departure_node
        self.arrival_node = arrival_node
        self.tw_start = tw_start
        self.tw_end = tw_end


class Order:
    def __init__(self, order_id=0, vertex_id=0,
                 quantity=0, service_time=0,
                 tw_start=0, tw_end=0,
                 service_start=0):
        self.order_id = order_id
        self.vertex_id = vertex_id
        self.quantity = quantity
        self.service_time = service_time
        self.service_start = service_start
        self.tw_start = tw_start
        self.tw_end = tw_end


class Distance:
    def __init__(self, vertex_id_start=0, vertex_id_end=0,
                 distance_length=0, distance_duration=0,
                 time_code=0):
        self.vertex_id_start = vertex_id_start
        self.vertex_id_end = vertex_id_end
        self.distance_length = distance_length
        self.distance_duration = distance_duration
        self.time_code = time_code


class InputData:
    def __init__(self, vertices=None,
                 vehicles=None, distances=None):
        self.vertices = vertices
        self.vehicles = vehicles
        self.distances = distances


class Route:
    def __init__(self, route_id=0,
                 vertices=None,
                 vehicle=None, load=0,
                 distance_length=0,
                 distance_time=0):
        self.route_id = route_id
        self.vertices = vertices
        self.vehicle = vehicle
        self.load = load
        self.distance_length = distance_length
        self.distance_time = distance_time


class Solution:
    def __init__(self, routes=None, cost=0, date=None):
        self.routes = routes
        self.cost = cost
        self.date = date
