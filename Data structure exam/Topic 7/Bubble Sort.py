import datetime
from enum import Enum

class ServiceType(Enum):
    BASIC_WASH = 1
    DELUXE_WASH = 2
    PREMIUM_WASH = 3

class Order:
    def __init__(self, order_id, customer, vehicle, service_type, priority):
        self.order_id = order_id
        self.customer = customer
        self.vehicle = vehicle
        self.service_type = service_type
        self.priority = priority
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return (f"Order({self.order_id}, {self.customer.name}, {self.vehicle.license_plate}, "
                f"{self.service_type.name}, Priority: {self.priority}, Time: {self.created_at})")

class Customer:
    def __init__(self, customer_id, name, phone, email):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

class Vehicle:
    def __init__(self, license_plate, make, model, color):
        self.license_plate = license_plate
        self.make = make
        self.model = model
        self.color = color

class OrderSorter:
    @staticmethod
    def bubble_sort_by_priority(orders: list) -> list:
        n = len(orders)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if orders[j].priority < orders[j + 1].priority:
                    orders[j], orders[j + 1] = orders[j + 1], orders[j]
                    swapped = True
            if not swapped:
                break
        return orders

    @staticmethod
    def bubble_sort_by_time(orders: list) -> list:
        n = len(orders)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if orders[j].created_at > orders[j + 1].created_at:
                    orders[j], orders[j + 1] = orders[j + 1], orders[j]
                    swapped = True
            if not swapped:
                break
        return orders

    @staticmethod
    def bubble_sort_by_service_type(orders: list) -> list:
        n = len(orders)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if orders[j].service_type.value > orders[j + 1].service_type.value:
                    orders[j], orders[j + 1] = orders[j + 1], orders[j]
                    swapped = True
            if not swapped:
                break
        return orders

# Example usage
def main():
    sorter = OrderSorter()
    
    # Create sample orders
    orders = [
        Order(1, Customer(1, "John", "123", "john@email.com"), 
              Vehicle("ABC123", "Toyota", "Camry", "Blue"),
              ServiceType.BASIC_WASH, 2),
        Order(2, Customer(2, "Jane", "456", "jane@email.com"),
              Vehicle("XYZ789", "Honda", "Civic", "Red"),
              ServiceType.PREMIUM_WASH, 1),
        Order(3, Customer(3, "Bob", "789", "bob@email.com"),
              Vehicle("DEF456", "Ford", "Focus", "Black"),
              ServiceType.DELUXE_WASH, 3)
    ]
    
    # Sort by different criteria
    sorted_by_priority = sorter.bubble_sort_by_priority(orders.copy())
    sorted_by_time = sorter.bubble_sort_by_time(orders.copy())
    sorted_by_service = sorter.bubble_sort_by_service_type(orders.copy())
    
    # Display results
    print("\nSorted by Priority:")
    for order in sorted_by_priority:
        print(order)

    print("\nSorted by Created Time:")
    for order in sorted_by_time:
        print(order)

    print("\nSorted by Service Type:")
    for order in sorted_by_service:
        print(order)

if __name__ == "__main__":
    main()
