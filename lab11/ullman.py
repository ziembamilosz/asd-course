import copy
import numpy as np


class Vertex:

    def __init__(self, key):
        self.__key = key

    def __repr__(self):
        return f'{self.__key}'

    def __eq__(self, other):
        return self.__key == other.__key

    def __hash__(self):
        return hash(self.__key)

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

    def get_matrix(self):
        return self.matrix

    def insert_vertex(self, vertex):
        if self.is_empty():
            self.matrix = [[self.fill_value]]
        elif vertex in self.indexes:
            return
        else:
            for row in self.matrix:
                row.append(self.fill_value)
            self.matrix.append([self.fill_value] * (len(self.indexes) + 1))
        self.objects_to_indexes[vertex] = len(self.indexes)
        self.indexes.append(vertex)

    def insert_edge(self, vertex1, vertex2, edge):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
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
            if value > self.fill_value:
                neighbours_indexes.append((index, value))
        return neighbours_indexes

    def neighbours(self, vertex_idx):
        neighbours_objects = []
        for index, value in enumerate(self.matrix[vertex_idx]):
            if value > self.fill_value:
                neighbours_objects.append((self.indexes[index], value))
        return neighbours_objects

    def order(self):
        return len(self.indexes)

    def size(self):
        sum_of_edges = 0
        nr_of_items_in_row = 1
        for i in self.matrix:
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


def get_M0_matrix(P, G):
    M0 = np.zeros(shape=(P.shape[0], G.shape[0]))
    for i in range(P.shape[0]):
        nbrs_of_P = sum([j for j in P[i]])
        for j in range(G.shape[0]):
            nbrs_of_G = sum([k for k in G[j]])
            if nbrs_of_P <= nbrs_of_G:
                M0[i, j] = 1
    return M0

def prune(M, P, G):
    M_orig = copy.deepcopy(M)
    was_changed = True
    while was_changed:
        was_changed = False
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if M[i, j] == 1:
                    any_neighbour = False
                    p_neighbours = [index for index, value in enumerate(P[i]) if value == 1]
                    g_neighbours = [index for index, value in enumerate(G[j]) if value == 1]
                    for x in p_neighbours:
                        for y in g_neighbours:
                            if M[x, y] == 1:
                                any_neighbour = True
                                break
                    if not any_neighbour:
                        was_changed = True
                        M[i, j] = 0
                        break
    if (M == M_orig).all():
        return True
    return False

def ullman1(M, P, G, columns, found_isomorphisms=0, nr_of_iterations=0, current_row=0):
    nr_of_iterations += 1
    if current_row == M.shape[0]:
        if (P == np.dot(M, np.dot(M, G).T)).all():
            found_isomorphisms += 1
        return found_isomorphisms, nr_of_iterations
    for current_col in range(len(columns)):
        if not columns[current_col]:
            columns[current_col] = True
            M[current_row, :] = 0
            M[current_row, current_col] = 1
            found_isomorphisms, nr_of_iterations = ullman1(M, P, G, columns, found_isomorphisms, nr_of_iterations, current_row + 1)
            columns[current_col] = False
    return found_isomorphisms, nr_of_iterations


def ullman2(M, P, G, M0, columns, found_isomorphisms=0, nr_of_iterations=0, current_row=0):
    nr_of_iterations += 1
    if current_row == M.shape[0]:
        if (P == np.dot(M, np.dot(M, G).T)).all():
            found_isomorphisms += 1
        return found_isomorphisms, nr_of_iterations
    for current_col in range(len(columns)):
        if not columns[current_col] and M0[current_row, current_col] == 1:
            columns[current_col] = True
            M[current_row, :] = 0
            M[current_row, current_col] = 1
            found_isomorphisms, nr_of_iterations = ullman2(M, P, G, M0, columns, found_isomorphisms, nr_of_iterations, current_row + 1)
            columns[current_col] = False
    return found_isomorphisms, nr_of_iterations


def ullman3(M, P, G, M0, columns, found_isomorphisms=0, nr_of_iterations=0, current_row=0):
    nr_of_iterations += 1
    if current_row == M.shape[0]:
        if (P == M @ (M @ G).T).all():
            found_isomorphisms += 1
        return found_isomorphisms, nr_of_iterations
    M_copy = copy.deepcopy(M)
    is_possible = True
    if current_row == M.shape[0] - 1:
        is_possible = prune(M_copy, P, G)
    for current_col in range(len(columns)):
        if not is_possible and current_row > 0:
            break
        if columns[current_col] ==False and M0[current_row, current_col] == 1:
            columns[current_col] = True
            M_copy[current_row, :] = 0
            M_copy[current_row, current_col] = 1
            found_isomorphisms, nr_of_iterations = ullman3(M_copy, P, G, M0, columns, found_isomorphisms, nr_of_iterations, current_row + 1)
            columns[current_col] = False
    return found_isomorphisms, nr_of_iterations



graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]
g = MatrixGraph()
p = MatrixGraph()
for key1, key2, edge in graph_G:
    g.insert_edge(Vertex(key1), Vertex(key2), edge)
G = np.array(g.get_matrix())
for key1, key2, edge in graph_P:
    p.insert_edge(Vertex(key1), Vertex(key2), edge)
P = np.array(p.get_matrix())
m = np.zeros(shape=(p.order(), g.order()))
print(f'1.0: {ullman1(m.copy(), P, G,                      [False for _ in range(m.shape[1])])}')
print(f'2.0: {ullman2(m.copy(), P, G, get_M0_matrix(P, G), [False for _ in range(m.shape[1])])}')
print(f'3.0: {ullman3(m.copy(), P, G, get_M0_matrix(P, G), [False for _ in range(m.shape[1])])}')
