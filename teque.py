import sys
from collections import deque

class Teque:
    def __init__(self):
        self.a = deque()
        self.b = deque()

    def push_back(self, number):
        self.b.append(number)
        self._balance()

    def push_front(self, number):
        self.a.appendleft(number)
        self._balance()

    def push_middle(self, number):
        if len(self.a) - len(self.b) == 0:
            self.a.append(number)
        elif len(self.b) > len(self.a):
            self.a.append(self.b.popleft())
            self.b.appendleft(number)
        else:
            self.b.appendleft(number)

    def get_item(self, index):
        if index > (len(self.a)  - 1):
            return self.b[index - len(self.a)]
        else: 
            return self.a[index]

    def _balance(self):
        if abs(len(self.a) - len(self.b)) <= 1:
            return
        
        elif len(self.b) > len(self.a):
            self.a.append(self.b.popleft())

        else:
            self.b.appendleft(self.a.pop())


def main():
    number_of_operations = int(sys.stdin.readline())
    teque = Teque()

    for _ in range(number_of_operations):
        operation, nr = sys.stdin.readline().split()
        nr = int(nr)
        index = nr

        if operation == "push_back":
            teque.push_back(nr)
        elif operation == "push_front":
            teque.push_front(nr)
        elif operation == "push_middle":
            teque.push_middle(nr)
        else:
            sys.stdout.write(str(teque.get_item(index)))
            sys.stdout.write("\n")

main()
