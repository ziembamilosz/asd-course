#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import time


class Element:

    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority

    def __repr__(self):
        return f'{self.__priority} : {self.__data}'

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority


class PriorityQueue:

    def __init__(self, to_sort=None):
        if to_sort is not None:
            self.table = to_sort
            self.size = len(to_sort)
            for i in range(self.parent(self.size - 1), -1, -1):
                self.heapify(i)
        else:
            self.table = []
            self.size = 0

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

    def sort(self):
        while not self.is_empty():
            self.dequeue()

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
        self.size -= 1
        self.swap(0, self.size)
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
            if left < self.size and not (self.table[left] < self.table[index]):
                index = left
            if right < self.size and not (self.table[right] < self.table[index]):
                index = right
            if index == current:
                break
            self.swap(current, index)
            current = index

    # methods allowing easier traversing a heap
    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def parent(self, index):
        return (index - 1) // 2

    def swap(self, i, j):
        self.table[i], self.table[j] = self.table[j], self.table[i]


def find_min_index(lst, i, n):
    min_index = i
    for j in range(i, n):
        if lst[j] < lst[min_index]:
            min_index = j
    return min_index


def selection_sort_swap(lst):
    n = len(lst)
    for i in range(n):
        min_index = find_min_index(lst, i, n)
        lst[i], lst[min_index] = lst[min_index], lst[i]


def selection_sort_shift(lst: list):
    n = len(lst)
    for i in range(n):
        min_index = find_min_index(lst, i, n)
        lst.insert(i, lst.pop(min_index))


lst_of_objects = [Element(data, priority) for priority, data in [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
                                                                 (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]]
q = PriorityQueue(lst_of_objects)
q.print_tab()
print()
q.print_tree(0, 0)
print()
q.sort()
print(lst_of_objects)
print('Algorytm niestabilny')

lst_of_random_numbers = [int(random.random() * 100) for _ in range(10000)]
t_start = time.perf_counter()
q2 = PriorityQueue(lst_of_random_numbers)
q2.sort()
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

lst_of_objects = [Element(data, priority) for priority, data in [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
                                                                 (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]]
selection_sort_swap(lst_of_objects)
print('Algorytm niestabilny')

lst_of_random_numbers = [int(random.random() * 100) for _ in range(10000)]
t_start = time.perf_counter()
selection_sort_swap(lst_of_random_numbers)
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

lst_of_objects = [Element(data, priority) for priority, data in [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
                                                                 (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]]
selection_sort_shift(lst_of_objects)
print('Algorytm niestabilny')

lst_of_random_numbers = [int(random.random() * 100) for _ in range(10000)]
t_start = time.perf_counter()
selection_sort_shift(lst_of_random_numbers)
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
