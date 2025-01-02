class Order:
    def __init__(self, order_id: int, customer_name: str, service_type: str, priority: int):
        self.order_id = order_id
        self.customer_name = customer_name
        self.service_type = service_type
        self.priority = priority
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    def append(self, order_id: int, customer_name: str, service_type: str, priority: int):
        new_order = Order(order_id, customer_name, service_type, priority)
        
        if self.is_empty():
            self.head = new_order
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_order
        self.size += 1
    
    def remove(self, order_id: int) -> bool:
        if self.is_empty():
            return False
            
        if self.head.order_id == order_id:
            self.head = self.head.next
            self.size -= 1
            return True
            
        current = self.head
        while current.next:
            if current.next.order_id == order_id:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False
    
    def find_order(self, order_id: int) -> Order:
        current = self.head
        while current:
            if current.order_id == order_id:
                return current
            current = current.next
        return None
    
    def display_orders(self):
        orders = []
        current = self.head
        while current:
            orders.append({
                'order_id': current.order_id,
                'customer_name': current.customer_name,
                'service_type': current.service_type,
                'priority': current.priority
            })
            current = current.next
        return orders

# Example usage
def test_singly_linked_list():
    order_list = SinglyLinkedList()
    
    # Add some orders
    order_list.append(1, "Ernset IZERE", "Premium Wash", 1)
    order_list.append(2, "Sam Kalungi", "Basic Wash", 2)
    order_list.append(3, "Boby Wayne", "Deluxe Wash", 3)
    
    print("Initial orders:", order_list.display_orders())
    
    # Find an order
    order = order_list.find_order(2)
    if order:
        print(f"Found order for: {order.customer_name}")
    
    # Remove an order
    order_list.remove(2)
    print("After removing order 2:", order_list.display_orders())

if __name__ == "__main__":
    test_singly_linked_list()