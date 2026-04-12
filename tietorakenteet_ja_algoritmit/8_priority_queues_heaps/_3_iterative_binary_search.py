def binary_search_iterative(array, value):
    """
    Performs a binary search in the the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    if len(array) <= 0:
        return None

    low_end_index = 0
    high_end_index = len(array) - 1
    middle_index = (low_end_index + high_end_index) // 2
    #while index interval is greater than 2
    while low_end_index + 1 < high_end_index:
        #print(array[middle_index])

        if array[middle_index] > value:
            high_end_index = middle_index
            # recenter middle, round down
            middle_index = (low_end_index + high_end_index) // 2

        elif array[middle_index] < value:
            low_end_index = middle_index
            # recenter middle, round up te reach the top
            middle_index = ((low_end_index + high_end_index) // 2) + 1

        elif array[middle_index] == value:
            return middle_index

        else:
            raise RuntimeError('This should never happen')

    #if loop breaks see if value is in remaining 2 indexes
    if array[low_end_index] == value:
        return low_end_index
    elif array[high_end_index] == value:
        return high_end_index
    else:
        return None


#main
if __name__ == "__main__":
    array = [1, 2, 3]
    print(binary_search_iterative(array, 2))
    #tulos: 1

    array = [0, 5, 8, 11, 14, 17, 29, 31, 31, 35, 39, 40, 47, 61, 68, 78, 85, 88, 95, 98]
    print(binary_search_iterative(array, 0))
    print(binary_search_iterative(array, 98))
    print(binary_search_iterative(array, 29))
    print(binary_search_iterative(array, 100))
    print(binary_search_iterative(array, -1))
    print(binary_search_iterative(array, 44))