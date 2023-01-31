'''
Date: 2022-06-05 22:59:28
LastEditors: r7000p
LastEditTime: 2022-06-06 23:04:48
FilePath: \Daily\daily-python\06\0605.py
'''
class MyCircularQueue:

    def __init__(self, k):
        self._list = [None] * k
        self.size = k
        self.tail = -1
        self.head = -1

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.head += 1
            self.tail += 1
            self._list[self.tail] = value
            return True
        elif self.isFull():
            return False
        else:
            self.tail = (self.tail + 1) % self.size
            self._list[self.tail] = value
            return True
    def deQueue(self) -> bool:
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        elif self.isEmpty():
            return False
        else:
            self.head = (self.head + 1) % self.size
            return True
    def Front(self) -> int:
        return -1 if self.isEmpty() else self._list[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self._list[self.tail]

    def isEmpty(self) -> bool:
        return self.tail == -1 and self.head == -1

    def isFull(self) -> bool:
        return (self.tail + 1) % self.size == self.head


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()