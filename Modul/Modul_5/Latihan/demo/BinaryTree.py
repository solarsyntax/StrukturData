class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def insert_node(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert_node(root.left, data)
        else:
            root.right = insert_node(root.right, data)
    return root


def build_tree():
    root = None
    nodes = input("Masukkan kombinasi angka dan huruf (pisahkan dengan spasi): ").split()
    for node in nodes:
        root = insert_node(root, node)
    return root


def print_preorder(root):
    if root:
        print(root.data, end=" ")
        print_preorder(root.left)
        print_preorder(root.right)


def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.data, end=" ")
        print_inorder(root.right)


def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.data, end=" ")


# Main program
tree_root = build_tree()

print("\nTraversal Preorder:")
print_preorder(tree_root)

print("\nTraversal Inorder:")
print_inorder(tree_root)

print("\nTraversal Postorder:")
print_postorder(tree_root)
