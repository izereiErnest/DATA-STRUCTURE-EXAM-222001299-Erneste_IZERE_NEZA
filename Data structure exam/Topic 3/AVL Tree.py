class Order:
    def __init__(self, order_id: int, customer_name: str, service_type: str, priority: int):
        self.order_id = order_id
        self.customer_name = customer_name
        self.service_type = service_type
        self.priority = priority

class AVLNode:
    def __init__(self, order: Order):
        self.order = order
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, root, order):
        # Standard BST insert
        if not root:
            return AVLNode(order)

        if order.order_id < root.order.order_id:
            root.left = self.insert(root.left, order)
        elif order.order_id > root.order.order_id:
            root.right = self.insert(root.right, order)
        else:
            return root  # Duplicate order_ids not allowed

        # Update height of ancestor node
        self.update_height(root)

        # Get balance factor
        balance = self.balance_factor(root)

        # Left Left Case
        if balance > 1 and order.order_id < root.left.order.order_id:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and order.order_id > root.right.order.order_id:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and order.order_id > root.left.order.order_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and order.order_id < root.right.order.order_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def insert_order(self, order):
        self.root = self.insert(self.root, order)

    def search(self, root, order_id):
        if not root or root.order.order_id == order_id:
            return root

        if order_id < root.order.order_id:
            return self.search(root.left, order_id)
        return self.search(root.right, order_id)

    def find_order(self, order_id):
        return self.search(self.root, order_id)

# Example usage
def main():
    avl_tree = AVLTree()
    
    # Insert some orders
    orders = [
        Order(1, "Izere Ernest", "Premium Wash", 1),
        Order(2, "Sam Kalungi", "Basic Wash", 2),
        Order(3, "Boby Wayne", "Deluxe Wash", 3)
    ]
    
    for order in orders:
        avl_tree.insert_order(order)
    
    # Search for an order
    found_order = avl_tree.find_order(2)
    if found_order:
        print(f"Found order: {found_order.order.customer_name}")

if __name__ == "__main__":
    main()