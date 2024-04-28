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

    def find_maximum(self):
        if self.root is None:
            return None

        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        return current_node

    def find_minimum(self):
        if self.root is None:
            return None

        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node


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

# Find maximum value
maximum_node = bst.find_maximum()
if maximum_node:
    print(f"Maximum node: {maximum_node}")
else:
    print("Tree is empty")

# Find minimum value
minimum_node = bst.find_minimum()
if minimum_node:
    print(f"Minimum node: {minimum_node}")
else:
    print("Tree is empty")
