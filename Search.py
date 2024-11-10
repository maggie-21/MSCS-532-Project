from HashTable import HashTable
# Create an instance of the HashTable
product_catalog = HashTable()

# Insert sample products into the catalog
product_catalog.insert(101, "Smartphone")
product_catalog.insert(102, "Laptop")
product_catalog.insert(103, "Headphones")

# Search for a specific product
product_id = 102
product = product_catalog.search(product_id)

if product:
    print(f"Product ID {product_id}: {product}")
else:
    print(f"Product ID {product_id} not found in the catalog.")

# Delete a product
product_catalog.delete(103)

# Verify if the product is deleted
deleted_product = product_catalog.search(103)
if deleted_product:
    print(f"Product ID 103: {deleted_product}")
else:
    print("Product ID 103 has been successfully deleted.")
