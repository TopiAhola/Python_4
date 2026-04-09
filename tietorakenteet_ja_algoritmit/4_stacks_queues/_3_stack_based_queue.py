




class StackBasedQueue():

    def __init__(self):
        self._InboundStack = []
        self._OutboundStack = []
        self._size = 0

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack][::-1]
        values.extend([c for c in self._OutboundStack])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'


    def enqueue(self, data):
        self._InboundStack.append(data)
        self._size += 1

    def dequeue(self):
        if len(self._OutboundStack) == 0:
            while len(self._InboundStack) > 0:
                self._OutboundStack.append(self._InboundStack.pop())


        if len(self._OutboundStack) > 0:
            self._size -= 1
            return self._OutboundStack.pop()

        else:
            return None

#main


queue = StackBasedQueue()
print(queue)

queue = StackBasedQueue()
queue.enqueue('A')
print(queue)

queue = StackBasedQueue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
print(queue)

queue = StackBasedQueue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
val = queue.dequeue()
print(val, queue)