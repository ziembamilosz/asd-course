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


listgraph = ListGraph()
for item in polska.polska:
    listgraph.insert_vertex(Vertex(item[2]))

for connection in polska.graf:
    listgraph.insert_edge(Vertex(connection[0]), Vertex(connection[1]))

listgraph.delete_vertex(Vertex('K'))
listgraph.delete_edge(Vertex('W'), Vertex('E'))

#polska.draw_map(listgraph.edges())

lst1 = ['a', 'b']
lst2 = [1, 2]
print(zip(lst1, lst2))
