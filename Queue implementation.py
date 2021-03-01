
class Queue:

    def __init__(self):
        self.Queue = []

    def isEmpty(self):
        return self.Queue == []

    def enqueue(self, data):
        self.Queue.append(data)

    def dequeue(self):
        data = self.Queue[0]
        del self.Queue[0]
        return data

    def peek(self):
        return self.Queue[0]

    def size1(self):
        return len(self.Queue)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print("size:", queue.size1())
print("Dequeue:", queue.dequeue())
print("peek:", queue.peek())