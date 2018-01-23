# coding: utf-8

"""
希尔排序（缩小增量排序）
    最好：O(1)
    最坏: O(n^2)
    平均: O(n log n)
    不稳定
"""


def shell_sort(lst):
    length = len(lst)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            key = lst[i]
            j = i
            while j > 0 and lst[j-gap] > key:
                lst[j] = lst[j-gap]
                j -= gap
            lst[j] = key
        gap //= 2
    return lst
