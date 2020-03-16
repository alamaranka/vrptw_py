from data.models import Route
from helpers.helpers import Helper


class InitialSolutionConstructor:
    def __init__(self, input_data):
        self.vertices = input_data.vertices
        self.vehicles = input_data.vehicles
        self.distances = input_data.distances

    def run(self):
        unvisited_customers = \
            [c for c in self.vertices if c.vertex_type == 1]
        unassigned_vehicles = self.vehicles

        depots = [v for v in self.vertices if v.vertex_type == 0]
        depot_from = depots[0]
        depot_to = depots[1]

        routes = []

        while (len(unvisited_customers) > 0) & (len(unassigned_vehicles) > 0):
            route = InsertionHeuristics(depot_from,
                                        depot_to,
                                        unvisited_customers,
                                        unassigned_vehicles,
                                        self.distances).generate()
            unvisited_customers = [c for c in unvisited_customers if c not in route.vertices]
            unassigned_vehicles = [v for v in unassigned_vehicles if v != route.vehicle]
            routes.append(route)

        return routes


class InsertionHeuristics:
    def __init__(self, depot_from, depot_to,
                 unvisited_customers,
                 unassigned_vehicles,
                 distances):
        self.depot_from = depot_from
        self.depot_to = depot_to
        self.unvisited_customers = unvisited_customers
        self.unassigned_vehicles = unassigned_vehicles
        self.distances = distances
        self.route = None

    def generate(self):
        self.initialize_route()
        # TODO: develop rest
        return self.route

    def initialize_route(self):
        vehicle = self.unassigned_vehicles.pop()
        self.route = Route(
            vertices=[self.depot_from,
                      self.depot_to],
            vehicle=vehicle
        )
        self.route = Helper.insert_customer(self.route,
                                            self.get_seed_customer(),
                                            len(self.route.vertices) - 1)

    def get_seed_customer(self):
        max_distance = 0.0
        seed_customer = None
        for customer in self.unvisited_customers:
            distance = Helper.calculate_distance(self.depot_from, customer, self.distances)
            if distance > max_distance:
                max_distance = distance
                seed_customer = customer
        self.unvisited_customers.remove(seed_customer)
        return seed_customer
