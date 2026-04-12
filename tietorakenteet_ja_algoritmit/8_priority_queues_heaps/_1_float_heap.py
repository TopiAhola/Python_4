class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """
        target_index = (self._size - 1)
        target = self._heap[target_index]
        parent_index = (target_index - 1) // 2

        while parent_index >= 0 and self._heap[parent_index] > target:
            #swap
            self._heap[target_index] = self._heap[parent_index]
            self._heap[parent_index] = target

            #indexes for next level
            target_index = parent_index
            parent_index = (target_index - 1) // 2
        return




#main
if __name__ == '__main__':
    h = Heap()
    h._heap = [3, 6, 5, 9, 7, 8, 2]
    h._size = 7
    h._float()
    print(h._heap)
    print('''[2, 6, 3, 9, 7, 8, 5]''')

    h = Heap()
    h._heap = [3, 6, 5, 9, 7, 8, 4]
    h._size = 7
    h._float()
    print(h._heap)
    print('''[3, 6, 4, 9, 7, 8, 5]''')