class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Node({self.value})'


class BST:
    def __init__(self):
        self.root = None

    def _find(self, value):
        # Helper function for recursive search
        def _find_recursive(node, value):
            if node is None or node.value == value:
                return node
            elif value < node.value:
                return _find_recursive(node.left, value)
            else:
                return _find_recursive(node.right, value)

        # Start the search from the root
        return _find_recursive(self.root, value)


# Example usage:
# Create a BST
bst = BST()
# Insert some nodes
bst.root = Node(10)
bst.root.left = Node(5)
bst.root.right = Node(15)
bst.root.left.left = Node(3)
bst.root.left.right = Node(7)
bst.root.right.left = Node(12)
bst.root.right.right = Node(17)

# Search for a value
search_value = 7
found_node = bst._find(search_value)
if found_node:
    print(f"Found node with value {search_value}: {found_node}")
else:
    print(f"Node with value {search_value} not found")

