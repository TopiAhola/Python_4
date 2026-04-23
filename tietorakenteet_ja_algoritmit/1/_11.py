def combine_lists(list1, list2):
    return_list = []

    while list1 and list2:
        if list1[0] <= list2[0]:
            return_list.append(list1.pop(0))

        elif list1[0] > list2[0]:
            return_list.append(list2.pop(0))

        else:
            raise ValueError()

    while list1:
        return_list.append(list1.pop(0))

    while list2:
        return_list.append(list2.pop(0))

    return return_list


#main

print(combine_lists([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]))
