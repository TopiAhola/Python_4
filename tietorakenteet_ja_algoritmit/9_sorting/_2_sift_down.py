def sift_down(array, start, end):
    """
    This function sinks (if necessary) the given node of a MaxHeap structure

    Parameters:
    - array: The heap array
    - start: The index of the node that should be sinked.
    - end: The end of the heap inside the array. The index of the last node

    Returns: None
    """


    node_index = start

    while node_index <= end:

        node_value = array[node_index]
        #print("sink:", node_value, " at ", node_index)

        child1_index = 2 * node_index + 1
        child2_index = 2 * node_index + 2

        #get valid swap targets
        child_to_swap = None
        if child1_index <= end and child2_index <= end :
            if array[child1_index] >= array[child2_index]:
                child_to_swap = child1_index
            else:
                child_to_swap = child2_index

        elif child1_index <= end and child2_index > end:
            child_to_swap = child1_index

        elif child1_index > end and child2_index <= end:
            child_to_swap = child2_index

        elif child2_index > end and child1_index > end:
            break

        else:
            raise RuntimeError("This should not happen")

        #
        if child_to_swap is None or child_to_swap > end:
            break

        # swap
        if array[child_to_swap] > array[node_index]:
            #print("swap:", array[node_index], array[child_to_swap])
            array[node_index] = array[child_to_swap]
            array[child_to_swap] = node_value

            #point to new location
            node_index = child_to_swap
        else:
            #break if children are smaller
            break

    #after sinking raise the end of heap
    end = end -1

#main
if __name__ == '__main__':
    array = [6, 2, 5, 8, 1]
    sift_down(array, 1, 4)
    print(array)
    ''' [6, 8, 5, 2, 1] '''

    array = [6, 8, 5, 1, 2]
    sift_down(array, 0, 4)
    print(array)
    """[8, 6, 5, 1, 2]"""

    array = [2, 5, 6, 1, 8]
    sift_down(array, 0, 3)
    print(array)
    """[6, 5, 2, 1, 8]"""

    array = [1, 6, 5, 2, 3, 8]
    sift_down(array, 0, 4)
    print(array)
    """[6, 3, 5, 2, 1, 8]"""

    array = [1, 6, 5, 2, 3, 8]
    sift_down(array, 0, 3)
    print(array)
    """[6, 2, 5, 1, 3, 8]"""