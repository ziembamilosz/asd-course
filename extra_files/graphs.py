#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Dict


def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:

    adjlist = {key + 1: [] for key in range(len(adjmat))}
    for vertex, values in enumerate(adjmat, start=1):
        for index, value in enumerate(values, start=1):
            if value > 0:
                for _ in range(value):
                    adjlist[vertex].append(index)
    length = len(adjlist)
    for key in range(length):
        if not adjlist[key+1]:
            del adjlist[key+1]
    return adjlist


def dfs_recursive(Graph: Dict[int, List[int]], start: int) -> List[int]:

    visited = []

    def dfs_visit(parent: int) -> None:
        visited.append(parent)
        for vertex in Graph[parent]:
            if vertex not in visited:
                dfs_visit(vertex)

    dfs_visit(start)

    for key in Graph.keys():
        if key not in visited:
            dfs_visit(key)

    return visited


def dfs_iterative(Graph: Dict[int, List[int]], start: int) -> List[int]:

    visited = []
    stack = [start]

    def dfs_visit(stack: List) -> None:
        while stack:
            parent = stack.pop()
            if parent not in visited:
                visited.append(parent)
                for vertex in Graph[parent][::-1]:
                    if vertex not in visited:
                        stack.append(vertex)

    dfs_visit(stack)
    for key in Graph.keys():
        if key not in visited:
            dfs_visit([key])
    return visited


def is_acyclic(G: Dict[int, List[int]]) -> bool:

    def is_cyclic(visited_copy: List[int], current: int) -> bool:

        if current in visited_copy:
            return True

        visited_copy.append(current)
        if current in G.keys():
            for current_neighbour in G[current]:
                if_cyclic = is_cyclic(visited_copy[:], current_neighbour)
                if if_cyclic:
                    return True
            return False

    visited = []

    for node in G.keys():
        visited.append(node)
        for node_neighbour in G[node]:
            is_any_cycle = is_cyclic(visited[:], node_neighbour)
            if is_any_cycle:
                return False
        visited.remove(node)
    return True
