#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.is_empty():
            return None
        node = self.head
        result = ""
        while node is not None:
            result += f"-> {str(node.data)}\n"
            node = node.next
        return result

    def __len__(self):
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def destroy(self):
        length = len(self)
        if length > 2:
            self.head.next.prev = None
            self.head.next = None
            self.tail.prev.next = None
            self.tail.prev = None
        elif length == 2:
            self.head.next.prev = None
            self.head.next = None
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove(self):
        if not self.is_empty():
            node = self.head
            if node.next is None:
                self.head = None
                self.tail = None
            else:
                next_node = node.next
                next_node.prev = None
                self.head = next_node

    def remove_end(self):
        if not self.is_empty():
            node = self.tail
            if node.prev is None:
                self.head = None
                self.tail = None
            else:
                prev_node = node.prev
                prev_node.next = None
                self.tail = prev_node

    def is_empty(self):
        return bool(not self.head)

    def get(self):
        if self.is_empty():
            return None
        return self.head.data


lst = \
[('AGH', 'Kraków', 1919),
('UJ', 'Kraków', 1364),
('PW', 'Warszawa', 1915),
('UW', 'Warszawa', 1915),
('UP', 'Poznań', 1919),
('PG', 'Gdańsk', 1945)]

uczelnie = DoublyLinkedList()

for i in range(len(lst[:3])):
    uczelnie.add(lst[i])
for i in range(3, len(lst)):
    uczelnie.append(lst[i])
print(uczelnie)
print(len(uczelnie))
uczelnie.remove()
print(uczelnie.get())
uczelnie.remove_end()
print(uczelnie)
uczelnie.destroy()
print(uczelnie.is_empty())
uczelnie.remove()
uczelnie.remove_end()
