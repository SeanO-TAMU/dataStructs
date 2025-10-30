class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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
        
        return False
    
    # O(n) - linear time
    def __len__(self):
        length = 0

        node = self.head
        while node != None:
            node = node.next
            length += 1
        
        return length

    # O(n) - linear time
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next != None:
                node = node.next
        
            node.next = Node(value)

    # O(1) - constant time
    def prepend(self, value):
        node = self.head
        self.head = Node(value)
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

                next = node.next
                node.next = Node(value)
                node.next.next = next

    # O(n) - linear time
    def delete(self, value):
        node = self.head
        if node != None:
            if node.value == value:
                self.head = node.next
            while node.next != None:
                if node.next.value == value:
                    node.next = node.next.next
                    break
                node = node.next
        
    # O(n) - linear time
    def pop(self, index):
        if self.head == None:
            raise ValueError("Index out of bounds")
        else:
            node = self.head
            for i in range(index - 1):
                if node.next == None:
                    raise ValueError("Index out of bounds")
                node = node.next

            if node.next == None:
                raise ValueError("Index out of bounds")
            else:
                node.next = node.next.next
            
    # O(n) - linear time
    def get(self, index):
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
    
    ll = LinkedList()

    ll.append(10)
    ll.append(5)
    ll.append(18)
    ll.append(22)
    ll.append(29)

    ll.prepend(100)

    ll.insert(200, 1)

    ll.delete(5)

    ll.pop(5)

    print(ll)

    print(ll.get(2))
