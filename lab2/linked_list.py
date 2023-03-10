#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

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
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def remove(self):
        if not self.is_empty():
            node = self.head
            if node.next is None:
                self.head = None
            else:
                self.head = node.next

    def remove_end(self):
        if not self.is_empty():
            if self.head.next is not None:
                previous_node = self.head
                next_node = self.head.next
                while next_node.next is not None:
                    previous_node = next_node
                    next_node = next_node.next
                previous_node.next = None
            else:
                self.head = None

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

uczelnie = LinkedList()

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
