class Node:

    def __init__(self, suffix):
        self.suffix = suffix
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f'({self.suffix})'

    def __repr__(self):
        return f'({self.suffix})'

class SuffixTree:

    def __init__(self, text):
        self.text = text
        self.root = []
        for i in range(1, len(text)):
            self.insert_suffix(text[i:])

    def insert_suffix(self, word):
        if len(self.root) == 0:
            node = Node(word[0])
            self.root.append(node)
            for i in range(1, len(word)):
                next_node = Node(word[i])
                node.left = next_node
                next_node.parent = node
                node = next_node
        else:
            node_exists = False
            start_node = None
            for node in self.root:
                if node.suffix == word[0]:
                    node_exists = True
                    start_node = node
                    break
            if node_exists:
                node = start_node
                for i in range(len(word)):
                    if node.suffix != word[i]:
                        if node.left is None:
                            node.left = Node(word[i])
                            node.left.parent = node
                        else:
                            node.right = Node(word[i])
                            node.right.parent = node
            else:
                node = Node(word[0])
                self.root.append(node)
                for i in range(1, len(word)):
                    next_node = Node(word[i])
                    node.left = next_node
                    next_node.parent = node
                    node = next_node

print(len("banana\0"))