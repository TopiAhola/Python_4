class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Queue ({self._size} element{plural}): [{values.lstrip(", ")}]>'


    def enqueue(self, data):
        # Prepare some variables to make the necessary changes
        # The new node will be inserted between previous_node and next_node
        previous_node = None
        next_node = self._head
        # Move to the given index and update pointer variables
        for _ in range(0):
            previous_node = next_node
            next_node = next_node.next

        # Create new node with right value and pointers
        new_node = ListNode(data, prev=previous_node, next=next_node)

        # If insert at front, update head
        if previous_node is None:
            self._head = new_node
        else:
            # If not, update previous node
            previous_node.next = new_node

        # If insert at the end, update tail
        if next_node is None:
            self._tail = new_node
        else:
            # If not, update next node
            next_node.prev = new_node

        # Update list size
        self._size += 1

    def dequeue(self):
        # If list is empty, returns None
        if not self._size:
            return None

        # Locate previous_node (the node just before last node)
        node_to_remove = self._tail
        previous_node = node_to_remove.prev

        # If node to remove is first node, then update head pointer
        if node_to_remove == self._head:
            self._head = None
        else:
            # If not, update the pointer of the previous node
            previous_node.next = None   # It is now the last node

        # Update tail pointer
        self._tail = previous_node

        # Update size, remove node and return its content
        self._size -= 1
        value = node_to_remove.data
        del(node_to_remove)
        return value




'''
 <Queue (3 elements): [C, B, A]>
 '''

#main
queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
print(queue)


queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
val = queue.dequeue()
print(val, queue)