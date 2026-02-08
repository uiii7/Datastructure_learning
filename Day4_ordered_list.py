class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next


class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        current = self.head
        previous = None

        while current is not None and current.getData() < item:
            previous = current
            current = current.getNext()

        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.getData() == item:
                if previous is None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                current.setNext(None)
                return True
            previous = current
            current = current.getNext()
        return False

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            if current.getData() != item:
                current = current.getNext()
                count += 1
            else:
                return count

    def pop(self, pos=None):
        if pos is None:
            current = self.head
            previous = None
            while current.getNext() is not None:
                previous = current
                current = current.getNext()
            if previous is None:
                self.head = None
            else:
                previous.setNext(None)
            return current.getData()

        else:
            current = self.head
            count = 0
            previous = None
            while current is not None:
                if count == pos:
                    if previous is None:
                        self.head = current.getNext()
                    else:
                        previous.setNext(current.getNext())
                    current.setNext(None)
                    return current.getData()
                previous = current
                current = current.getNext()
                count += 1
            return None

if __name__ == '__main__':
    ols = OrderedList()
    for i in range(10):
        ols.add(i)
    print(ols.pop(1))
    print(ols.pop())
