#!/usr/bin/python
# -*- coding: utf-8 -*-
size = 6


class Node:

    def __init__(self):
        self.table = [None for _ in range(size)]
        self.content = 0
        self.next = None

    def __str__(self):
        return str(self.table)

    def add_by_index(self, data, index):
        value_to_insert = data
        for i in range(index, size):
            temp = self.table[i]
            self.table[i] = value_to_insert
            value_to_insert = temp

    def delete_by_index(self, index):
        for i in range(index, size-1):
            self.table[i] = self.table[i+1]
        self.table[-1] = None

    def is_overloaded(self):
        return bool(self.content == size)


class UnrolledLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.sum_of_content = 0

    def __str__(self):
        if self.head is None:
            return '[]'
        result = ''
        node = self.head
        while node is not None:
            result += str(node) + ' -> '
            node = node.next
        return result[:-4]

    def get(self, index):
        if index > self.sum_of_content - 1:
            return None
        node, insert_index = self.identify_node_and_insert_index(index)
        return node.table[insert_index]

    def insert(self, data, index):
        if self.head is None:
            self.head = Node()
            self.tail = self.head
        if 0 <= index < self.sum_of_content:
            node, insert_index = self.identify_node_and_insert_index(index)
            if node.is_overloaded():
                self.add_new_node_and_split_data(node)
            node, insert_index = self.identify_node_and_insert_index(index)
            node.add_by_index(data, insert_index)
            node.content += 1
            self.sum_of_content += 1

        elif index >= self.sum_of_content:
            if self.tail.is_overloaded():
                self.add_new_node_and_split_data(self.tail)
            self.tail.add_by_index(data, self.tail.content)
            self.tail.content += 1
            self.sum_of_content += 1

    def delete(self, index):
        node, insert_index = self.identify_node_and_insert_index(index)
        node.delete_by_index(insert_index)
        node.content -= 1
        self.sum_of_content -= 1
        if node.content < 3:
            if node.next is not None:
                if node.next.content <= int(size/2):
                    self.rewrite_to_previous_node(node, node.next)
                else:
                    temp = node.next.table[0]
                    node.next.delete_by_index(0)
                    node.add_by_index(temp, node.content)

    def identify_node_and_insert_index(self, index):
        node = self.head
        while True:
            if index - node.content < 0:
                return node, index
            index -= node.content
            node = node.next

    def add_new_node_and_split_data(self, node):
        # przepiecie
        new_node = Node()
        new_node.next = node.next
        node.next = new_node
        if new_node.next is None:
            self.tail = new_node

        # przepisanie
        for i in range(0, int(size/2)):
            new_node.table[i] = node.table[int(size/2) + i]
            node.table[int(size / 2) + i] = None

        # aktualizacja ilosci w danym nodzie
        node.content = int(size/2)
        new_node.content = int(size/2)

    def rewrite_to_previous_node(self, node, next_node):
        for i in range(next_node.content):
            node.add_by_index(next_node[i], i + node.content)
        node.content += next_node.content
        if next_node.next is None:
            self.tail = node
            node.next = None
        else:
            node.next = next_node.next
            next_node.next = None


lista = UnrolledLinkedList()
for i in range(1, 9):
    lista.insert(data=i, index=i-1)
print(lista.get(4))
lista.insert(data=10, index=1)
lista.insert(data=11, index=8)
print(lista)
lista.delete(1)
lista.delete(2)
print(lista)
