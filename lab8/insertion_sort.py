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


def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
    return lst


def shell_sort(lst):
    n = len(lst)
    h = n // 2
    while h > 0:
        for outer in range(h, n):
            insertion_value = lst[outer]
            inner = outer
            while inner - h > - 1 and lst[inner - h] > insertion_value:
                lst[inner] = lst[inner - h]
                inner = inner - h
            lst[inner] = insertion_value
        h = h // 2
    return lst


lst_of_objects = [Element(data, priority) for priority, data in [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
                                                                 (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]]
insertion_sort(lst_of_objects)
print(lst_of_objects)

lst_of_random_numbers = [int(random.random() * 100) for _ in range(10000)]
t_start = time.perf_counter()
insertion_sort(lst_of_random_numbers)
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print('Algorytm stabilny')

lst_of_objects = [Element(data, priority) for priority, data in [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
                                                                 (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]]
shell_sort(lst_of_objects)
print(lst_of_objects)

lst_of_random_numbers = [int(random.random() * 100) for _ in range(10000)]
t_start = time.perf_counter()
shell_sort(lst_of_random_numbers)
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print('Algorytm niestabilny')
