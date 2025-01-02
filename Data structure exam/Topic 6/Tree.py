from typing import List, Optional

class ServiceNode:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.children: List[ServiceNode] = []
        self.parent: Optional[ServiceNode] = None
        self.orders: List[dict] = []  # Store orders at this service level

class ServiceHierarchyTree:
    def __init__(self):
        # Create root node for all services
        self.root = ServiceNode("Car Wash Services", "All available services")
        self.setup_initial_structure()

    def setup_initial_structure(self):
        # Level 1: Main service categories
        exterior = self.add_service(self.root, "Exterior Services", "All exterior cleaning services")
        interior = self.add_service(self.root, "Interior Services", "All interior cleaning services")
        premium = self.add_service(self.root, "Premium Packages", "Combined service packages")

        # Level 2: Specific services under each category
        # Exterior services
        self.add_service(exterior, "Basic Wash", "Simple exterior wash")
        self.add_service(exterior, "Deluxe Wash", "Advanced exterior wash with wax")
        self.add_service(exterior, "Premium Wash", "Complete exterior treatment")

        # Interior services
        self.add_service(interior, "Vacuum", "Basic interior vacuum")
        self.add_service(interior, "Deep Clean", "Detailed interior cleaning")
        self.add_service(interior, "Sanitization", "Complete interior sanitization")

        # Premium packages
        self.add_service(premium, "Full Service", "Complete interior and exterior service")
        self.add_service(premium, "VIP Package", "Premium detailing package")

    def add_service(self, parent: ServiceNode, name: str, description: str = "") -> ServiceNode:
        new_service = ServiceNode(name, description)
        new_service.parent = parent
        parent.children.append(new_service)
        return new_service

    def add_order(self, service_path: List[str], order: dict) -> bool:
        """Add an order to a specific service node"""
        node = self.find_service(service_path)
        if node:
            node.orders.append(order)
            return True
        return False

    def find_service(self, path: List[str]) -> Optional[ServiceNode]:
        """Find a service node by following a path from root"""
        current = self.root
        for service_name in path:
            found = False
            for child in current.children:
                if child.name == service_name:
                    current = child
                    found = True
                    break
            if not found:
                return None
        return current

    def get_service_orders(self, path: List[str]) -> List[dict]:
        """Get all orders for a specific service"""
        node = self.find_service(path)
        return node.orders if node else []

    def print_structure(self, node: Optional[ServiceNode] = None, level: int = 0):
        """Print the entire service hierarchy"""
        if node is None:
            node = self.root
        
        print("  " * level + f"- {node.name}")
        for child in node.children:
            self.print_structure(child, level + 1)

# Example usage
def main():
    # Create service hierarchy
    service_tree = ServiceHierarchyTree()
    
    # Add some orders
    order1 = {
        "order_id": 1,
        "customer_name": "IZERE Ernest ",
        "timestamp": "2025-01-02 10:00",
        "status": "pending"
    }
    
    # Add order to Basic Wash service
    service_tree.add_order(["Exterior Services", "Basic Wash"], order1)
    
    # Print structure
    print("Service Hierarchy:")
    service_tree.print_structure()
    
    # Get orders for a specific service
    basic_wash_orders = service_tree.get_service_orders(["Exterior Services", "Basic Wash"])
    print(f"\nBasic Wash Orders: {len(basic_wash_orders)}")

if __name__ == "__main__":
    main()