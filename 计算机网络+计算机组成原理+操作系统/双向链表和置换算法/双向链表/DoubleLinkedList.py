import sys


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        val = "{%s}: {%s}" % (self.key, self.value)
        return val

    def __repr__(self):
        val = "{%s}: {%s}" % (self.key, self.value)
        return val


class DoubleLinkedList:
    def __init__(self, capacity=sys.maxsize):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None

    # 从头部添加节点
    def __add_head(self, node):
        # 如果head为空，也就是双向链表中没有node
        if not self.head:
            self.head = node
            self.tail = node
            self.head.next = None
            self.head.prev = None
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
        self.size += 1
        return node

    # 从尾部添加节点
    def __add_tail(self, node):
        # 如果tail为空，也就是双向链表中没有node
        if not self.tail:
            self.tail = node
            self.head = node
            self.tail.prev = None
            self.tail.next = None
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.next = None
        self.size += 1
        return node

    # 删除尾部节点
    def __del_tail(self):
        # 链表中没有节点
        if not self.tail:
            return

        node = self.tail
        if node.prev:
            self.tail = node.prev
            self.tail.next = None
        else:
            self.tail = self.head = None
        self.size -= 1
        return node

    # 删除头部节点
    def __del_head(self):
        # 链表中没有节点
        if not self.head:
            return

        node = self.head
        if node.next:
            self.head = node.next
            self.head.prev = None
        else:
            self.head = self.tail = None
        self.size -= 1
        return node

    # 删除任一节点
    def  __remove(self, node):
        # 如果为None，默认删除尾部节点
        if not node:
            node = self.tail

        if node == self.tail:
            self.__del_tail()
        elif node == self.head:
            self.__del_head()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        return node

    # 弹出头部节点，删除并返回
    def pop(self):
        return self.__del_head()

    # 添加节点
    def append(self, node):
        return self.__add_tail(node)

    # 往头部添加节点
    def append_front(self, node):
        return self.__add_head(node)

    # 删除节点
    def remove(self, node=None):
        return self.__remove(node)

    # 打印链表
    def print(self):
        p = self.head
        line = ""
        while p:
            line += "%s" % p
            p = p.next
            if p:
                line += " => "
        print(line)


if __name__ == '__main__':
    list = DoubleLinkedList(10)
    nodes = []
    for i in range(10):
        node = Node(i, i)
        nodes.append(node)
    list.append(nodes[0])
    list.print()
    list.append(nodes[1])
    list.print()
    list.pop()
    list.print()
    list.append(nodes[2])
    list.print()
    list.append_front(nodes[3])
    list.print()
    list.append(nodes[4])
    list.print()
    list.remove(nodes[2])
    list.print()
    list.remove()
    list.print()