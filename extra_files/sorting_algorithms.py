#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Tuple


def quicksort(lst: List[float]) -> List[float]:

    def quicksort_for_help(modified_lst: List, left_index: int, right_index: int) -> None:
        i = left_index
        j = left_index - 1
        pivot_index = right_index
        while i <= pivot_index:
            if modified_lst[i] <= modified_lst[pivot_index]:
                j += 1
                if modified_lst[i] < modified_lst[j]:
                    modified_lst[i], modified_lst[j] = modified_lst[j], modified_lst[i]
            i += 1

        if left_index < j-1:
            quicksort_for_help(modified_lst, left_index, j-1)
        if j+1 < right_index:
            quicksort_for_help(modified_lst, j+1, right_index)

    copy_lst = lst[:]
    quicksort_for_help(copy_lst, 0, len(copy_lst)-1)
    return copy_lst


def bubblesort(lst: List[float]) -> Tuple[List[float], int]:

    if_changed = False
    nr_of_comparisons = 0
    copy_lst = lst[:]
    n = len(lst)
    while n > 1:
        for i in range(1, n):
            if copy_lst[i-1] > copy_lst[i]:
                copy_lst[i-1], copy_lst[i] = copy_lst[i], copy_lst[i-1]
                if_changed = True
            nr_of_comparisons += 1
        if not if_changed:
            break
        if_changed = False
        n = n - 1

    return copy_lst, nr_of_comparisons
