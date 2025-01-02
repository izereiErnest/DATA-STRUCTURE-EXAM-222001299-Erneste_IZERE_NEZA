class Order:
    def __init__(self, order_id: int, customer_name: str, service_type: str, priority: int):
        self.order_id = order_id
        self.customer_name = customer_name
        self.service_type = service_type
        self.priority = priority
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    def append(self, order_id: int, customer_name: str, service_type: str, priority: int):
        new_order = Order(order_id, customer_name, service_type, priority)
        
        if self.is_empty():
            self.head = new_order
            new_order.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_order
            new_order.next = self.head
        self.size += 1
    
    def remove(self, order_id: int) -> bool:
        if self.is_empty():
            return False
        
        # If head is to be removed
        if self.head.order_id == order_id:
            if self.size == 1:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            self.size -= 1
            return True
        
        # Remove from middle or end
        current = self.head
        while current.next != self.head:
            if current.next.order_id == order_id:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False
    
    def rotate(self):
        """Rotate the list by moving head to next node"""
        if not self.is_empty():
            self.head = self.head.next
    
    def find_order(self, order_id: int) -> Order:
        if self.is_empty():
            return None
            
        current = self.head
        while True:
            if current.order_id == order_id:
                return current
            current = current.next
            if current == self.head:
                break
        return None
    
    def display_orders(self):
        orders = []
        if self.is_empty():
            return orders
            
        current = self.head
        while True:
            orders.append({
                'order_id': current.order_id,
                'customer_name': current.customer_name,
                'service_type': current.service_type,
                'priority': current.priority
            })
            current = current.next
            if current == self.head:
                break
        return orders

# Example usage
def test_circular_linked_list():
    order_list = CircularLinkedList()
    
    # Add some orders
    order_list.append(1, "Ernest IZERE", "Premium Wash", 1)
    order_list.append(2, "Sam Kalungi", "Basic Wash", 2)
    order_list.append(3, "Boby Wayne", "Deluxe Wash", 3)
    
    print("Initial orders:", order_list.display_orders())
    
    # Rotate the list
    order_list.rotate()
    print("After rotation:", order_list.display_orders())
    
    # Find an order
    order = order_list.find_order(2)
    if order:
        print(f"Found order for: {order.customer_name}")
    
    # Remove an order
    order_list.remove(2)
    print("After removing order 2:", order_list.display_orders())

if __name__ == "__main__":
    test_circular_linked_list()