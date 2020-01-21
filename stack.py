class Stack():
    stack = list()
    def __init__(self):
        pass

    def push(self, a):
        self.stack.insert(0, a)
        print("{} pushed. now: {}".format(a, self.stack))
        pass
    def pop(self):
        if len(self.stack) == 0:
            return
        a = self.stack[0]
        self.stack.remove(a)
        print("{} poped. now: {}".format(a, self.stack))
        return a

        pass
    def show(self):
        return self.stack

if __name__ == '__main__':
    s = Stack()
    print(type(s))
    s.show()
    s.push('a')
    s.show()
    s.push('b')
    s.show()
    s.pop()
    s.show()
    s.pop()
    s.show()
    s.pop()
    s.show()
