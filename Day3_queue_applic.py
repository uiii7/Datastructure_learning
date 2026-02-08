from Day3_queue import Queue


def HotPotato(name, num):
    q = Queue()
    for name in name:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


print(HotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
