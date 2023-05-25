class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

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

def main():
    while True:
        elements = input("\nMasukkan kombinasi angka dan huruf (pisahkan dengan spasi), atau ketik 'exit' untuk keluar: ")
        
        if elements.lower() == "exit":
            break
        
        elements = elements.split()
        tree = None

        for element in elements:
            tree = insert(tree, element)

        print("Pre-order traversal:")
        preorder_traversal(tree)

        print("\nIn-order traversal:")
        inorder_traversal(tree)

        print("\nTraversal Post-Order:")
        postorder_traversal(tree)

if __name__ == '__main__':
    main()
