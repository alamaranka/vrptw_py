from data.models import Route
from helpers.helpers import Helper


class InitialSolutionConstructor:
    def __init__(self, input_data):
        self.vertices = input_data.vertices
        self.vehicles = input_data.vehicles
        self.unvisited_customers = None
        self.unassigned_vehicles = None
        self.starting_depot = None
        self.ending_depot = None

    def run(self):
        self.unvisited_customers = \
            [c for c in self.vertices if c.vertex_type == 1]
        self.unassigned_vehicles = self.vehicles

        depots = [v for v in self.vertices if v.vertex_type == 0]
        self.starting_depot = depots[0]
        self.ending_depot = depots[1]

        routes = []

        while (len(self.unvisited_customers) > 0) & (len(self.unassigned_vehicles) > 0):
            route = InsertionHeuristics(self.starting_depot,
                                        self.ending_depot,
                                        self.unvisited_customers,
                                        self.unassigned_vehicles).generate()
            self.unvisited_customers = [c for c in self.unvisited_customers if c not in route.vertices]
            self.unassigned_vehicles = [v for v in self.unassigned_vehicles if v != route.vehicle]
            routes.append(route)

        return routes


class InsertionHeuristics:
    def __init__(self, starting_depot, ending_depot,
                 unvisited_customers,
                 unassigned_vehicles):
        self.starting_depot = starting_depot
        self.ending_depot = ending_depot
        self.unvisited_customers = unvisited_customers
        self.unassigned_vehicles = unassigned_vehicles
        self.route = None

    def generate(self):
        self.initialize_route()
        # TODO: develop rest
        return self.route

    def initialize_route(self):
        vehicle = self.unassigned_vehicles.pop()
        self.route = Route(
            vertices=[self.starting_depot,
                      self.ending_depot],
            vehicle=vehicle
        )
        self.route = Helper.insert_customer(self.route,
                                            self.get_seed_customer(),
                                            len(self.route.vertices) - 1)

    def get_seed_customer(self):
        max_distance = 0.0
        seed_customer = None
        for customer in self.unvisited_customers:
            distance = Helper.calculate_distance(self.starting_depot, customer)
            if distance > max_distance:
                max_distance = distance
                seed_customer = customer
        self.unvisited_customers.remove(seed_customer)
        return seed_customer
