class Node:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(n) - linear time
    def __repr__(self):
        if self.head == None:
            return "[]"
        else:
            node = self.head
            return_string = f"[{node.value}"
            
            while node.next != None:
                node = node.next
                return_string += f", {node.value}"
            
            return_string += "]"

            return return_string

    # O(n) - linear time
    def __contains__(self, val):
        
        node = self.head
        while node != None:
            if node.value == val:
                return True

            node = node.next
        
        return False
    
    # O(n) - linear time
    def __len__(self):
        length = 0

        node = self.head
        while node != None:
            node = node.next
            length += 1
        
        return length

    # O(1) - constant time
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            node = self.tail
            node.next = newNode
            newNode.prev = node
            self.tail = newNode

    # O(1) - constant time
    def prepend(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            node = self.head
            self.head = Node(value)
            node.prev = self.head
            self.head.next = node


    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head == None:
                raise ValueError("Index out of bounds")
            else:
                node = self.head
                for i in range(index - 1):
                    if node.next == None:
                        raise ValueError("Index out of bounds")
                    node = node.next

                newNode = Node(value)
                newNode.next = node.next
                newNode.prev = node
                if node.next != None:
                    node.next.prev = newNode
                else:
                    self.tail = newNode
                node.next = newNode
                

    # O(n) - linear time
    def delete(self, value):
        node = self.head
        if node != None:
            if node.value == value:
                self.head = node.next
                if self.head != None:
                    self.head.prev = None
                else:
                    self.tail = None
                return
            while node.next != None:
                if node.next.value == value:
                    if node.next.next != None:
                        node.next.next.prev = node
                    else:
                        self.tail = node
                    node.next = node.next.next
                    break
                node = node.next
        
    # O(n) - linear time
    def pop(self, index):
        if self.head == None:
            raise ValueError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
        else:
            node = self.head
            for i in range(index - 1):
                if node.next == None:
                    raise ValueError("Index out of bounds")
                node = node.next

            if node.next == None:
                raise ValueError("Index out of bounds")
            else:
                if node.next.next != None:
                    node.next.next.prev = node
                if node.next.next == None:
                    self.tail = node
                node.next = node.next.next
            
    # O(n) - linear time
    def get(self, index):
        if index < 0:
            raise ValueError("Negative index not allowed")
        if self.head == None:
            raise ValueError("Index out of bounds")
        else:
            node = self.head
            for i in range(index):
                if node.next == None:
                    raise ValueError("Index out of bounds")
                node = node.next
            
            return node.value

if __name__ == "__main__":
    
    ll = DoubleLinkedList()

    print("=== INITIAL STATE ===")
    print(ll)  # []
    print("Length:", len(ll))

    # --- Append test ---
    print("\n=== APPEND TEST ===")
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("List after appending 10, 20, 30:", ll)
    print("Head:", ll.head.value, "Tail:", ll.tail.value)

    # --- Prepend test ---
    print("\n=== PREPEND TEST ===")
    ll.prepend(5)
    print("List after prepending 5:", ll)
    print("Head:", ll.head.value, "Tail:", ll.tail.value)

    # --- Insert tests ---
    print("\n=== INSERT TESTS ===")
    ll.insert(15, 2)
    print("Inserted 15 at index 2:", ll)
    ll.insert(35, len(ll))  # insert at end (tail)
    print("Inserted 35 at tail:", ll)
    ll.insert(1, 0)  # insert at head
    print("Inserted 1 at head:", ll)

    # --- Contains test ---
    print("\n=== CONTAINS TEST ===")
    print("Does list contain 20?", 20 in ll)
    print("Does list contain 99?", 99 in ll)

    # --- Get test ---
    print("\n=== GET TEST ===")
    for i in range(len(ll)):
        print(f"Value at index {i}:", ll.get(i))

    # --- Delete tests ---
    print("\n=== DELETE TESTS ===")
    ll.delete(1)
    print("Deleted value 1 (head):", ll)
    ll.delete(35)
    print("Deleted value 35 (tail):", ll)
    ll.delete(15)
    print("Deleted value 15 (middle):", ll)

    # --- Pop tests ---
    print("\n=== POP TESTS ===")
    print("Before pop:", ll)
    ll.pop(0)
    print("After popping head:", ll)
    ll.pop(len(ll) - 1)
    print("After popping tail:", ll)
    if len(ll) > 1:
        ll.pop(1)
        print("After popping index 1 (middle):", ll)

    # --- Length and tail/head check ---
    print("\n=== LENGTH & STRUCTURE CHECK ===")
    print("Final list:", ll)
    print("Length:", len(ll))
    print("Head:", ll.head.value if ll.head else None)
    print("Tail:", ll.tail.value if ll.tail else None)

    # --- Edge case: empty pop/delete ---
    print("\n=== EDGE CASE TESTS ===")
    ll2 = DoubleLinkedList()
    try:
        ll2.pop(0)
    except ValueError as e:
        print("Pop on empty list:", e)

    ll2.append(42)
    ll2.pop(0)
    print("After popping only element:", ll2)
    print("Head:", ll2.head, "Tail:", ll2.tail)