# Lab: Searching in a Logistics System (No Ordering)

# ------------------------------------------------------------
# Overview
# ------------------------------------------------------------
# In this lab, you will work with objects representing shipments
# in a logistics company.
#
# You will:
# - Implement classes with inheritance
# - Add custom methods to compare objects
# - Use a provided dataset
# - Implement linear search algorithms ONLY
# - Understand how object behavior supports searching

# IMPORTANT:
# You are NOT using sorting, binary search, or bisect in this lab.
# Focus only on objects and linear search.

# ------------------------------------------------------------
# Part 1: Implement Classes
# ------------------------------------------------------------
# Implement the following classes:
#
# Base class: Shipment
# Attributes:
# - shipment_id (int)
# - weight (float)
# - destination (string)

class Shipment:
    def __init__(self, shipment_id, weight, destination):
        # TODO
        pass

    # TODO: display method
    # Return a string like:
    # "ID: 101, Destination: Toronto, Weight: 10.5"

    # TODO: compare_destination(other)
    # Return True if both shipments have the same destination

    # TODO: compare_weight(other)
    # Return True if this shipment is heavier than the other


# Subclass: AirShipment
# Additional attribute: airline (string)

class AirShipment(Shipment):
    def __init__(self, shipment_id, weight, destination, airline):
        # TODO
        pass


# Subclass: GroundShipment
# Additional attribute: truck_company (string)

class GroundShipment(Shipment):
    def __init__(self, shipment_id, weight, destination, truck_company):
        # TODO
        pass


# ------------------------------------------------------------
# Part 2: Provided Dataset
# ------------------------------------------------------------

shipments = [
    AirShipment(101, 10.5, "Toronto", "Air Canada"),
    GroundShipment(202, 50.0, "Montreal", "FedEx"),
    AirShipment(303, 5.2, "Toronto", "WestJet"),
    GroundShipment(404, 70.3, "Vancouver", "UPS"),
    AirShipment(505, 8.0, "Calgary", "Air Canada"),
    GroundShipment(606, 60.0, "Toronto", "DHL"),
]

# ------------------------------------------------------------
# Part 3: Test Your Methods
# ------------------------------------------------------------

# TODO:
# Print all shipments using your display method


# TODO:
# Compare two shipments by destination


# TODO:
# Compare two shipments by weight


# ------------------------------------------------------------
# Part 4: Linear Search (Single Result)
# ------------------------------------------------------------
# Find the FIRST shipment going to a given destination
# Return index or -1


def linear_search_by_destination(shipments, destination):
    # TODO
    pass


# ------------------------------------------------------------
# Part 5: Linear Search (Multiple Results)
# ------------------------------------------------------------
# Return ALL shipments going to a destination


def find_all_by_destination(shipments, destination):
    # TODO
    pass


# ------------------------------------------------------------
# Part 6: Search by ID
# ------------------------------------------------------------
# Find shipment using shipment_id


def search_by_id(shipments, shipment_id):
    # TODO
    pass


# ------------------------------------------------------------
# Part 7: Heaviest Shipment
# ------------------------------------------------------------
# Find the heaviest shipment using your compare_weight method


def find_heaviest(shipment_list):
    # TODO
    pass


# ------------------------------------------------------------
# Part 8: Reflection
# ------------------------------------------------------------
# Answer in comments:
# 1. Why does linear search always work?
# 2. What is its time complexity?
# 3. How did object methods help your search?
# 4. Would your code still work if objects were different?


# ------------------------------------------------------------
# Bonus Challenge
# ------------------------------------------------------------
# Find all shipments heavier than a given weight


def find_heavier_than(shipments, weight):
    # TODO
    pass


# ------------------------------------------------------------
# End of Lab
# ------------------------------------------------------------
