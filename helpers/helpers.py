import math

from data.model import Route


def calculate_distance(vertex_from, vertex_to, distances):
    if distances is not None:
        distance = get_first_or_default(
            [d for d in distances if (d.vertex_id_from == vertex_from.vertex_id) &
                                     (d.vertex_id_to == vertex_to.vertex_id)])
        return distance.distance_length
    else:
        x_dist = vertex_from.cx - vertex_to.cx
        y_dist = vertex_from.cy - vertex_to.cy
        return math.sqrt(math.pow(x_dist, 2) + math.pow(y_dist, 2))


def calculate_service_start(vertex_prev, vertex_next):
    return max(vertex_next.order.tw_start,
               vertex_prev.order.service_start +
               vertex_prev.order.service_time +
               calculate_distance(vertex_prev, vertex_next))


def is_route_feasible(customer, route_load, vehicle_capacity):
    is_capacity_exceeded = route_load > vehicle_capacity
    is_after_service_end = customer.order.service_start > customer.order.tw_end
    if is_capacity_exceeded | is_after_service_end:
        return False
    return True


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
            calculate_service_start(constructed_route.vertices[c - 1],
                                           constructed_route.vertices[c])
        constructed_route.vertices[c].route_id = constructed_route.route_id
        constructed_route.load += constructed_route.vertices[c].order.quantity
        constructed_route.distance += calculate_distance(constructed_route.vertices[c - 1],
                                                                constructed_route.vertices[c])
        if not is_route_feasible(constructed_route.vertices[c],
                                        constructed_route.load,
                                        constructed_route.vehicle.capacity):
            return None

    return constructed_route


def insert_customer(route, candidate_customer, index):
    customers_in_new_order = route.vertices
    customers_in_new_order.insert(index, candidate_customer)
    return construct_route(route, customers_in_new_order)


def get_first_or_default(lst):
    if len(lst) == 0:
        return None
    return lst[0]
