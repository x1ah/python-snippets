# coding: utf-8


class LNode:
    """ 单链表节点 """

    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_


def reverse_link_list(link_list):
    """ 翻转单链表 """
    if not link_list:
        return
    current = link_list.next_
    link_list.next_ = None
    pre = link_list

    while current:
        _next = current.next_
        current.next_ = pre
        pre = current
        current = _next

    return pre


if __name__ == '__main__':
    link_list = LNode('a', LNode('b', LNode('c', LNode('d', LNode('e')))))
    print("before reverse".center(80, '-'))
    cursor = link_list
    while cursor:
        print(cursor.value)
        cursor = cursor.next_

    print("after reverse".center(80, '-'))
    ret = reverse_link_list(link_list)
    cursor = ret
    while cursor:
        print(cursor.value)
        cursor = cursor.next_
