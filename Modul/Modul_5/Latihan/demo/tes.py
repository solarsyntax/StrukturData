class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data <= root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def preorder_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" ")

def build_tree_from_input():
    elements = input("Masukkan elemen-elemen (dipisahkan dengan spasi): ").split()
    tree = None

    for element in elements:
        tree = insert(tree, element)

    return tree

def main():
    tree = build_tree_from_input()

    print("Pre-order traversal:")
    preorder_traversal(tree)
    print("\n")

    print("In-order traversal:")
    inorder_traversal(tree)
    print("\n")

    print("Post-order traversal:")
    postorder_traversal(tree)
    print("\n")

if __name__ == '__main__':
    main()
