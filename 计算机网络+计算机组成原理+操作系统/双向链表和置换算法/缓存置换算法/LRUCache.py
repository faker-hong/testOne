from 计算机组成原理实践.双向链表.DoubleLinkedList import Node, DoubleLinkedList


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.list = DoubleLinkedList(self.capacity)

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.list.remove(node)
            self.list.append_front(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            node.value = value
            self.list.append_front(node)
        else:
            node = Node(key, value)
            # 链表缓存已满
            if self.list.size >= self.list.capacity:
                old_node = self.list.remove()
                self.map.pop(old_node.key)

            self.list.append_front(node)
            self.map[key] = node

    def print(self):
        self.list.print()


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.print()
    cache.put(2, 2)
    cache.print()
    print(cache.get(2))
    cache.print()
    cache.put(3, 3)
    cache.print()