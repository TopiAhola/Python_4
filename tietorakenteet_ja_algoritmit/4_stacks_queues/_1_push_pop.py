class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add an element to the stack

        Parameters:
        - 'data': Data/value being added

        Returns: None
        """
        self._top = Node(data, self._top)
        self._size += 1

    def pop(self):
        """
        Remove the top node from the stack and return its content

        Parameters: None

        Returns: The content of the node or None if stack is empty
        """
        if self._top:
            returnData = self._top.data
            self._top = self._top.next
            self._size -= 1
            return returnData

        else:
            self._size = 0
            return None

    def __repr__(self):
        current_node = self._top
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Stack ({self._size} element{plural}): [{values.lstrip(", ")}]>'



#main
if __name__ == '__main__':
    mystack = Stack()
    mystack.push('A')
    mystack.push('B')
    mystack.push('C')
    print(mystack)



    mystack = Stack()
    for c in 'ABC':
        mystack.push(c)
        print(mystack)
    val = mystack.pop()
    print(val, mystack)