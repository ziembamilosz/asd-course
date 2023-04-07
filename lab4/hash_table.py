#!/usr/bin/python
# -*- coding: utf-8 -*-

class ListIsFullException(Exception):
    pass


class KeyNotFoundException(Exception):
    pass


class Pair:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f'{self.key}: {self.value}'


class HashTable:

    def __init__(self, size, c1=1, c2=0):
        self.table = [None for _ in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def __str__(self):
        result = '{'
        for pair in self.table:
            result += str(pair) + ', '
        return result[:-2] +'}'

    def search(self, key):
        index = self.hash_function(key)

        if self.table[index] is not None and self.table[index].key == key:
            return self.table[index].value

        # rehashing with linear/quadratic probing
        for i in range(1, self.size):
            new_index = (index + self.c1 * i + self.c2 * i ** 2) % self.size
            if self.table[new_index] is not None and self.table[new_index].key == key:
                return self.table[new_index].value

    def insert(self, key, value):
        pair = Pair(key, value)
        index = self.hash_function(key)

        if self.table[index] is None:
            self.table[index] = pair
            return

        if self.table[index].key == key:
            self.table[index] = pair
            return

        # rehashing with linear/quadratic probing
        for i in range(1, self.size):
            new_index = (index + self.c1*i + self.c2*i**2) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = pair
                return
            if self.table[new_index].key == key:
                self.table[new_index] = pair
                return

        raise ListIsFullException('Brak miejsca')

    def remove(self, key):
        index = self.hash_function(key)

        if self.table[index] is not None and self.table[index].key == key:
            self.table[index] = None
            return

        # rehashing with linear/quadratic probing
        for i in range(1, self.size):
            new_index = (index + self.c1*i + self.c2*i**2) % self.size
            if self.table[new_index] is not None and self.table[new_index].key == key:
                self.table[new_index] = None
                return
        raise KeyNotFoundException('Brak takiego klucza')

    def hash_function(self, key):
        # hashing key to index
        if isinstance(key, str):
            index = 0
            for letter in key:
                index += ord(letter)
        else:
            index = key
        return index % self.size


def fun1(size, c1=1, c2=0):
    tablica = HashTable(size, c1, c2)
    letter = ord('A')
    for i in range(1, 16):
        if i == 6:
            try:
                tablica.insert(18, chr(letter))
            except Exception as e:
                print(e)
        elif i == 7:
            try:
                tablica.insert(31, chr(letter))
            except Exception as e:
                print(e)
        else:
            try:
                tablica.insert(i, chr(letter))
            except Exception as e:
                print(e)
        letter += 1
    print(tablica)
    print(tablica.search(5))
    print(tablica.search(14))
    tablica.insert(5, 'Z')
    print(tablica.search(5))
    try:
        tablica.remove(5)
    except Exception as e:
        print(e)
    print(tablica)
    print(tablica.search(31))
    try:
        tablica.insert('test', 'W')
    except Exception as e:
        print(e)
    print(tablica)


def fun2(size, c1=1, c2=0):
    tablica = HashTable(size, c1, c2)
    letter = ord('A')
    for i in range(1, 16):
        try:
            tablica.insert(i*13, chr(letter))
        except Exception as e:
            print(e)
        letter += 1
    print(tablica)


def main():
    fun1(13)
    fun2(13)
    fun2(13, c1=0, c2=1)
    fun1(13, c1=0, c2=1)


main()
