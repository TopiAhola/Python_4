class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        # Start at the end of the heap
        index = self._size - 1
        # Calculate index of parent element
        parent_index = (index-1) // 2
        # While not at Root node and value less than its parent
        while index > 0 and self._heap[index] < self._heap[parent_index]:
            # swap value with its parent
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            # Update indices
            index = parent_index
            parent_index = (index-1) // 2

    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()

    def _sink(self):
        """
        Sinks the root node of the heap until the heap is in order
        """
        #these are unnecessary
        target_index = 0
        child1_index = 2 * target_index + 1
        child2_index = 2 * target_index + 2

        #value of root
        target = self._heap[target_index]

        #initialize this
        child_index = target_index

        while target_index < self._size:
            #see if both children exist
            if child1_index < self._size and child2_index < self._size:
                #see which to swap with
                if self._heap[child1_index] <= self._heap[child2_index]:
                    child_index = child1_index
                else:
                    child_index = child2_index
            #if child 1
            elif child1_index < self._size:
                child_index = child1_index

            #if child 2
            elif child2_index < self._size:
                child_index = child2_index

            #neither
            else:
                break

            #swap if smaller child value < target value, else stop
            if self._heap[child_index] < target:
                # swap
                print("swap:", self._heap[target_index], self._heap[child_index])
                self._heap[target_index] = self._heap[child_index]
                self._heap[child_index] = target

                # indexes for next level
                target_index = child_index
                child1_index = 2 * target_index + 1
                child2_index = 2 * target_index + 2
                print("next indexes:", child1_index, child2_index)
            else:
                break
        return


#main
if __name__ == '__main__':
    h = Heap()
    h._heap = [8, 6, 5, 9, 7]
    h._size = 5
    h._sink()
    print(h._heap)

    h = Heap()
    h._heap = [25, 10, 20, 30, 40, 50, 60]
    h._size = 7
    h._sink()
    print('''[10, 25, 20, 30, 40, 50, 60]''')
    print(h._heap)