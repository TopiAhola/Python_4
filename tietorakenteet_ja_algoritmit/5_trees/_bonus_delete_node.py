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
        if data is None:
            return None

        if data.__class__ is Node:
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

    def _detach_node(self, node):
        """
        Detach a node from the tree. Node to be detached has one child at most.
        An error will be raised otherwise.
        """

        #see that only 1 child exists
        if node._left_child is not None and node._right_child is not None:
            raise ValueError("Nodes with 2 children cannot be detached")

        #get the child node
        child_node = None
        if node._left_child is not None:
            child_node = node._left_child

        elif node._right_child is not None:
            child_node = node._right_child

        ##set parent point to child
        #is not root
        if node._parent is not None and node is not self._root_node:
            #give the child to the parent
            if node._parent._left_child == node:
                node._parent._left_child = child_node

            elif node._parent._right_child == node:
                node._parent._right_child = child_node

            #tell child the new parent
            if child_node is not None:
                child_node._parent = node._parent

        #is root
        elif node is self._root_node and node._parent is None:
            #set child as root node
            self._root_node = child_node

            # tell child the new parent
            if child_node is not None:
                child_node._parent = None

        # bad node
        elif node._parent is None and node is not self._root_node:
            raise RuntimeError("This should not happen")




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

        raise(RuntimeError("This should not happen"))


    def delete_node(self, data):
        found_node = self._find(data)

        #if not found return
        if found_node is None:
            return

        #if only 1 or 0 child
        elif found_node._left_child is None or found_node._right_child is None:
            self.debug_print("Found node with 0 or 1 child:", found_node)
            self._detach_node(found_node)


        #if 2 children
        elif found_node._left_child is not None and found_node._right_child is not None:

            self.debug_print("Found node with 2 children:", found_node)

            successor = self.find_minimum_node(found_node._right_child)

            #if successor is the right child
            if found_node._right_child is successor:
                self.debug_print("Successor was right child of target:", successor)

                #successor cannot have left child, successors right child remains unmodified????
                successor._left_child = found_node._left_child

                #set new left child point to successor
                successor._left_child._parent = successor

                successor.parent = found_node._parent if found_node._parent is not None else None

                # set parent point ot successor
                if found_node._parent is not None:
                    if found_node._parent._left_child is found_node:
                        print("found node was left child")
                        found_node._parent._left_child = successor

                    elif found_node._parent._right_child is found_node:
                        print("found node was left child")
                        found_node._parent._right_child = successor

                    else:
                        raise RuntimeError("This should not happen")

                else:
                    successor._parent = None


            else:
                self.debug_print("Successor was not direct child of target:", successor)

                #successor cannot have left child so it can be detached
                self._detach_node(successor)

                #replace target with successor
                successor._left_child = found_node._left_child
                successor._right_child = found_node._right_child
                successor._parent = found_node._parent if found_node._parent is not None else None

                #set children point to successor
                successor._left_child._parent = successor
                successor._right_child._parent = successor

                #set parent point ot successor
                if found_node._parent is not None:
                    if found_node._parent._left_child is found_node:
                        print("found node was left child")
                        found_node._parent._left_child = successor

                    elif found_node._parent._right_child is found_node:
                        print("found node was left child")
                        found_node._parent._right_child = successor

                    else:
                        raise RuntimeError("This should not happen")

                else:
                    successor._parent = None

                self.debug_print("Successor after replacement:", successor)

            #set root if necessary
            if found_node == self._root_node:
                self._root_node = successor

            self.debug_print("Successor after:", successor)
            self.debug_print("Root after:", self._root_node)

            return

        else:
            raise RuntimeError("This should not happen")

    def debug_print(self, text, node):
        print(text, node.data, "parent:",
              node._parent.data if node._parent else None,
              "children: ", node._left_child.data if node._left_child else None,
              node._right_child.data if node._right_child else None)


    def delete_node2(self, data):

        # Find the node to remove
        node_to_remove = self._find(data)
        # if node is not found, return
        if not node_to_remove:
            return
        # If node has only one or no child, just detach the node from the tree,
        # replacing it with one of its childs (if any)
        if node_to_remove._left_child is None or node_to_remove._right_child is None:
            self._detach_node(node_to_remove)
        else:
            # Node to be removed has two children. Find its successor.
            # By definition the successor does not have a left child
            # (because then it would be the actual successor)

            #successor_node = self._find_successor(node_to_remove)
            successor_node = self.find_minimum_node(node_to_remove._right_child)

            # Detach the successor from the tree
            self._detach_node(successor_node)
            # And replace the node to remove with the successor
            self._replace_node(node_to_remove, successor_node)


    def _replace_node(self, node_to_replace, replacement_node):
        """
        Link the parent and children of the node to be replaced to the replacement node.
        Replacement node and node to be replaced must exist.
        Node to be replaced is not modified.
        If node_to_replace is Root node, then _root_node pointer is updated.
        if BST rules are not fulfilled, an error is thrown.
        """
        # Check nodes exist.
        if node_to_replace is None or replacement_node is None:
            raise (ValueError)

        parent_node = node_to_replace._parent
        # Link the replacement node to the parent
        replacement_node._parent = parent_node  # Bottom up
        # If node to replace is Root node, update _root_node pointer.
        if node_to_replace is self._root_node:
            self._root_node = replacement_node  # From top to bottom
        # If not, link parent to the replacement on the right or the left
        elif parent_node._left_child is node_to_replace:
            # Replacement is left node
            if replacement_node.data > parent_node.data:
                raise (ValueError)
            parent_node._left_child = replacement_node  # From top to bottom
        else:
            # Replacement is right node
            if replacement_node.data < parent_node.data:
                raise (ValueError)
            parent_node._right_child = replacement_node  # From top to bottom

        # Link replacement node to child nodes (if any)
        # From parent to child
        replacement_node._left_child = node_to_replace._left_child
        replacement_node._right_child = node_to_replace._right_child
        # From child to parent
        if replacement_node._left_child:
            if replacement_node._left_child.data > replacement_node.data:
                raise (ValueError)
            replacement_node._left_child._parent = replacement_node
        if replacement_node._right_child:
            if replacement_node._right_child.data < replacement_node.data:
                raise (ValueError)
            replacement_node._right_child._parent = replacement_node


#main
if __name__ == '__main__':
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
    tree.delete_node(35)
    print(tree._find(tree._root_node.data))
    print()


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
    print()

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
    print()

    tree = Tree()
    tree.insert(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(90)
    tree.insert(10)
    tree.insert(40)
    tree.insert(30)
    tree.insert(35)
    print("Before:", tree._find(tree._root_node.data))
    tree.delete_node(20)
    print("After 20:",tree._find(tree._root_node.data))
    print()

    tree = Tree()
    tree.insert(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(90)
    tree.insert(10)
    tree.insert(40)
    tree.insert(30)
    tree.insert(35)
    print("Before: ", tree._find(tree._root_node.data))
    tree.delete_node(50)
    print("After 50:",tree._find(tree._root_node.data))
    print()

    tree = Tree()
    tree.insert(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(90)
    tree.insert(10)
    tree.insert(40)
    tree.insert(30)
    tree.insert(35)
    print("Before:" , tree._find(tree._root_node.data))
    tree.delete_node(50)
    print("After 50:", tree._find(tree._root_node.data))
    tree.delete_node(20)
    print("After 20:", tree._find(tree._root_node.data))
    tree.delete_node(70)
    print("After 70:", tree._find(tree._root_node.data))
    tree.delete_node(90)
    print("After 90:", tree._find(tree._root_node.data))
    tree.delete_node(10)
    print("After 10:", tree._find(tree._root_node.data))
    tree.delete_node(40)
    print("After 40:", tree._find(tree._root_node.data))
    tree.delete_node(30)
    print("After 30:", tree._find(tree._root_node.data))
    tree.delete_node(35)
    print("After 35:", tree._find(tree._root_node.data) if tree._find(tree._root_node) is not None else "" )

    target = re.compile(tree._find(tree._root_node.data).__str__())
    if re.search(target, "None"):
        print("true")
    else:
        print("false")
    print()


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

    print()