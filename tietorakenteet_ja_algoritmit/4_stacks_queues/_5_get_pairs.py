
from _4_node_list_queue import Queue

def get_pairs(number_list):

    odd_queue = Queue()
    even_queue = Queue()

    for number in number_list:
        if number % 2 == 0:
            even_queue.enqueue(number)
        elif number % 2 != 0:
            odd_queue.enqueue(number)
        else:
            raise(ValueError("Input invalid"))

    return_list = []
    while even_queue._size > 0 and odd_queue._size > 0:
        return_list.append( (even_queue.dequeue(),odd_queue.dequeue()) )

    return return_list