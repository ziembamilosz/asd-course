#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.key} {self.value},'


class BinarySearchTree:

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
        if root is None:
            return Node(key, value)
        if key < root.key:
            root.left = self.insert_recursive(root.left, key, value)
        elif key > root.key:
            root.right = self.insert_recursive(root.right, key, value)
        else:
            root.value = value
        return root

    def delete(self, key):
        self.root = self.delete_recursive(key, self.root)

    def delete_recursive(self, key, root):
        if root is None:
            return root
        elif key < root.key:
            root.left = self.delete_recursive(key, root.left)
        elif key > root.key:
            root.right = self.delete_recursive(key, root.right)
        else:
            if root.left is None and root.right is None:  # node doesnt't have child
                root = None
            elif root.right is not None and root.left is None:  # node has only one one right child
                temp = root.right
                return temp
            elif root.left is not None and root.right is None:  # node has only one one left child
                temp = root.left
                return temp
            else:                                                  # node has both children
                temp = self.get_min_value_in_right_subtree(root.right)
                root.key = temp.key
                root.value = temp.value
                root.right = self.delete_recursive(temp.key, root.right)
        return root

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

    def get_min_value_in_right_subtree(self, root):
        if root.left is None:
            return root
        return self.get_min_value_in_right_subtree(root.left)

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


bst = BinarySearchTree()
dct = {50: 'A', 15: 'B', 62: 'C', 5: 'D', 20: 'E', 58: 'F', 91: 'G', 3: 'H', 8: 'I', 37: 'J', 60: 'K', 24: 'L'}
for key, value in dct.items():
    bst.insert(key, value)

bst.print_tree()
print(bst)
print(bst.search(24))
bst.insert(20, 'AA')
bst.insert(6, 'M')
bst.delete(62)
bst.insert(59, 'N')
bst.insert(100, 'P')
bst.delete(8)
bst.delete(15)
bst.insert(55, 'R')
bst.delete(50)
bst.delete(5)
bst.delete(24)
print(bst.height())
print(bst)
bst.print_tree()
