# coding: utf-8

"""
冒泡排序：
    最好：全部有序，O(n)
    最坏：全部逆序，O(n^2)
    稳定排序
"""


def bubble_sort(lst):
    length = len(lst)
    for i in range(length):
        for j in range(length-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
