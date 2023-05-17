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


class Edge:

    def __init__(self, weight, is_residual):
        self.weight = weight
        self.is_residual = is_residual
        if is_residual:
            self.flow = 0
            self.residual = 0
        else:
            self.flow = 0
            self.residual = weight

    def __repr__(self):
        return f'{self.weight} {self.flow} {self.residual} {self.is_residual}'


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

    def insert_edge(self, vertex1, vertex2, edge):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        i = self.objects_to_indexes[vertex1]
        self.list_of_neighbours[i][vertex2] = edge

    def get_edge(self, vertex_idx1, vertex_idx2):
        return self.list_of_neighbours[vertex_idx1][self.get_vertex(vertex_idx2)]

    def delete_vertex(self, vertex):
        for dct in self.list_of_neighbours:
            if vertex in dct.keys():
                del dct[vertex]
        self.list_of_neighbours.pop(self.objects_to_indexes[vertex])
        self.indexes.remove(vertex)
        del self.objects_to_indexes[vertex]

    def delete_edge(self, vertex1, vertex2):
        i = self.objects_to_indexes[vertex1]
        del self.list_of_neighbours[i][vertex2]

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
            for key, value in self.list_of_neighbours[i].items():
                vertex1 = self.indexes[i]
                vertex2 = key
                vertex1_key = vertex1.get_key()
                vertex2_key = vertex2.get_key()
                result_list.append((vertex1_key, vertex2_key, value))
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


def BFS(G: ListGraph, u):
    parent = [-1 for _ in range(G.order())]
    visited = [u]
    stack = [u]
    while stack:
        item = stack.pop(0)
        neighbours = G.neighbours_idx(item)
        for neighbour, edge in neighbours:
            if neighbour not in visited and edge.residual > 0:
                stack.append(neighbour)
                visited.append(neighbour)
                parent[neighbour] = item
    return parent


def analyzing_path(G, u, v, parent):
    current = v
    min_capacity = float("Inf")
    if parent[current] == -1:
        return 0
    while current != u:
        p = parent[current]
        edge = G.get_edge(p, current)
        if edge.residual < min_capacity:
            min_capacity = edge.residual
        current = p
    return min_capacity


def augmenting_path(G, u, v, parent, min_capacity):
    current = v
    while current != u:
        edge_non_residual = G.get_edge(parent[current], current)
        edge_non_residual.flow += min_capacity
        edge_non_residual.residual -= min_capacity
        edge_residual = G.get_edge(current, parent[current])
        edge_residual.residual += min_capacity
        current = parent[current]


def ford_fulkerson(G, s, t):
    path = BFS(G, s)
    min_capacity = analyzing_path(G, s, t, path)
    while min_capacity > 0:
        augmenting_path(G, s, t, path, min_capacity)
        path = BFS(G, s)
        min_capacity = analyzing_path(G, s, t, path)
    flow_sum = 0
    for neighbour, edge in G.neighbours_idx(t):
        edge = G.get_edge(neighbour, t)
        flow_sum += edge.flow
    return flow_sum


graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]

graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20),
          ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]

graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
          ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]

graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7),
          ('d', 'c', 4)]

g = ListGraph()
for key1, key2, edge in graf_0:
    g.insert_edge(Vertex(key1), Vertex(key2), Edge(edge, False))
    g.insert_edge(Vertex(key2), Vertex(key1), Edge(0, True))
print(ford_fulkerson(g, g.get_vertex_idx(Vertex('s')), g.get_vertex_idx(Vertex('t'))))
print_graph(g)

g = ListGraph()
for key1, key2, edge in graf_1:
    g.insert_edge(Vertex(key1), Vertex(key2), Edge(edge, False))
    g.insert_edge(Vertex(key2), Vertex(key1), Edge(0, True))
g.insert_edge(Vertex('a'), Vertex('c'), Edge(10, False))
print(ford_fulkerson(g, g.get_vertex_idx(Vertex('s')), g.get_vertex_idx(Vertex('t'))))
print_graph(g)

g = ListGraph()
for key1, key2, edge in graf_2:
    g.insert_edge(Vertex(key1), Vertex(key2), Edge(edge, False))
    g.insert_edge(Vertex(key2), Vertex(key1), Edge(0, True))

print(ford_fulkerson(g, g.get_vertex_idx(Vertex('s')), g.get_vertex_idx(Vertex('t'))))
print_graph(g)

g = ListGraph()
for key1, key2, edge in graf_3:
    g.insert_edge(Vertex(key1), Vertex(key2), Edge(edge, False))
    g.insert_edge(Vertex(key2), Vertex(key1), Edge(0, True))
g.insert_edge(Vertex('b'), Vertex('d'), Edge(7, False))
print(ford_fulkerson(g, g.get_vertex_idx(Vertex('s')), g.get_vertex_idx(Vertex('t'))))
print_graph(g)