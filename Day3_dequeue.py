class Deque:
    """
    Deque

    """
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def addFront(self, item):
        self.item.append(item)

    def addRear(self, item):
        self.item.insert(0, item)

    def removeFront(self):
        return self.item.pop()

    def removeRear(self):
        return self.item.pop(0)

    def printDeque(self):
        print(self.item)

if __name__ == '__main__':
    d = Deque()
    for i in range(10):
        d.addFront(i)
    for j in range(10):
        d.addRear(j)

    d.printDeque()