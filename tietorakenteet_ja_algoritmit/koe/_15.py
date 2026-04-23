class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._previous = None

    def next(self):
        return self._next

    def previous(self):
        return self._previous

    def link_next(self, node):
        self._next = node

    def link_previous(self, node):
        self._previous = node

    def value(self):
        return self._data


class Sorted_Doubly_Linked_List:
    def __init__(self):
        self._head_node = None

    def print_list(self):
        current = self._head_node
        print('[', end='')
        while current is not None:
            print(current.value(), end='')
            current = current.next()
            if current is not None:
                print(', ', end='')
        print(']')

    def append(self, data):
        if not self._head_node:
            self._head_node = Node(data)
            return

        current_node = self._head_node
        prev_node = None
        while current_node:
            if current_node.value() < data:
                prev_node = current_node
                current_node = current_node.next()
            else:
                break

        new_node = Node(data)
        new_node.link_previous(prev_node)
        new_node.link_next(current_node)

        if current_node:
            current_node.link_previous(new_node)

        if current_node is self._head_node:
            self._head_node = new_node

        if prev_node:
            prev_node.link_next(new_node)

    # Respect the indentation, so the method can be added to the class
    # Respect the indentation, so the method can be added to the class
    def merge(self, other):

        # starting point
        self_pointer = self._head_node
        other_pointer = other._head_node

        current_node = None
        if self_pointer and other_pointer:
            if self_pointer.value() <= other_pointer.value():
                current_node = self_pointer
                self_pointer = self_pointer.next()

            else:
                current_node = other_pointer
                other_pointer = other_pointer.next()

        elif self_pointer:
            current_node = self_pointer
            self_pointer = self_pointer.next()

        elif other_pointer:
            current_node = other_pointer
            other_pointer = other_pointer.next()

        self._head_node = current_node

        while self_pointer and other_pointer:
            if self_pointer.value() <= other_pointer.value():
                current_node.link_next(self_pointer)
                self_pointer.link_previous(current_node)
                current_node = self_pointer
                self_pointer = self_pointer.next()

            else:
                current_node.link_next(other_pointer)
                other_pointer.link_previous(current_node)
                current_node = other_pointer
                other_pointer = other_pointer.next()

        while self_pointer:
            current_node.link_next(self_pointer)
            self_pointer.link_previous(current_node)
            current_node = self_pointer
            self_pointer = self_pointer.next()

        while other_pointer:
            current_node.link_next(other_pointer)
            other_pointer.link_previous(current_node)
            current_node = other_pointer
            other_pointer = other_pointer.next()

        ##make bowh objects the same
        other._head_node = self._head_node

#main
l1 = Sorted_Doubly_Linked_List()
l1.append(9)
l1.append(5)
l1.append(7)
l1.append(1)
l1.append(3)
l2 = Sorted_Doubly_Linked_List()
l2.append(2)
l2.append(8)
l2.append(0)
l2.append(6)
l2.append(4)
l1.merge(l2)
l1.print_list()
l2.print_list()