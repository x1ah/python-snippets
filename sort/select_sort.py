# coding: utf-8

"""
选择排序
    O(n^2)
    稳定
"""


def select_sort(lst):
    length = len(lst)
    for i in range(length):
        min_idx = i
        for j in range(i+1, length):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[min_idx], lst[i] = lst[min_idx], lst[i]
    return lst
