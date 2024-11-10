from BST import BST
from HashTable import HashTable
from DG import Graph
# Initialize the data structures
user_preferences = BST()
product_catalog = HashTable()
recommendation_graph = Graph()

# Step 1: Insert sample user preferences into the BST
# Let's assume user preferences are numerical values for simplicity
root = None
user_preferences_list = [25, 50, 10, 60, 30]
for preference in user_preferences_list:
    root = user_preferences.insert(root, preference)

# Step 2: Insert sample products into the Hash Table
product_catalog.insert(101, "Smartphone")
product_catalog.insert(102, "Laptop")
product_catalog.insert(103, "Headphones")
product_catalog.insert(104, "Tablet")
product_catalog.insert(105, "Smartwatch")

# Step 3: Simulate user-product interactions in the Directed Graph
# Adding interactions between users and products
recommendation_graph.add_edge("user1", 101)  # User1 viewed Smartphone
recommendation_graph.add_edge("user1", 102)  # User1 viewed Laptop
recommendation_graph.add_edge("user2", 103)  # User2 viewed Headphones
recommendation_graph.add_edge("user2", 105)  # User2 viewed Smartwatch
recommendation_graph.add_edge("user1", 104)  # User1 viewed Tablet

# Step 4: Retrieve recommendations based on user interactions
user_id = "user1"
recommendations = recommendation_graph.get_recommendations(user_id)

# Displaying product names for recommendations
print(f"Recommendations for {user_id}:")
for product_id in recommendations:
    product_name = product_catalog.search(product_id)
    if product_name:
        print(f" - {product_name}")

# Additional demonstration: Check if a specific user preference exists in the BST
preference_to_search = 30
preference_found = user_preferences.search(root, preference_to_search)

if preference_found:
    print(f"\nUser preference {preference_to_search} exists in the BST.")
else:
    print(f"\nUser preference {preference_to_search} does not exist in the BST.")
