# coding: utf-8

"""
快速排序：
    最好：无序，O(n log n)
    最坏：有序，O(n^2)
    平均：O(n log n)
    不稳定排序
"""


def quick_sort_k(lst):
    if len(lst) <= 1:
        return lst
    key = lst[0]
    left, mid, right = [], [], []
    [{
        i < key: left,
        i == key: mid,
        i > key: right
    }[True].append(i) for i in lst]
    return quick_sort_k(left) + mid + quick_sort_k(right)


def quick_sort(lst, start, stop):
    if start < stop:
        i, j, key = start, stop, lst[start]
        while i < j:
            while i < j and lst[j] >= key:
                j -= 1
            lst[i] = lst[j]
            while i < j and lst[i] < key:
                i +=1
            lst[j] = lst[i]
        lst[i] = key
        quick_sort(lst, start, i-1)
        quick_sort(lst, i+1, stop)
    return lst
