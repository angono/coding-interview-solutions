# Deque uses FIFO and LIFO
# Deque data are mutable. e.g. Python list

class Deque:
    def __init__(self):
        self.items = []

    def add_rear(self, item):
        return self.items.append(item)

    def add_front(self, item):
        return self.items.insert(0, item)

    def remove_rear(self):
        if self.items:
            return self.items.pop()
        return None

    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        return None

    def peek_rear(self):
        if self.items:
            self.items[-1]
        return None

    def peek_front(self):
        if self.items:
            return self.items[0]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


def check_palindrome(input_str):
    my_deque = Deque()
    for char in input_str:
        my_deque.add_rear(char)

    # Size 1 or 0 means the string is a palindrome
    while my_deque.size() >= 2:
        front_item = my_deque.remove_front()
        rear_item = my_deque.remove_rear()

        if front_item != rear_item:
            return False
    return True


# print(check_palindrome('racecar'))
# print(check_palindrome('oranges'))

from collections import deque

def checkpd(A):
    d = deque(A)
    while len(d) >= 2:
        if d.pop() != d.popleft():
            return False
    return True


print(checkpd('racecar'))
print(checkpd('choice'))
print(checkpd('radar'))
print(checkpd('derkos'))





