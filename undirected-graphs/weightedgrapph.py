

class WeightedGraph:
    def __init__(self):
        """
        Initialize an empty weighted graph.
        """
        self.graph = {}

    def add_flight(self, source, destination, cost):
        """
        Add a flight between source and destination airports with a given cost.
        """
        if source not in self.graph:
            self.graph[source] = {}
        if destination not in self.graph:
            self.graph[destination] = {}
        self.graph[source][destination] = cost

    def remove_flight(self, source, destination):
        """
        Remove the flight between source and destination airports.
        """
        if source in self.graph and destination in self.graph[source]:
            del self.graph[source][destination]

    def get_flights_from(self, source):
        """
        Get all flights departing from a given source airport.
        """
        return self.graph.get(source, {})

    def get_cost(self, source, destination):
        """
        Get the cost of the flight between source and destination airports.
        """
        if source in self.graph and destination in self.graph[source]:
            return self.graph[source][destination]
        else:
            return float('inf')  # Return infinity if no direct flight exists

    def get_airports(self):
        """
        Get all airports in the graph.
        """
        return list(self.graph.keys())
