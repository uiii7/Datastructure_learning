#Define a stack using list

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def reverse(self):
        return self.items.reverse()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def printStack(self):
        for item in self.items:
            print(item)

#main
if __name__ == '__main__':
    s = Stack()
    s.push(4)
    s.push("aaa")
    s.push(True)
    s.printStack()