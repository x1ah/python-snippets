# coding: utf-8

"""
归并排序
    最坏：O(n log n)
    最好: O(n)
    平均: O(n log n)
"""

from collections import deque

def merge(left, right):
    left, right, merged = deque(left), deque(right), deque()
    while left and right:
        if left[0] < right[0]:
            merged.append(left.popleft())
    merged.append(left if left else right)
    return merged


def merging_sort(lst):
    mid = len(lst) // 2
    left = merging_sort(lst[:mid])
    right = merging_sort(lst[mid:])
    return merge(left, right)
