import time
from random import randint


def merge_sort(array):
    """
    Sort the array using the Merge sort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: The sorted array.
    """

    if len(array) <= 1 :
        return array

    middle = len(array) // 2
    left_side = merge_sort(array[:middle])
    right_side = merge_sort(array[middle:])

    return_array = []   #len(left_side) + len(right_side)
    left_side_pointer = 0
    right_side_pointer = 0


    for index in range(0, len(left_side) + len(right_side), 1 ):

        #if both subarrays have been iterated
        if left_side_pointer > len(left_side) - 1 and right_side_pointer > len(right_side) - 1:
            return return_array

        #if left side is done iterate from right side
        elif left_side_pointer > len(left_side) - 1:
            return_array.append(right_side[right_side_pointer])
            right_side_pointer += 1

        #if right side is done iterate from lef side
        elif right_side_pointer > len(right_side) - 1:
            return_array.append(left_side[left_side_pointer])
            left_side_pointer += 1

        #if neither is done
        else:
            #compare which to add
            element1 = left_side[left_side_pointer]
            element2 = right_side[right_side_pointer]

            if right_side_pointer > len(right_side) -1 or element1 < element2:
                return_array.append(element1)
                left_side_pointer += 1

            elif element1 > element2:
                return_array.append(element2)
                right_side_pointer += 1

            elif element1 == element2:
                return_array.append(element1)
                return_array.append(element2)
                left_side_pointer += 1
                right_side_pointer += 1



    return return_array



#main
if __name__ == '__main__':
    array = [6, 8, 5, 1, 2, 3, 4, 5,7,9,2,6,78,0,4,3]
    print(array)
    array2 = merge_sort(array)
    print(array2)

    array = [randint(0, 10000) for _ in range(10000)]
    start_time = time.time()
    _ = merge_sort(array)
    runtime = time.time() - start_time
    print(f'Merge sort runtime: {runtime}')
