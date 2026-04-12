def interpolation_search(array, value):
    """
    Performs an Interpolation search in the the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """

    if len(array) <= 0:
        return None

    low_index = 0
    high_index = len(array) - 1
    middle_index = 0

    #calculate midpoint
    value_range = (array[high_index] - array[low_index])
    if value_range >= 0:
        middle_index = low_index + int((high_index - low_index) * ((value - array[low_index]) / value_range))
    if value_range < 0:
        return None
    else:
        middle_index = (low_index + high_index) // 2

    #while index interval is greater than 2
    while low_index + 1 < high_index:
        #print(array[middle_index])

        if array[middle_index] > value:
            high_index = middle_index #tämä voisi olla myös middle_index -1
            # recenter middle, round down


        elif array[middle_index] < value:
            low_index = middle_index  #tämä voisi olla myös middle_index +1
            # recenter middle, round up te reach the top


        elif array[middle_index] == value:
            return middle_index

        else:
            raise RuntimeError('This should never happen')

        #calulate new midpoint
        value_range = (array[high_index] - array[low_index])
        if value_range >= 0:
            middle_index = low_index + int((high_index - low_index) * ((value - array[low_index]) / value_range ))
        if value_range < 0:
            return None
        else:
            middle_index = (low_index + high_index) // 2

    #if loop breaks see if value is in remaining 2 indexes
    if array[low_index] == value:
        return low_index
    elif array[high_index] == value:
        return high_index
    else:
        return None





#main
if __name__ == "__main__":
    array = [0, 5, 8, 11, 14, 17, 29, 31, 31, 35, 39, 40, 47, 61, 68, 78, 85, 88, 95, 98]
    print(interpolation_search(array, 0))
    print(interpolation_search(array, 98))
    print(interpolation_search(array, 29))
    print(interpolation_search(array, 100))
    print(interpolation_search(array, -1))
    print(interpolation_search(array, 44))


    '''
    0
    19
    6
    None
    None
    None
    '''