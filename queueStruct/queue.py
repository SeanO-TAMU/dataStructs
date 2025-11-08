class Node:

    def __init__(self, value):
        self.val = value
        self.next = None

class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        items = []
        node = self.head
        while node != None:
            items.append(str(node.val))
            node = node.next

        return "Queue([" + ", ".join(items) + "])"

    def enqueue(self, value):
        node = Node(value)
        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.size += 1

    def dequeue(self):
        if self.is_empty():
             raise ValueError("Queue is empty")
        
        value = self.head.val
        self.size -= 1

        if self.size == 0:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return value


    def peak(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        
        return self.head.val

    def is_empty(self):
        return self.size == 0



if __name__ == "__main__":
    q = Queue()

    print("Initial queue:", q)
    print("Is empty?", q.is_empty())
    print("Length:", len(q))
    print("-" * 30)

    # Enqueue elements
    print("Enqueueing elements 10, 20, 30...")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Queue after enqueues:", q)
    print("Length:", len(q))
    print("Peek:", q.peak())
    print("Is empty?", q.is_empty())
    print("-" * 30)

    # Dequeue elements
    print("Dequeued:", q.dequeue())
    print("Queue now:", q)

    print("Dequeued:", q.dequeue())
    print("Queue now:", q)

    print("Dequeued:", q.dequeue())
    print("Queue now:", q)
    print("Is empty?", q.is_empty())
    print("-" * 30)

    # Edge case: dequeue from empty queue
    try:
        print("Trying to dequeue from empty queue...")
        q.dequeue()
    except ValueError as e:
        print("Caught expected error:", e)

    # Edge case: peek on empty queue
    try:
        print("Trying to peek on empty queue...")
        q.peak()
    except ValueError as e:
        print("Caught expected error:", e)