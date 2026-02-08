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


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        while current is not None:
            previous = current
            current = current.getNext()
            if current.getData() == item:
                previous.setNext(current.getNext())
                current.setNext(None)
                break
        return None

    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            current = current.getNext()
            count += 1
            if current.getData() == item:
                return count
            return None
        return None