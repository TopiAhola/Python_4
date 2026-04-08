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
        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            # if list is not empty, update the last element and point it to the new node
            self._tail.next = new_node
            self._tail = new_node

        # Update list's size
        self._size += 1


    def pop(self):

        # if list is empty
        if not self._tail:
            return None

        #if list length is 1
        if self._size == 1:
            returnData = self._tail.data
            del self._tail
            self._head = None
            self._tail = None
            self._size -= 1
            return returnData


        #if list length is > 1
        else:
            #start from head, iterate until .next is None
            current_node = self._head
            previous_node = None
            while current_node.next:
                previous_node = current_node
                current_node = current_node.next

            #assert the end of list
            assert current_node == self._tail

            #previous node set pointer to None, set tail to previous
            previous_node.next = None
            self._tail = previous_node

            #get data, delete current node
            returnData = current_node.data
            del current_node
            self._size -= 1
            return returnData


#main
list = SinglyLinkedList()
for i in 'abc':
    list.append(i)
val = list.pop()

print(val, list)