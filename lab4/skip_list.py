#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


class Node:

    def __init__(self, key, value, max_levels, levels=0):
        self.key = key
        self.value = value
        self.max_levels = max_levels
        self.levels = levels if levels > 0 else self.calculate_random_level()
        self.next = [None for _ in range(self.levels)]

    def calculate_random_level(self, p=0.5):
        level = 1
        while random.random() < p and level < self.max_levels:
            level += 1
        return level

    def __str__(self):
        return f'{self.key} : {self.value}, '


class SkipList:

    def __init__(self, max_levels):
        self.head = Node(None, None, max_levels, max_levels)
        self.max_levels = max_levels

    def display_list(self):
        node = self.head.next[0]
        keys = []
        while node is not None:
            keys.append(node.key)
            node = node.next[0]

        for lvl in range(self.max_levels - 1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head.next[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print("  ", end=" ")
                    idx += 1
                idx += 1
                print("{:2d}".format(node.key), end=" ")
                node = node.next[lvl]
            print("")

    def __str__(self):
        result = '[ '
        node = self.head
        while node.next[0] is not None:
            node = node.next[0]
            result += str(node)
        return result[:-2] + ' ]'

    def search(self, key):

        current = self.head

        for i in reversed(range(self.max_levels)):
            while current.next[i] is not None and current.next[i].key < key:
                current = current.next[i]

        current = current.next[0]

        if current is None or current.key != key:
            return None

        return current.value

    def insert(self, key, value):
        current = self.head
        previous_in_each_level = [None for _ in range(self.max_levels)]
        for i in reversed(range(self.max_levels)):
            while current.next[i] is not None and current.next[i].key < key:
                current = current.next[i]
            previous_in_each_level[i] = current
        current = current.next[0]
        # if key exists, overwriting its data, otherwise inserting new node and making it work with already existing
        if current is not None and current.key == key:
            current.value = value
        else:
            new_node = Node(key, value, self.max_levels)
            for i in reversed(range(new_node.levels)):
                new_node.next[i] = previous_in_each_level[i].next[i]
                previous_in_each_level[i].next[i] = new_node

    def remove(self, key):

        previous = self.head
        previous_in_each_level = [None for _ in range(self.max_levels)]
        for i in reversed(range(self.max_levels)):
            while previous.next[i] is not None and previous.next[i].key < key:
                previous = previous.next[i]
            previous_in_each_level[i] = previous

        current = previous.next[0]
        if current is not None and current.key == key:
            for i in reversed(range(current.levels)):
                previous_in_each_level[i].next[i] = current.next[i]


max_level = 6
skiplist = SkipList(max_level)
letter = ord('A')
for i in range(1, 16):
    skiplist.insert(i, chr(letter))
    letter += 1
skiplist.display_list()
print(skiplist.search(2))
skiplist.insert(2, 'Z')
print(skiplist.search(2))
skiplist.remove(5)
skiplist.remove(6)
skiplist.remove(7)
print(skiplist)
skiplist.insert(6, 'W')
print(skiplist)

skiplist = SkipList(max_level)
letter = ord('A')
for i in range(15, 0, -1):
    skiplist.insert(i, chr(letter))
    letter += 1
skiplist.display_list()
print(skiplist.search(2))
skiplist.insert(2, 'Z')
print(skiplist.search(2))
skiplist.remove(5)
skiplist.remove(6)
skiplist.remove(7)
print(skiplist)
skiplist.insert(6, 'W')
print(skiplist)