#!/usr/bin/python
# -*- coding: utf-8 -*-

class Element:

    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority

    def __str__(self):
        return f'{self.__priority} : {self.__data}'

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority


class PriorityQueue:

    def __init__(self):
        self.size = 0
        self.table = []

    def print_tab(self):
        print('{', end=' ')
        for i in range(self.size):
            print(self.table[i], end=', ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.table[idx] if self.table[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.table[0]

    def dequeue(self):
        if self.is_empty():
            return None
        result = self.table[0]
        self.swap(0, self.size-1)
        self.size -= 1
        self.heapify()
        return result

    def enqueue(self, element):
        if self.size == len(self.table):
            self.table.append(element)
        else:
            self.table[self.size] = element
        self.size += 1
        index = self.size - 1
        # repairing the structure to remain heap
        while self.parent(index) > -1:
            if self.table[index] > self.table[self.parent(index)]:
                self.swap(index, self.parent(index))
                index = self.parent(index)
            else:
                break

    def heapify(self, index=0):
        # repairing the structure to remain heap
        current = index
        while index < self.size - 1:
            left = self.left(current)
            right = self.right(current)
            if left < self.size and self.table[left] > self.table[index]:
                index = left
            if right < self.size and self.table[right] > self.table[index]:
                index = right
            if index == current:
                break
            else:
                self.swap(current, index)
                current = index

    # methods allowing easier traversing a heap
    def left(self, index):
        return 2*index + 1

    def right(self, index):
        return 2*index + 2

    def parent(self, index):
        return (index-1)//2

    def swap(self, i, j):
        self.table[i], self.table[j] = self.table[j], self.table[i]


q = PriorityQueue()
for data, priority in zip("GRYMOTYLA", [7, 5, 1, 2, 5, 3, 4, 8, 9]):
    q.enqueue(Element(data, priority))
q.print_tree(0, 0)
q.print_tab()
temp = q.dequeue()
print(q.peek())
q.print_tab()
print(temp)
while not q.is_empty():
    print(q.dequeue())
q.print_tab()
