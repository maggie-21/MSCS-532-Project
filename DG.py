# Directed Graph class for Recommendations
class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the graph
        self.graph = {}

    def add_edge(self, user, product):
        # Add an edge from user to product
        if user not in self.graph:
            self.graph[user] = []
        self.graph[user].append(product)

    def get_recommendations(self, user):
        # Get products associated with a particular user
        return self.graph.get(user, [])
