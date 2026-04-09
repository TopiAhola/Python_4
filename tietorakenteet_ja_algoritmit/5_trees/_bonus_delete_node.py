class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'

class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        """
        Inserts a new value in the BST

        Parameters:
        - 'data': Value or data to insert

        Returns: None
        """
        # Let's use a couple of pointers to traverse the tree
        # following BST rules and find the parent of the node
        # to be inserted
        current_node = self._root_node
        parent_node = None
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        # After the loop, parent_node variable is parent node or None if Tree is empty
        new_node = Node(data, parent_node=parent_node)
        if parent_node is None:
            if self._root_node is None:
                # If tree is empty, just make the new node the root node
                self._root_node = new_node
            else:
                # If tree is not empty and parent_node is None,
                # probably is an error.
                raise(ValueError)
        elif new_node.data < parent_node.data:
            # If value of new node is smaller than parent's, add new node to its left
            parent_node._left_child = new_node
        else:
            # If value of new node is bigger than parent's, add new node to its right
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.

        Parameters:
        - 'data': The data to be found

        Returns:
        - The node that contains such data or None if data is not found
        """
        if data.__class__ is not int:
            data = data.data


        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child
        return None

    def _detach_node(self, nod):
        """
        Detach a node from the tree. Node to be detached has one child at most.
        An error will be raised otherwise.
        """

        #see that only 1 child exists
        if nod._left_child is not None and nod._right_child is not None:
            raise ValueError("Nodes with 2 children cannot be detached")

        #get the child node
        child_node = None
        if nod._left_child is not None:
            child_node = nod._left_child

        elif nod._right_child is not None:
            child_node = nod._right_child

        #is the node root node
        if nod is not self._root_node:
            #give the child to the parent
            if nod._parent._left_child == nod:
                nod._parent._left_child = child_node

            elif nod._parent._right_child == nod:
                nod._parent._right_child = child_node


        else:
            #set child as root node
            self._root_node = child_node



    def find_minimum_node(self, node):
        """
        Returns the minimum value of the tree
        """

        current_node = node
        while current_node:
            if current_node._left_child is not None:
                current_node = current_node._left_child
            else:
                return current_node

        return None


    def delete_node(self, data):
        found_node = self._find(data)

        if found_node is None:
            #print("Node not found")
            return

        #if no children
        if found_node._left_child is None and found_node._right_child is None:
            #print("Node with data", found_node.data, "no children")
            del found_node
            return

        #if only 1 child
        elif (found_node._left_child is not None and found_node._right_child is None) or (found_node._left_child is None and found_node._right_child is not None):
            #print("Node with data", found_node.data, "1 children:", found_node._left_child.data if found_node._left_child else None,  found_node._right_child.data if found_node._right_child else None)
            self._detach_node(found_node)
            del found_node
            return

        #if 2 children
        elif found_node._left_child is not None and found_node._right_child is not None:
            #print("Node with data", found_node.data, "2 children: ",found_node._left_child.data if found_node._left_child else None,  found_node._right_child.data if found_node._right_child else None)

            successor = self.find_minimum_node(found_node._right_child)

            #if successor is the right child
            if found_node._right_child == successor:
                successor.parent = found_node._parent if found_node._parent is not None else None
                #successor cannot have left child, successors right child remains unmodified
                successor._left_child = found_node._left_child
                found_node = successor


            else:
                #successor cannot have left child so it can be detached
                self._detach_node(successor)

                #replace target with successor
                successor._left_child = found_node._left_child
                successor._right_child = found_node._right_child
                successor._parent = found_node._parent if found_node._parent is not None else None

                found_node = successor

            #set root
            if found_node == self._root_node:
                self._root_node = successor


            del found_node

        else:
            #print("Error?")
            pass





#main
if __name__ == '__main__':
    tree = Tree()
    tree.insert(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(90)
    tree.insert(10)
    tree.insert(40)
    tree.insert(30)
    tree.insert(35)
    tree.delete_node(35)
    print(tree._find(tree._root_node.data))

    tree = Tree()
    tree.insert(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(90)
    tree.insert(10)
    tree.insert(40)
    tree.insert(30)
    tree.insert(35)
    tree.delete_node(30)
    print(tree._find(tree._root_node.data))

    tree = Tree()
    tree.insert(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(90)
    tree.insert(10)
    tree.insert(40)
    tree.insert(30)
    tree.insert(35)
    tree.delete_node(40)
    print(tree._find(tree._root_node.data))

    tree = Tree()
    tree.insert(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(90)
    tree.insert(10)
    tree.insert(40)
    tree.insert(30)
    tree.insert(35)
    tree.delete_node(20)
    print(tree._find(tree._root_node.data))

    tree = Tree()
    tree.insert(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(90)
    tree.insert(10)
    tree.insert(40)
    tree.insert(30)
    tree.insert(35)
    tree.delete_node(50)
    print(tree._find(tree._root_node.data))

    tree = Tree()
    tree.insert(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(90)
    tree.insert(10)
    tree.insert(40)
    tree.insert(30)
    tree.insert(35)
    tree.delete_node(50)
    tree.delete_node(20)
    tree.delete_node(70)
    tree.delete_node(90)
    tree.delete_node(10)
    tree.delete_node(40)
    tree.delete_node(30)
    tree.delete_node(35)
    print(tree._find(tree._root_node))

    import re

    tree = Tree()
    tree.insert(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(90)
    tree.insert(10)
    tree.insert(40)
    tree.insert(30)
    tree.insert(35)
    tree.delete_node(0)
    print(tree._find(tree._root_node.data))

    target = re.compile(tree._find(tree._root_node.data).__str__())
    if re.search(target,"50<20<10<><>#><40<30<><35<><>#>#><>#>#><70<><90<><>#>#>#"):
        print("true")

    if tree._find(tree._root_node.data).__str__() == "50<20<10<><>#><40<30<><35<><>#>#><>#>#><70<><90<><>#>#>#":
        print("true")