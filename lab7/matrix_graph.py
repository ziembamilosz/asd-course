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


matrixgraph = MatrixGraph()
for item in polska.polska:
    matrixgraph.insert_vertex(Vertex(item[2]))

for connection in polska.graf:
    matrixgraph.insert_edge(Vertex(connection[0]), Vertex(connection[1]))

matrixgraph.delete_vertex(Vertex('K'))
matrixgraph.delete_edge(Vertex('W'), Vertex('E'))

polska.draw_map(matrixgraph.edges())
