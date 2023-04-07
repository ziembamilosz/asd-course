#!/usr/bin/python
# -*- coding: utf-8 -*-

class NodeAVL:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return f'{self.key}:{self.value} '


class BinarySearchTreeAVL:

    def __init__(self):
        self.root = None

    def __str__(self):
        return self.dfs_string(self.root)

    def dfs_string(self, root):
        # using DFS algorithm to print the tree properly
        if root is None:
            return ''
        return self.dfs_string(root.left) + str(root) + self.dfs_string(root.right)

    def find_node_by_key(self, key, root):
        # receives key and returns node with that key, otherwise None
        if root is None:
            return None
        if key == root.key:
            return root
        if key < root.key:
            return self.find_node_by_key(key, root.left)
        if key > root.key:
            return self.find_node_by_key(key, root.right)

    def search(self, key):
        root = self.find_node_by_key(key, self.root)
        if root is None:
            return None
        return root.value

    def insert(self, key, value):
        self.root = self.insert_recursive(self.root, key, value)

    def insert_recursive(self, root, key, value):
        # looking for proper place to insert
        if root is None:
            root = NodeAVL(key, value)
            root.height = self.height_recursive(root)
        if key < root.key:
            root.left = self.insert_recursive(root.left, key, value)
        elif key > root.key:
            root.right = self.insert_recursive(root.right, key, value)
        else:
            root.value = value

        # balancing the tree
        root.height = self.height_recursive(root)

        balance = self.calculate_balance(root)

        if balance > 1:
            if self.calculate_balance(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        if balance < - 1:
            if self.calculate_balance(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def delete(self, key):
        self.root = self.delete_recursive(key, self.root)

    def delete_recursive(self, key, root):
        # looking for node to delete
        if root is None:
            return root
        elif key < root.key:
            root.left = self.delete_recursive(key, root.left)
        elif key > root.key:
            root.right = self.delete_recursive(key, root.right)
        else:
            # actual deleting the node
            if root.left is None and root.right is None:
                root = None
                return root
            elif root.right is not None and root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.left is not None and root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                temp = self.get_min_value_in_right_subtree(root.right)
                root.key = temp.key
                root.value = temp.value
                root.right = self.delete_recursive(temp.key, root.right)

        if root is None:
            return root

        # balancing the tree
        root.height = self.height_recursive(root)

        balance = self.calculate_balance(root)

        if balance > 1:
            if self.calculate_balance(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        if balance < - 1:
            if self.calculate_balance(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def calculate_balance(self, root):
        if root is None:
            return 0
        return self.get_height_of_node(root.left) - self.get_height_of_node(root.right)

    def get_height_of_node(self, root):
        if root is None:
            return 0
        return root.height

    def rotate_right(self, root):
        left_child = root.left
        temp = left_child.right
        left_child.right = root
        root.left = temp

        root.height = self.height_recursive(root)
        left_child.height = self.height_recursive(left_child)

        return left_child

    def rotate_left(self, root):
        right_child = root.right
        temp = right_child.left
        right_child.left = root
        root.right = temp

        root.height = self.height_recursive(root)
        right_child.height = self.height_recursive(right_child)

        return right_child

    def get_min_value_in_right_subtree(self, root):
        # returns minimal key in the right subtree of a particular node
        if root.left is None:
            return root
        return self.get_min_value_in_right_subtree(root.left)

    def height(self, key=None):
        if key is None:
            key = self.root.key
        return self.height_recursive(self.find_node_by_key(key, self.root))

    def height_recursive(self, root):
        if root is None:
            return 0
        left_height = self.height_recursive(root.left)
        right_height = self.height_recursive(root.right)
        return max(left_height, right_height) + 1

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self._print_tree(node.left, lvl + 5)


bst = BinarySearchTreeAVL()
dct = {50: 'A', 15: 'B', 62: 'C', 5: 'D', 2: 'E', 1: 'F', 11: 'G', 100: 'H', 7: 'I', 6: 'J', 55: 'K',
       52: 'L', 51: 'M', 57: 'N', 8: 'O', 9: 'P', 10: 'R', 99: 'S', 12: 'T'}
for key, value in dct.items():
    bst.insert(key, value)

bst.print_tree()
print(bst)
print(bst.search(10))
bst.delete(50)
bst.delete(52)
bst.delete(11)
bst.delete(57)
bst.delete(1)
bst.delete(12)
bst.insert(3, 'AA')
bst.insert(4, 'BB')
bst.delete(7)
bst.delete(8)
bst.print_tree()
print(bst)
