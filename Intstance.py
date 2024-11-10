from BST import BST
# Create an instance of the BST
bst = BST()

# Insert sample user preferences
# Let's say these "preferences" are represented as numerical values for simplicity
root = None
preferences = [50, 30, 20, 40, 70, 60, 80]

for pref in preferences:
    root = bst.insert(root, pref)

# Search for a specific preference
search_key = 40
result = bst.search(root, search_key)

# Output the result of the search
if result:
    print(f"Preference {search_key} found in the BST.")
else:
    print(f"Preference {search_key} not found in the BST.")
