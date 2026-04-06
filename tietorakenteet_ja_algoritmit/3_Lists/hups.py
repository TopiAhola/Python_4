class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        new_node = ListNode(value)

        # If list is empty just point the header to the new node
        if self._head is None:
            self._head = self._tail = new_node
        else:
            # if list is not empty, update the last element and point it to the new node
            self._tail.next = new_node
            self._tail = new_node

        # Update list's size
        self._size += 1

    def pop(self):
        """
        Removes the last node of the list

        Parameters: None

        Returns:
            The content of the removed node. If list is empty, returns None
        """
        # If list is empty return None
        if not self._size:
            return None

        # Locate previous_node (the node just before last node)
        if self._size == 1:
            previous_node = None
        else:
            previous_node = self._head
            for _ in range(self._size-1):
                previous_node = previous_node.next

        # If head is also last node, then update head
        if self._head == self._tail:
            self._head = None

        # Save the content of the last node and remove it
        value = self._tail.data
        del(self._tail)

        # Update tail
        self._tail = previous_node

        # Finally update size and return the value of the removed node
        self._size -= 1
        return value

    def insert(self, index, value):
        """
        Insert a new node with value in the position given by the index

        Parameters:
        - 'index': The position where to insert the new node
        - 'value': The value of the new node

        Returns: None
        """
        # Check if index is inside bounds
        if index < 0 or index > self._size:
            raise(ValueError('Index out of bounds'))

        # Prepare some variables to make the necessary changes
        # The new node will be inserted between previous_node and next_node
        previous_node = None
        next_node = self._head
        # Move to the given index and update pointer variables
        for _ in range(index):
            previous_node = next_node
            next_node = next_node.next

        # Create new node. It's next pointer points to next node or None
        new_node = ListNode(value, next_node)

        # If insert at front, update head
        if previous_node is None:
            self._head = new_node
        else:
            # If not, update previous node
            previous_node.next = new_node

        # If insert at the end, update tail
        if previous_node == self._tail:
            self._tail = new_node

        # Update list size
        self._size += 1

    def remove(self, index):

        if index < 0 or index > self._size:
            raise(ValueError('Index out of bounds'))

        #if remove head
        if index == 0:
            returnData = self._head.data
            next_node = self._head.next
            del self._head
            self._size -= 1

            if next_node is not None:
                next_node.prev = None
                self._head = next_node

            return returnData

        #if remove tail
        if index == self._size -1:
            returnData = self._tail.data
            del self._tail
            self._size -= 1
            return returnData

        #else
        else:
            #start from head, iterate until index found
            previous_node = None
            current_node = self._head
            next_node = self._head.next
            searchIndex = 0

            while searchIndex < index:
                index += 1
                previous_node = current_node
                current_node = current_node.next
                next_node = current_node.next

            #assert all nodes exist
            assert searchIndex == index
            assert current_node is not None and previous_node is not None and next_node is not None

            #set pointer between prev and next nodes
            previous_node.next = next_node
            next_node.prev = previous_node

            #get data, delete current node
            returnData = current_node.data
            del current_node
            self._size -= 1
            return returnData

        return