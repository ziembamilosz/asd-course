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

    def insert_edge(self, vertex1, vertex2, edge=0):
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
        self.list_of_neighbours.pop(self.objects_to_indexes[vertex])
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

    # zwraca krotki (sasiad, waga)
    def neighbours_idx(self, vertex_idx):
        neighbours_indexes = []
        for key, value in self.list_of_neighbours[vertex_idx].items():
            neighbours_indexes.append((self.objects_to_indexes[key], value))
        return neighbours_indexes

    # zwraca krotki (sasiad, waga)
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
            for key in self.list_of_neighbours[i].keys():
                vertex1 = self.indexes[i]
                vertex2 = key
                vertex1_key = vertex1.get_key()
                vertex2_key = vertex2.get_key()
                result_list.append((vertex1_key, vertex2_key))
        return result_list


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


def primMST(G):
    size = G.order()
    intree = [0 for _ in range(size)]
    distance = [float("inf") for _ in range(size)]
    parent = [-1 for _ in range(size)]

    edges = []

    # result MST graph, currently without any edges
    mst_graph = ListGraph()
    for i in range(G.order()):
        mst_graph.insert_vertex(G.get_vertex(i))

    vertex = 0  # starting vertex
    while intree[vertex] == 0:
        intree[vertex] = 1

        for neighbour, edge in G.neighbours_idx(vertex):
            if edge < distance[neighbour] and intree[neighbour] == 0:
                distance[neighbour] = edge
                parent[neighbour] = vertex

        min_distance = float("inf")
        for v in range(G.order()):
            if intree[v] == 0:
                if distance[v] < min_distance:
                    min_distance = distance[v]
                    vertex = v

        edge_weight = 0
        for neighbour, edge in G.neighbours_idx(parent[vertex]):
            if neighbour == vertex:
                edge_weight = edge
                break

        mst_graph.insert_edge(G.get_vertex(parent[vertex]), G.get_vertex(vertex), edge=edge_weight)
        edges.append(edge_weight)

    return mst_graph, sum(edges[:-1])


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
    G.insert_edge(Vertex(entry[0]), Vertex(entry[1]), entry[2])

prim_graph, sum_of_distances = primMST(G)
print_graph(prim_graph)
