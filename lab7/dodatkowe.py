#!/usr/bin/python
# -*- coding: utf-8 -*-
import polska


class Vertex:

    def __init__(self, key):
        self.__key = key

    def __eq__(self, other):
        return self.__key == other.__key

    def __hash__(self):
        return hash(self.__key)

    def __str__(self):
        return f'{self.__key}'

    def get_key(self):
        return self.__key


class MatrixGraph:

    def __init__(self, fill_value=0):
        self.matrix = None
        self.indexes = []
        self.fill_value = fill_value
        self.objects_to_indexes = {}

    def is_empty(self):
        return bool(len(self.indexes) == 0)

    def insert_vertex(self, vertex):
        if self.is_empty():
            self.matrix = [[self.fill_value]]
        else:
            for row in self.matrix:
                row.append(self.fill_value)
            self.matrix.append([self.fill_value]*(len(self.indexes)+1))
        self.objects_to_indexes[vertex] = len(self.indexes)
        self.indexes.append(vertex)

    def insert_edge(self, vertex1, vertex2, edge=1):
        if self.is_empty():
            return
        i = self.objects_to_indexes[vertex1]
        j = self.objects_to_indexes[vertex2]
        self.matrix[i][j] = edge
        self.matrix[j][i] = edge

    def delete_vertex(self, vertex):
        i = self.objects_to_indexes[vertex]
        self.matrix.pop(i)
        for row in self.matrix:
            row.pop(i)
        self.indexes.remove(vertex)
        del self.objects_to_indexes[vertex]

    def delete_edge(self, vertex1, vertex2):
        i = self.objects_to_indexes[vertex1]
        j = self.objects_to_indexes[vertex2]
        self.matrix[i][j] = self.fill_value
        self.matrix[j][i] = self.fill_value

    def get_vertex_idx(self, vertex):
        return self.objects_to_indexes[vertex]

    def get_vertex(self, vertex_idx):
        return self.indexes[vertex_idx]

    def neighbours_idx(self, vertex_idx):
        neighbours_indexes = []
        for index, value in enumerate(self.matrix[vertex_idx]):
            if value != self.fill_value:
                neighbours_indexes.append(index)
        return neighbours_indexes

    def neighbours(self, vertex_idx):
        neighbours_objects = []
        for index, value in enumerate(self.matrix[vertex_idx]):
            if value != self.fill_value:
                neighbours_objects.append(self.indexes[index])
        return neighbours_objects

    def order(self):
        return len(self.indexes)

    def size(self):
        sum_of_edges = 0
        nr_of_items_in_row = 1
        for i in range(len(self.matrix)):
            for j in range(nr_of_items_in_row):
                if self.matrix[i][j] != self.fill_value:
                    sum_of_edges += 1
            nr_of_items_in_row += 1
        return sum_of_edges

    def edges(self):
        result_list = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != self.fill_value:
                    vertex1 = self.indexes[i]
                    vertex2 = self.indexes[j]
                    vertex1_key = vertex1.get_key()
                    vertex2_key = vertex2.get_key()
                    result_list.append((vertex1_key, vertex2_key))
        return result_list

    def get_list_of_vertexes(self):
        return self.indexes


class ListGraph:

    def __init__(self, fill_value=0):
        self.list_of_neighbours = []
        self.fill_value = fill_value
        self.indexes = []
        self.objects_to_indexes = {}

    def is_empty(self):
        return len(self.indexes) == 0

    def insert_vertex(self, vertex):
        self.list_of_neighbours.append({})
        self.objects_to_indexes[vertex] = len(self.indexes)
        self.indexes.append(vertex)

    def insert_edge(self, vertex1, vertex2, edge=1):
        if self.is_empty():
            return
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
        for key in self.list_of_neighbours[vertex_idx].keys():
            neighbours_indexes.append(self.objects_to_indexes[key])
        return neighbours_indexes

    def neighbours(self, vertex_idx):
        neighbours_objects = []
        for key in self.list_of_neighbours[vertex_idx].keys():
            neighbours_objects.append(key)
        return neighbours_objects

    def order(self):
        return len(self.indexes)

    def size(self):
        sum_of_edges = 0
        for dct in self.list_of_neighbours:
            sum_of_edges += len(dct)
        return sum_of_edges//2

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

    def get_list_of_vertexes(self):
        return self.indexes


def paint_graph(graph, dfs_or_bfs):

    if dfs_or_bfs == 0:
        return dfs(graph)
    elif dfs_or_bfs == 1:
        return bfs(graph)


def dfs(graph):

    colours = [-1 for _ in range(graph.size())]
    colours[0] = 0
    stack = [graph.get_vertex(0)]
    visited = [graph.get_vertex(0)]
    while stack:
        parent = stack.pop()
        colours_help = [False for _ in range(graph.size())]
        for vertex in graph.neighbours(graph.get_vertex_idx(parent)):
            if vertex not in visited:
                stack.append(vertex)
                visited.append(vertex)
            index_of_neighbour = graph.get_vertex_idx(vertex)
            if colours[index_of_neighbour] > -1:
                colours_help[colours[index_of_neighbour]] = True
        i = 0
        while colours_help[i]:
            i += 1
        index_of_parent = graph.get_vertex_idx(parent)
        colours[index_of_parent] = i

    return colours


def bfs(graph):

    colours = [-1 for _ in range(graph.size())]
    colours[0] = 0
    stack = [graph.get_vertex(0)]
    visited = [graph.get_vertex(0)]
    while stack:
        parent = stack.pop(0)
        colours_help = [False for _ in range(graph.size())]
        for vertex in graph.neighbours(graph.get_vertex_idx(parent)):
            if vertex not in visited:
                stack.append(vertex)
                visited.append(vertex)
            index_of_vertex = graph.get_vertex_idx(vertex)
            if colours[index_of_vertex] > -1:
                colours_help[colours[index_of_vertex]] = True
        i = 0
        while colours_help[i]:
            i += 1
        index_of_parent = graph.get_vertex_idx(parent)
        colours[index_of_parent] = i

    return colours


# zmiana implementacji wymaga odkomentowania innej linijki
graph = ListGraph()
# graph = MatrixGraph()

for item in polska.polska:
    graph.insert_vertex(Vertex(item[2]))

for connection in polska.graf:
    graph.insert_edge(Vertex(connection[0]), Vertex(connection[1]))

colours = paint_graph(graph, 0)  # 0 jezeli dfs, 1 jezeli bfs
vertexes = graph.get_list_of_vertexes()

polska.draw_map(graph.edges(), [(vertexes[i].get_key(), colours[i]) for i in range(len(vertexes))])
