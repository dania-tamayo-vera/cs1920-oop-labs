# ------------------------------------------------------------
# Solution: Searching in a Logistics System
# ------------------------------------------------------------

class Shipment:
    def __init__(self, shipment_id, weight, destination):
        self.shipment_id = shipment_id
        self.weight = weight
        self.destination = destination

    def display(self):
        return f"ID: {self.shipment_id}, Destination: {self.destination}, Weight: {self.weight}"

    def compare_destination(self, other):
        return self.destination == other.destination

    def compare_weight(self, other):
        return self.weight > other.weight


class AirShipment(Shipment):
    def __init__(self, shipment_id, weight, destination, airline):
        super().__init__(shipment_id, weight, destination)
        self.airline = airline


class GroundShipment(Shipment):
    def __init__(self, shipment_id, weight, destination, truck_company):
        super().__init__(shipment_id, weight, destination)
        self.truck_company = truck_company


shipments = [
    AirShipment(101, 10.5, "Toronto", "Air Canada"),
    GroundShipment(202, 50.0, "Montreal", "FedEx"),
    AirShipment(303, 5.2, "Toronto", "WestJet"),
    GroundShipment(404, 70.3, "Vancouver", "UPS"),
    AirShipment(505, 8.0, "Calgary", "Air Canada"),
    GroundShipment(606, 60.0, "Toronto", "DHL"),
]


def linear_search_by_destination(shipments, destination):
    for i in range(len(shipments)):
        if shipments[i].destination == destination:
            return i
    return -1


def find_all_by_destination(shipments, destination):
    results = []
    for s in shipments:
        if s.destination == destination:
            results.append(s)
    return results


def search_by_id(shipments, shipment_id):
    for s in shipments:
        if s.shipment_id == shipment_id:
            return s
    return None


def find_heaviest(shipment_list):
    if not shipment_list:
        return None

    heaviest = shipment_list[0]

    for s in shipment_list[1:]:
        if s.compare_weight(heaviest):
            heaviest = s

    return heaviest


def find_heavier_than(shipments, weight):
    results = []
    for s in shipments:
        if s.weight > weight:
            results.append(s)
    return results


if __name__ == "__main__":
    print("All Shipments:")
    for s in shipments:
        print(s.display())

    print("\nFirst Toronto index:")
    print(linear_search_by_destination(shipments, "Toronto"))

    print("\nAll Toronto shipments:")
    for s in find_all_by_destination(shipments, "Toronto"):
        print(s.display())

    print("\nSearch by ID 404:")
    result = search_by_id(shipments, 404)
    print(result.display() if result else "Not found")

    print("\nHeaviest shipment:")
    print(find_heaviest(shipments).display())

    print("\nHeavier than 20:")
    for s in find_heavier_than(shipments, 20):
        print(s.display())
