import time

import numpy as np

# a) ------------------------------------------------------------------
def string_compare_recursive(P, T, i, j):
    if i == 0:
        return len(T[:j])
    if j == 0:
        return len(P[:i])
    swaps = string_compare_recursive(P, T, i-1, j-1) + int(P[i] != T[j])
    inserts = string_compare_recursive(P, T, i, j-1) + 1
    deletes = string_compare_recursive(P, T, i-1, j) + 1

    lowest_cost = min(swaps, inserts, deletes)

    return lowest_cost


P = ' kot'
T = ' pies'
r = string_compare_recursive(P, T, len(P)-1, len(T)-1)
print(r)

# b) ---------------------------------------------------------------------------------------------

def string_compare_PD(P, T):
    D = []
    parents = []
    for i in range(len(P)):
        row_D = []
        row_parents = []
        for j in range(len(T)):
            if i == 0 and j == 0:
                row_D.append(j)
                row_parents.append('X')
            elif j == 0:
                row_D.append(i)
                row_parents.append('D')
            elif i == 0:
                row_D.append(j)
                row_parents.append('I')
            else:
                row_D.append(0)
                row_parents.append('X')
        D.append(row_D)
        parents.append(row_parents)

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            swaps = D[i - 1][j - 1] + int(P[i] != T[j])
            inserts = D[i][j - 1] + 1
            deletes = D[i - 1][j] + 1
            lowest_cost = min(swaps, inserts, deletes)
            D[i][j] = lowest_cost
            if lowest_cost == swaps:
                if P[i] == T[j]:
                    parents[i][j] = 'M'
                else:
                    parents[i][j] = 'S'
            elif lowest_cost == inserts:
                parents[i][j] = 'I'
            else:
                 parents[i][j] = 'D'

    return D[len(P) - 1][len(T) - 1], parents

P = ' biały autobus'
T = ' czarny autokar'
r, _ = string_compare_PD(P, T)
print(r)

# c) ----------------------------------------------------------------------------------------------

def path_reconstruction(P, T, parents):
    i = len(P) - 1
    j = len(T) - 1
    path = []
    while parents[i][j] != 'X':
        path.append(parents[i][j])
        if parents[i][j] == 'M' or parents[i][j] == 'S':
            i -= 1
            j -= 1
        elif parents[i][j] == 'D':
            i -= 1
        elif parents[i][j] == 'I':
            j -= 1
    path.reverse()
    return  ''.join(path)

P = ' thou shalt not'
T = ' you should not'
_, parents = string_compare_PD(P, T)
print(path_reconstruction(P, T, parents))


# d) --------------------------------------------------------------------------------------

def matching_patterns(P, T):
    D = []
    parents = []
    for i in range(len(P)):
        row_D = []
        row_parents = []
        for j in range(len(T)):
            if i == 0 and j == 0:
                row_D.append(j)
                row_parents.append('X')
            elif j == 0:
                row_D.append(i)
                row_parents.append('D')
            elif i == 0:
                row_D.append(0)
                row_parents.append('X')
            else:
                row_D.append(0)
                row_parents.append('X')
        D.append(row_D)
        parents.append(row_parents)

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            swaps = D[i - 1][j - 1] + int(P[i] != T[j])
            inserts = D[i][j - 1] + 1
            deletes = D[i - 1][j] + 1
            lowest_cost = min(swaps, inserts, deletes)
            D[i][j] = lowest_cost
            if lowest_cost == swaps:
                if P[i] == T[j]:
                    parents[i][j] = 'M'
                else:
                    parents[i][j] = 'S'
            elif lowest_cost == inserts:
                parents[i][j] = 'I'
            else:
                 parents[i][j] = 'D'
    i = len(P) - 1
    j = 0
    for k in range(1, len(T)):
        if D[i][k] < D[i][j]:
            j = k
    return j - len(P) + 2

P = ' ban'
T = ' mokeyssbanana'
print(matching_patterns(P, T))

# e) ----------------------------------------------------------------------------------------------

def matching_patterns_2(P, T):
    D = []
    parents = []
    for i in range(len(P)):
        row_D = []
        row_parents = []
        for j in range(len(T)):
            if i == 0 and j == 0:
                row_D.append(j)
                row_parents.append('X')
            elif j == 0:
                row_D.append(i)
                row_parents.append('D')
            elif i == 0:
                row_D.append(j)
                row_parents.append('I')
            else:
                row_D.append(0)
                row_parents.append('X')
        D.append(row_D)
        parents.append(row_parents)

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            swaps = D[i - 1][j - 1] + 10000 if P[i] != T[j] else 0
            inserts = D[i][j - 1] + 1
            deletes = D[i - 1][j] + 1
            lowest_cost = min(swaps, inserts, deletes)
            D[i][j] = lowest_cost
            if lowest_cost == swaps:
                if P[i] == T[j]:
                    parents[i][j] = 'M'
                else:
                    parents[i][j] = 'S'
            elif lowest_cost == inserts:
                parents[i][j] = 'I'
            else:
                 parents[i][j] = 'D'

    return D[len(P) - 1][len(T) - 1], parents

def longest_common_sequence(P, T, parents):
    i = len(P) - 1
    j = len(T) - 1
    path = []
    while parents[i][j] != 'X':
        if parents[i][j] == 'M':
            path.append(P[i])
        if parents[i][j] == 'M' or parents[i][j] == 'S':
            i -= 1
            j -= 1
        elif parents[i][j] == 'D':
            i -= 1
        elif parents[i][j] == 'I':
            j -= 1
    path.reverse()
    return  ''.join(path)

P = ' democrat'
T = ' republican'
_, p = matching_patterns_2(P, T)
print(longest_common_sequence(P, T, p))

# f) ------------------------------------------------------------------------------------------------

def longest_common_monotonous_sequence(P, T, parents):
    i = len(P) - 1
    j = len(T) - 1
    path = []
    while parents[i][j] != 'X':
        if parents[i][j] == 'M':
            path.append(P[i])
        if parents[i][j] == 'M' or parents[i][j] == 'S':
            i -= 1
            j -= 1
        elif parents[i][j] == 'D':
            i -= 1
        elif parents[i][j] == 'I':
            j -= 1
    path.reverse()
    return  ''.join(path)


T = ' 243517698'
P = sorted(T)
P = ''.join(P)
_, p = matching_patterns_2(P, T)
print(longest_common_sequence(P, T, p))