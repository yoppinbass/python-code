class Queue():
    queue = list()
    def __init__(self):
        pass

    def enqueue(self, a):
        self.queue.append(a)
        print("{} enqueued. now: {}".format(a, self.queue))
        pass
    def dequeue(self):
        if len(self.queue) == 0:
            return
        a = self.queue.pop()
        print("{} poped. now: {}".format(a, self.queue))
        return a

        pass
    def show(self):
        print(self.queue)

if __name__ == '__main__':
    s = Queue()
    print(type(s))
    s.show()
    s.enqueue('a')
    s.show()
    s.enqueue('b')
    s.show()
    s.dequeue()
    s.show()
    s.dequeue()
    s.show()
    s.dequeue()
    s.show()
