class CarWashOrder:
    def __init__(self, order_id: int, customer_name: str, service_type: str, status: str):
        self.order_id = order_id
        self.customer_name = customer_name
        self.service_type = service_type
        self.status = status

class DynamicOrderArray:
    def __init__(self, initial_capacity=4):
        self.array = [None] * initial_capacity
        self.size = 0
        self.capacity = initial_capacity

    def resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, order):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.size] = order
        self.size += 1

    def remove(self, order_id):
        for i in range(self.size):
            if self.array[i].order_id == order_id:
                # Shift elements to fill the gap
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.array[self.size - 1] = None
                self.size -= 1
                return True
        return False

    def get_by_status(self, status):
        return [order for order in self.array[:self.size] if order.status == status]

    def update_status(self, order_id, new_status):
        for i in range(self.size):
            if self.array[i].order_id == order_id:
                self.array[i].status = new_status
                return True
        return False

    def get_all_orders(self):
        return self.array[:self.size]


def main():
    order_system = DynamicOrderArray()
    
    
    orders = [
        CarWashOrder(1, "Ernest Izere", "Premium Wash", "pending"),
        CarWashOrder(2, "Sam Kalungi", "Basic Wash", "in_progress"),
        CarWashOrder(3, "Boby Wayne", "Deluxe Wash", "completed")
    ]
    
    for order in orders:
        order_system.append(order)
    
    
    pending_orders = order_system.get_by_status("pending")
    print(f"Pending orders: {len(pending_orders)}")
    
    
    order_system.update_status(1, "completed")
    
    
    order_system.remove(2)

if __name__ == "__main__":
    main()