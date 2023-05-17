#!/usr/bin/python
# -*- coding: utf-8 -*-

class Vertex:

    def __init__(self, key):
        self.__key = key

    def __str__(self):
        return f'{self.__key}'

    def __repr__(self):
        return f'{self.__key}'

    def __eq__(self, other):
        return self.__key == other.__key

    def __hash__(self):
        return hash(self.__key)

    def get_key(self):
        return self.__key


class ListGraph:

    def __init__(self, fill_value=0):
        self.list_of_neighbours = []
        self.fill_value = fill_value
        self.indexes = []
        self.objects_to_indexes = {}

    def is_empty(self):
        return len(self.indexes) == 0

    def insert_vertex(self, vertex):
        if vertex in self.indexes:
            return
        self.list_of_neighbours.append({})
        self.objects_to_indexes[vertex] = len(self.indexes)
        self.indexes.append(vertex)

    def insert_edge(self, vertex1, vertex2, edge=0.0):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        i = self.objects_to_indexes[vertex1]
        j = self.objects_to_indexes[vertex2]
        self.list_of_neighbours[i][vertex2] = edge
        self.list_of_neighbours[j][vertex1] = edge

    def delete_vertex(self, vertex):
        for dct in self.list_of_neighbours:
            if vertex in dct.keys():
                del dct[vertex]
        i = self.objects_to_indexes[vertex]
        self.list_of_neighbours.pop(i)
        self.indexes.remove(vertex)
        del self.objects_to_indexes[vertex]

    def delete_edge(self, vertex1, vertex2):
        i = self.objects_to_indexes[vertex1]
        j = self.objects_to_indexes[vertex2]
        del self.list_of_neighbours[i][vertex2]
        del self.list_of_neighbours[j][vertex1]

    def get_vertex_idx(self, vertex):
        return self.objects_to_indexes[vertex]

    def get_vertex(self, vertex_idx):
        return self.indexes[vertex_idx]

    def neighbours_idx(self, vertex_idx):
        neighbours_indexes = []
        for key, value in self.list_of_neighbours[vertex_idx].items():
            neighbours_indexes.append((self.objects_to_indexes[key], value))
        return neighbours_indexes

    def neighbours(self, vertex_idx):
        neighbours_objects = []
        for key, value in self.list_of_neighbours[vertex_idx].items():
            neighbours_objects.append((key, value))
        return neighbours_objects

    def order(self):
        return len(self.indexes)

    def size(self):
        sum_of_edges = 0
        for dct in self.list_of_neighbours:
            sum_of_edges += len(dct)
        return sum_of_edges // 2

    def edges(self):
        result_list = []
        for i in range(len(self.list_of_neighbours)):
            for key, value in self.list_of_neighbours[i].items():
                vertex1 = self.indexes[i]
                vertex2 = key
                vertex1_key = vertex1.get_key()
                vertex2_key = vertex2.get_key()
                result_list.append((vertex1_key, vertex2_key, value))
        return result_list


class Kruskal:

    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [-1 for _ in range(n)]

    def find(self, v):
        if self.parent[v] != v:
            v = self.find(self.parent[v])
        return v

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        if self.size[u] > self.size[v]:
            self.parent[v] = u
            self.size[u] += 1
        else:
            self.parent[u] = v
            self.size[v] += 1

    def same_component(self, s1, s2):
        return self.find(s1) == self.find(s2)


def kruskal_MST(G):
    n = G.order()
    kruskal = Kruskal(n)
    edges = G.edges()
    edges.sort(key=lambda item: item[2])
    result_edges = []
    i = added_elements = 0
    while added_elements < n - 1:
        u, v, weight = edges[i]
        i += 1
        if not kruskal.same_component(u, v):
            added_elements += 1
            kruskal.union(u, v)
            result_edges.append((key_to_char(u), key_to_char(v), weight))
    return result_edges, sum([weight for _, _, weight in result_edges])


def print_graph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.get_vertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours_idx(i)
        for j, w in nbrs:
            print(str(g.get_vertex(j)), w, end=";")
        print()
    print("-------------------")


def char_to_key(item):
    return ord(item) - 65


def key_to_char(item):
    return chr(item + 65)


graf = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
        ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
        ('C', 'G', 9), ('C', 'D', 3),
        ('D', 'G', 10), ('D', 'J', 18),
        ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
        ('F', 'H', 2), ('F', 'G', 8),
        ('G', 'H', 9), ('G', 'J', 8),
        ('H', 'I', 3), ('H', 'J', 9),
        ('I', 'J', 9)
        ]

G = ListGraph()
for entry in graf:
    G.insert_edge(Vertex(char_to_key(entry[0])), Vertex(char_to_key(entry[1])), entry[2])

edges, sum_of_weights = kruskal_MST(G)

result_graph = ListGraph()
for u, v, weight in edges:
    result_graph.insert_edge(Vertex(u), Vertex(v), weight)
print_graph(result_graph)
print(sum_of_weights)