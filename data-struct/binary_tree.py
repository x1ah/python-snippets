# coding: utf-8

from collections import deque


class BNode:
    """ 二叉树节点 """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def level_traverse(binary_tree):
    """ 层次遍历二叉树 """
    stack = deque([binary_tree])
    while stack:
        top = stack.popleft()
        print(top.value)
        if top.left:
            stack.append(top.left)
        if top.right:
            stack.append(top.right)


if __name__ == "__main__":
    b_tree = BNode(1, BNode(2, BNode(4, BNode(5, BNode(7)))), BNode(3, BNode(6, right=BNode(8))))
    level_traverse(b_tree)
