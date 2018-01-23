# coding: utf-8

"""
堆排序
    O(n log n)
"""


def max_heap_adjust(lst, idx, size):
    max_idx = idx
    left = 2 * idx + 1
    right = 2 * (idx + 1)
    if left < size and lst[left] > lst[max_idx]:
        max_idx = left
    if right < size and lst[right] > lst[max_idx]:
        max_idx = right
    if max_idx != idx:
        lst[max_idx], lst[idx] = lst[idx], lst[max_idx]
        max_heap_adjust(lst, max_idx, size)


def build_max_heap(lst, size):
    last_root = int((size - 1) // 2)
    while last_root >= 0:
        max_heap_adjust(lst, last_root, size)
        last_root -= 1


def heap_sort(lst, size):
    build_max_heap(lst, size)
    for i in range(size-1, -1, -1):
        lst[i], lst[0] = lst[0], lst[i]
        max_heap_adjust(lst, 0, i)
