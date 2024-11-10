# MSCS-532-Project: E-commerce Recommendation System

**Author**: Muluwork Geremew  
**Date**: 10/27/2024  

## Overview

This project is a partial implementation of an e-commerce recommendation system. The system uses various data structures to handle user preferences, manage the product catalog, and model user-product interactions. The core data structures include:

- **Binary Search Tree (BST)** for user preferences
- **Hash Table** for the product catalog
- **Directed Graph (DG)** for user-product relationships

Each of these data structures is encapsulated in separate modules to facilitate modular design and maintainability.

## Project Structure

Here’s a brief overview of each file in the project:

- **App.py**: The main application file. This script ties together the functionalities from the different modules and demonstrates the recommendation system’s basic operations.
- **BST.py**: Implements the Binary Search Tree data structure used for storing and retrieving user preferences.
- **DG.py**: Implements the Directed Graph data structure for modeling relationships between users and products based on their interactions.
- **HashTable.py**: Contains the Hash Table implementation used to manage and quickly access the product catalog.
- **Instance.py**: Defines any instances or sample data used to test and populate the data structures.
- **Recommendation.py**: Contains the logic for generating recommendations based on the relationships captured in the Directed Graph.
- **Search.py**: Provides search functionalities that may involve different data structures, particularly for retrieving user preferences or product data.
- **README.md**: This file, providing setup instructions, descriptions of each module, and usage guidelines.

## Setup Instructions

1. **Clone the Repository**:
   Clone this repository to your local machine.
   ```bash
   git clone https://github.com/maggie-21/MSCS-532-Project.git
   cd MSCS-532-Project
    ```
# Recommendation System Project

This project implements a recommendation system using various data structures, including a Binary Search Tree (BST), Hash Table, and Directed Graph (DG).

## Install Dependencies

This project requires Python 3. Ensure you have Python 3 installed on your machine. No additional libraries are required beyond the standard library.

## Run the Application

Use `App.py` to run the main application, which demonstrates the functionality of the recommendation system.

python App.py

## Testing Individual Modules

Each module can be run individually for testing purposes:

- **BST.py**:
  python BST.py

- **DG.py**:
  python DG.py

- **HashTable.py**:
  python HashTable.py

- **Recommendation.py**:
  python Recommendation.py

## Usage

- **App.py**: Integrates the functionalities of the BST, Hash Table, and Directed Graph to provide product recommendations based on user preferences and interactions. It includes sample data and demonstrates operations such as adding user preferences, storing product details, and retrieving recommendations.

- **BST.py**: Implements a Binary Search Tree (BST) to store and retrieve user preferences efficiently, enabling quick insertion, search, and deletion operations.

- **HashTable.py**: Provides a simple Hash Table for managing the product catalog with efficient insertion, retrieval, and deletion of products based on unique product IDs.

- **DG.py**: Implements a Directed Graph (DG) to model user-product relationships, where each node represents a user or product, and directed edges capture interactions (e.g., views, purchases) between them. This is crucial for collaborative filtering in recommendation engines.

- **Instance.py**: Includes sample data for testing and populating the data structures with mock user preferences, product data, and user-product interactions, enabling realistic testing.

- **Recommendation.py**: Contains the recommendation logic, using data from the Directed Graph to generate recommendations based on user interactions and preferences.

- **Search.py**: Provides search functionalities to retrieve user preferences and product data based on specified criteria.

## Future Work

- **Optimize Data Structures**: Implement self-balancing trees, handle hash collisions, and improve graph traversal efficiency.
- **Integrate Advanced Algorithms**: Use collaborative and content-based filtering to enhance recommendation accuracy.
- **Performance Testing**: Evaluate the system's scalability and performance under high data loads.
- **Develop an API or User Interface**: Create an interactive interface for user interaction and real-time recommendations.
