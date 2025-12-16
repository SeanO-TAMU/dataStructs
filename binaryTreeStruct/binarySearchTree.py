class Node:

    def __init__ (self, key, value=None):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = value

    def __repr__(self):
        return f"({self.key}, {self.value})"

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __contains__(self, key):
        node = self.root

        while node != None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return True
            
        return False

    # O(n)
    def __iter__(self): # this will allow you to do for i in tree
        yield from self._in_order_traversal(self.root)

    # O(n)
    def __repr__(self):
        return str(list(self._in_order_traversal(self.root)))

    # O(n) worst case O(log n) average case, O(h) always (h = height)
    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            node = self.root
            while node:
                if node.key < key:
                    if node.right is None:
                        node.right = Node(key, value)
                        node.right.parent = node
                        return
                    else:
                        node = node.right
                elif node.key > key:
                    if node.left is None:
                        node.left = Node(key, value)
                        node.left.parent = node
                        return
                    else:
                        node = node.left
                else:
                    node.val = value
                    return
                
    # O(n) worst case O(log n) average case, O(h) always (h = height)
    def search(self, key):
        node = self.root

        while node:
            if node.key < key:
                node = node.right
            elif node.key > key:
                node = node.left
            else:
                return node
        
        return None

    # O(n) worst case O(log n) average case, O(h) always (h = height)
    def delete(self, key):
        node = self.search(key)

        if node is None:
            raise KeyError("Node with this key does not exist")
        
        self._delete(node)

    # O(n)
    def traverse(self, order):
        if order == 'inorder':
            yield from self._in_order_traversal(self.root)
        elif order == 'preorder':
            yield from self._pre_order_traversal(self.root)
        elif order == 'postorder':
            yield from self._post_order_traversal(self.root)
        else:
            raise ValueError("Unkown order")

    def _delete(self, node):

        # Node is leaf node
        if node.left is None and node.right is None:
            if node.parent is None: 
                self.root = None
            else:
                if node.parent.left == node:
                    node.parent.left = None
                elif node.parent.right == node:
                    node.parent.right = None
                
                node.parent = None

        # Node has one child node
        elif node.left is None or node.right is None:
            child_node = None
            if node.left is not None:
                child_node = node.left
            else:
                child_node = node.right

            if node.parent is None:
                child_node.parent = None
                self.root = child_node
            else:
                if node.parent.left == node:
                    node.parent.left = child_node
                elif node.parent.right == node:
                    node.parent.right = child_node
            
                child_node.parent = node.parent

            node.parent = node.left = node.right = None
        
        # Node has two child nodes
        else:
            successor = self._successor(node)
        
            node.key = successor.key
            node.value = successor.value
            
            self._delete(successor)

    def _successor(self, node):
        # smallest node that is larger than current node
        if node is None:
            raise ValueError("Cannot find successor of None")
        
        if node.right is None:
            return None
        else:
            current_node = node.right

            while current_node.left != None:
                current_node = current_node.left
            
            return current_node


    def _predecessor(self, node):
        # largest node that is smaller than current node
        if node is None:
            raise ValueError("Cannot find successor of None")
        
        if node.left is None:
            return None
        else:
            current_node = node.left

            while current_node.right != None:
                current_node = current_node.right
            
            return current_node

    def _in_order_traversal(self, node):
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield (node.key, node.value)
            yield from self._in_order_traversal(node.right)

    def _pre_order_traversal(self, node):
        if node is not None:
            yield (node.key, node.value)
            yield from self._pre_order_traversal(node.left)
            yield from self._pre_order_traversal(node.right)


    def _post_order_traversal(self, node):
        if node is not None:
            yield from self._post_order_traversal(node.left)
            yield from self._post_order_traversal(node.right)
            yield (node.key, node.value)


if __name__ == "__main__":
    
    bst = BinarySearchTree()

    # Insert values
    data = [
        (4, "root"),
        (2, "left"),
        (6, "right"),
        (1, "left.left"),
        (3, "left.right"),
        (5, "right.left"),
        (7, "right.right"),
    ]

    for k, v in data:
        bst.insert(k, v)

    print("Tree (in-order via __repr__):")
    print(bst)
    print()

    # Test membership
    print("Contains 3?", 3 in bst)
    print("Contains 10?", 10 in bst)
    print()

    # Test search
    print("Search key 6:", bst.search(6))
    print("Search key 99:", bst.search(99))
    print()

    # Test traversals
    print("In-order traversal:")
    print(list(bst.traverse("inorder")))

    print("Pre-order traversal:")
    print(list(bst.traverse("preorder")))

    print("Post-order traversal:")
    print(list(bst.traverse("postorder")))
    print()

    # Test iteration (__iter__)
    print("Iterating directly over tree:")
    for node in bst:
        print(node)
    print()

    # Delete leaf node
    print("Deleting leaf node (1)")
    bst.delete(1)
    print(list(bst))
    print()

    # Delete node with one child
    print("Deleting node with one child (6)")
    bst.delete(6)
    print(list(bst))
    print()

    # Delete node with two children
    print("Deleting node with two children (2)")
    bst.delete(2)
    print(list(bst))
    print()

    print("Final tree:")
    print(bst)