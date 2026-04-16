def insertion_sort(array):
    """
    Sort the array using the Insertion sort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: Nothing. The array is sorted in-place.
    """

    for index in range(1, len(array)):

        insert_pointer = index - 1
        value = array[index]

        while insert_pointer >= 0 and array[insert_pointer] > value:
            #shift element to right
            array[insert_pointer +1] = array[insert_pointer]
            array[insert_pointer] = value
            insert_pointer = insert_pointer - 1









#main
if __name__ == '__main__':
    array = [6, 8, 5, 1, 2]
    insertion_sort(array)
    print(array)

    from random import randint

    array = [randint(0, 100) for _ in range(20)]
    sorted_array = sorted(array)
    insertion_sort(array)
    print(array == sorted_array)