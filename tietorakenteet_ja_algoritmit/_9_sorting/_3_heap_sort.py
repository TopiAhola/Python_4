from multiprocessing.heap import Heap


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
        print("sink:", node_value, " at ", node_index)

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
    #end = end -1



def heap_sort(array):
    """
    Sort the array using the Heapsort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: Nothing. The array is sorted in-place.
    """
    #heapify?
    for heap_end in range(len(array) - 1, -1, -1):
        sift_down(array, heap_end, len(array) - 1)

    for heap_end in range(len(array)-1 , -1, -1 ):

        #put last element to root
        #print("swap: ", array[0], array[heap_end])
        array[0], array[heap_end] = array[heap_end], array[0]

        #print("End:",heap_end)
        #sink to sort
        sift_down(array, 0, heap_end-1)  ## miksi -1





#main
if __name__ == '__main__':
    array = [6, 8, 5, 1, 2]
    heap_sort(array)
    print(array)
    print([1, 2, 5, 6, 8])