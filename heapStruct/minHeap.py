import heapq

# Heap tree is always balanced ie: O(h) = O(log n)
class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

    # O(log n)
    def insert(self, key, value):
        self.heap.append((key, value))

        self._sift_up(len(self.heap) - 1)

    # O(1)
    def peek_min(self):
        if not self.heap:
            raise IndexError("Empty heap")
        
        return self.heap[0]

    # O(log n)
    def extract_min(self):
        if not self.heap:
            raise IndexError("Empty heap")
        
        min_element = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)

        return min_element

    #  O(n)
    def heapify(self, elements):
        self.heap = list(elements)

        for i in reversed(range(self._parent(len(self.heap) - 1) + 1)):
            self._sift_down(i)

    #  O(n)
    def meld(self, other_heap):
        combined_heap = self.heap + other_heap.heap

        self.heapify(combined_heap)

        other_heap.heap = []

    # O(1)
    def _parent(self, index):
        if index == 0:
            return None
        
        return (index - 1) // 2

    # O(1)
    def _left(self, index):
        left = 2 * index + 1

        if left < len(self.heap):
            return left
        
        return None

    # O(1)
    def _right(self, index):
        right = 2 * index + 2

        if right < len(self.heap):
            return right
        
        return None

    # O(log n)
    def _sift_up(self, index):
        # swim
        parent_index = self._parent(index)

        while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

            index = parent_index
            parent_index = self._parent(index)

    # O(log n)
    def _sift_down(self, index):
        # sink
        while True:
            smallest = index

            left = self._left(index)
            right = self._right(index)

            if left is not None and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right is not None and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            
            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest



if __name__ == "__main__":
    print("=== INSERT / PEEK TEST ===")
    h = MinHeap()
    data = [(5, "a"), (3, "b"), (8, "c"), (1, "d"), (6, "e"), (2, "f")]

    for k, v in data:
        h.insert(k, v)

    print("Heap:", h)
    print("Min:", h.peek_min())
    assert h.peek_min()[0] == 1
    print("Insert + peek_min OK\n")

    print("=== EXTRACT MIN TEST ===")
    extracted = []
    while len(h) > 0:
        extracted.append(h.extract_min()[0])

    print("Extracted:", extracted)
    assert extracted == sorted(extracted)
    print("extract_min OK\n")

    print("=== HEAPIFY TEST ===")
    h2 = MinHeap()
    h2.heapify(data)

    print("Heap after heapify:", h2)
    assert h2.peek_min()[0] == 1
    print("heapify OK\n")

    print("=== MELD TEST ===")
    h3 = MinHeap()
    h3.heapify([(7, "x"), (9, "y"), (4, "z")])

    h2.meld(h3)

    print("Heap after meld:", h2)
    assert len(h3) == 0

    extracted_after_meld = []
    while len(h2) > 0:
        extracted_after_meld.append(h2.extract_min()[0])

    assert extracted_after_meld == sorted(extracted_after_meld)
    print("meld OK\n")

    print("=== EDGE CASES ===")
    empty = MinHeap()

    try:
        empty.peek_min()
        assert False
    except IndexError:
        print("peek_min on empty OK")

    try:
        empty.extract_min()
        assert False
    except IndexError:
        print("extract_min on empty OK")

    print()

    print("=== COMPARE WITH heapq ===")
    my_heap = MinHeap()
    py_heap = []

    for item in data:
        my_heap.insert(*item)
        heapq.heappush(py_heap, item)

    my_out = []
    py_out = []

    while py_heap:
        py_out.append(heapq.heappop(py_heap))
        my_out.append(my_heap.extract_min())

    print("My heap:", my_out)
    print("heapq:  ", py_out)

    assert my_out == py_out
    print("Matches heapq behavior\n")

    print("ALL TESTS PASSED")