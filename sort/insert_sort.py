# coding: utf-8

"""
直接插入排序：
    最好：已经有序，O(n)
    最坏：逆序，O(n^2)
    平均: O(n^2)
    稳定排序
"""


def insert_sort(lst):
    length = len(lst)
    for i in range(length):
        j, key = i, lst[i]
        while j > 0 and lst[j-1] > key:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = key
    return lst
