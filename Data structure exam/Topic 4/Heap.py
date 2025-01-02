from typing import Optional

class Order:
    def __init__(self, order_id, customer_name, priority):
        self.order_id = order_id
        self.customer_name = customer_name
        self.priority = priority

    def __repr__(self):
        return f"Order(ID: {self.order_id}, Customer: {self.customer_name}, Priority: {self.priority})"

class OrderHeap:
    def __init__(self, capacity: int):
        self.heap = []
        self.capacity = capacity

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def left_child(self, i: int) -> int:
        return 2 * i + 1

    def right_child(self, i: int) -> int:
        return 2 * i + 2

    def swap(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_full(self) -> bool:
        return len(self.heap) >= self.capacity

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def insert(self, order: Order) -> bool:
        if self.is_full():
            # If new order has higher priority than root, replace root
            if order.priority > self.heap[0].priority:
                self.heap[0] = order
                self._heapify_down(0)
                return True
            return False
        
        self.heap.append(order)
        self._heapify_up(len(self.heap) - 1)
        return True

    def get_highest_priority(self) -> Optional[Order]:
        if self.is_empty():
            return None
        return self.heap[0]

    def extract_highest_priority(self) -> Optional[Order]:
        if self.is_empty():
            return None

        highest_priority = self.heap[0]
        last_item = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_item
            self._heapify_down(0)

        return highest_priority

    def _heapify_up(self, i: int):
        parent = self.parent(i)
        if i > 0 and self.heap[i].priority > self.heap[parent].priority:
            self.swap(i, parent)
            self._heapify_up(parent)

    def _heapify_down(self, i: int):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        heap_len = len(self.heap)

        if (left < heap_len and 
            self.heap[left].priority > self.heap[largest].priority):
            largest = left

        if (right < heap_len and 
            self.heap[right].priority > self.heap[largest].priority):
            largest = right

        if largest != i:
            self.swap(i, largest)
            self._heapify_down(largest)

    def get_all_orders(self) -> list:
        return sorted(self.heap, key=lambda x: x.priority, reverse=True)

# Example usage
def main():
    order_heap = OrderHeap(capacity=5)

    # Adding orders
    orders = [
        Order(1, "Alice", 3),
        Order(2, "Bob", 1),
        Order(3, "Charlie", 5),
        Order(4, "Diana", 4),
        Order(5, "Eve", 2),
        Order(6, "Frank", 6)  # This order has higher priority and might replace an existing one
    ]

    print("Inserting Orders:")
    for order in orders:
        inserted = order_heap.insert(order)
        print(f"Inserted {order} - {'Success' if inserted else 'Failed (Heap Full)'}")

    # Display all orders in heap
    print("\nOrders in Heap (Sorted by Priority):")
    all_orders = order_heap.get_all_orders()
    for order in all_orders:
        print(order)

    # Extracting orders by priority
    print("\nExtracting Orders by Highest Priority:")
    while not order_heap.is_empty():
        highest_priority_order = order_heap.extract_highest_priority()
        print(f"Extracted: {highest_priority_order}")

if __name__ == "__main__":
    main()
