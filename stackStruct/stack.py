class Node:

    def __init__(self, value):
        self.val = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    # O(1) - constant time
    def __len__(self):
        return self.size
    
    # O(n) - linear time
    def __repr__(self):
        if self.is_empty():
            return "[]"
        string = f"[{self.top.val}"
        node = self.top.next
        while node is not None:
            string += f", {node.val}"
            node = node.next
        

        return string + "]"


    # O(1) - constant time
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1

    # O(1) - constant time
    def pop(self):
        if not self.is_empty():
            node = self.top         
            self.top = self.top.next
            self.size -= 1
            return node.val
        
        raise ValueError("Stack is empty")

    # O(1) - constant time
    def peek(self):
        if not self.is_empty():
            return self.top.val
        
        raise ValueError("Stack is empty")
    
    # O(1) - constant time
    def is_empty(self):
        return self.size == 0


if __name__ == "__main__":
    s = Stack()

    print("Initial stack:", s)
    print("Is empty?", s.is_empty())
    print("Length:", len(s))
    print("-" * 30)

    # Test pushing elements
    s.push(10)
    s.push(20)
    s.push(30)
    print("After pushing 10, 20, 30:", s)
    print("Top element (peek):", s.peek())
    print("Length:", len(s))
    print("-" * 30)

    # Test popping elements
    print("Pop:", s.pop())
    print("After pop:", s)
    print("Top element (peek):", s.peek())
    print("Length:", len(s))
    print("-" * 30)

    # Pop all elements
    print("Pop:", s.pop())
    print("Pop:", s.pop())
    print("After popping all:", s)
    print("Is empty?", s.is_empty())
    print("Length:", len(s))
    print("-" * 30)

    # Test popping from empty stack
    try:
        s.pop()
    except ValueError as e:
        print("Caught error on empty pop:", e)

    # Test peek from empty stack
    try:
        s.peek()
    except ValueError as e:
        print("Caught error on empty peek:", e)
