import math

from data.models import Route


class Helper:
    @staticmethod
    def calculate_distance(v_start, v_end):
        term1 = math.pow(v_start.cx - v_end.cx, 2)
        term2 = math.pow(v_start.cy - v_end.cy, 2)
        return math.sqrt(term1 + term2)

    @staticmethod
    def calculate_service_start(vertex_prev, vertex_next):
        return max(vertex_next.order.tw_start,
                   vertex_prev.order.service_start +
                   vertex_prev.order.service_time +
                   Helper.calculate_distance(vertex_prev, vertex_next))

    @staticmethod
    def is_route_feasible(customer, route_load, vehicle_capacity):
        is_capacity_exceeded = route_load > vehicle_capacity
        is_after_service_end = customer.order.service_start > customer.order.tw_end
        if is_capacity_exceeded | is_after_service_end:
            return False
        return True

    @staticmethod
    def construct_route(route, customers):
        """
        this re-constructs the route once a vertex inserted,
        by updating relevant variables and checking feasibility.
        :param route: route before insert operation
        :param customers: customers in visit order
        :return: re-constructed route
        """
        constructed_route = Route(route.route_id,
                                  vertices=[customers[0]],
                                  vehicle=route.vehicle,
                                  load=0.0,
                                  distance=0.0)
        for c in range(1, len(customers)):
            constructed_route.vertices.append(customers[c])
            constructed_route.vertices[c].order.service_start = \
                Helper.calculate_service_start(constructed_route.vertices[c - 1],
                                               constructed_route.vertices[c])
            constructed_route.vertices[c].route_id = constructed_route.route_id
            constructed_route.load += constructed_route.vertices[c].order.quantity
            constructed_route.distance += Helper.calculate_distance(constructed_route.vertices[c - 1],
                                                                    constructed_route.vertices[c])
            if not Helper.is_route_feasible(constructed_route.vertices[c],
                                            constructed_route.load,
                                            constructed_route.vehicle.capacity):
                return None

        return constructed_route

    @staticmethod
    def insert_customer(route, candidate_customer, index):
        customers_in_new_order = route.vertices
        customers_in_new_order.insert(index, candidate_customer)
        return Helper.construct_route(route, customers_in_new_order)
