from Day3_queue import Queue
import random



class Task:
    def __init__(self, time):
        self.time = time
        self.pages = random.randrange(1, 21)

    def getPages(self):
        return self.pages

    def getTime(self):
        return self.time

    def waitTime(self, currenttime):
        return currenttime - self.time

def newTask():
    prob = random.randrange(1,181)
    return prob == 180

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.timeremain = 0
        self.isbusy = False
        self.current_task = None

    def tick(self):
        if self.current_task is not None:
            self.timeremain -= 1
            if self.timeremain <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def newtask(self, newtask):
        self.current_task = newtask
        self.timeremain = newtask.getPages() * 60 / self.pagerate

def run(num_seconds, ppm) -> None:
    printer = Printer(ppm)
    printq = Queue()
    waittime = []
    for currenttime in range(num_seconds):
        if newTask():
            task = Task(currenttime)
            printq.enqueue(task)
        if (not printer.busy()) and (not printq.isEmpty()):
            nexttask = printq.dequeue()
            waittime.append(nexttask.waitTime(currenttime))
            printer.newtask(nexttask)
        printer.tick()
    if len(waittime) == 0:
        print("No Tasks.")
    else:
        average_wait = sum(waittime) / len(waittime)
        print(f"Average wait {average_wait} s, {printq.size()} tasks remaining.")

if __name__ == '__main__':
    for i in range(10):
        run(3600, 5)