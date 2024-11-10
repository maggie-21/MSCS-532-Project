from DG import Graph
# Create an instance of the Graph
recommendation_graph = Graph()

# Add sample interactions (user-product relationships)
recommendation_graph.add_edge("user1", "Smartphone")
recommendation_graph.add_edge("user1", "Laptop")
recommendation_graph.add_edge("user2", "Headphones")
recommendation_graph.add_edge("user2", "Smartwatch")
recommendation_graph.add_edge("user1", "Tablet")

# Retrieve recommendations for a specific user
user_id = "user1"
recommendations = recommendation_graph.get_recommendations(user_id)

print(f"Recommendations for {user_id}: {recommendations}")

# Testing another user
user_id = "user2"
recommendations = recommendation_graph.get_recommendations(user_id)

print(f"Recommendations for {user_id}: {recommendations}")
