#!/usr/bin/python
# -*- coding: utf-8 -*-

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
    return lst


print(selection_sort_swap([1, 2, 2, 2, 2, 5, 32, 5, 3, 2, 4, 2, 2]))
