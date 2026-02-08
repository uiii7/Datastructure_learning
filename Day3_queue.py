class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop()

    def size(self):
        return len(self.queue) if not self.isEmpty() else None

    def printQueue(self):
        print(self.queue)

