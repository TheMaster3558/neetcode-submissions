from dataclasses import dataclass

@dataclass
class Node:
    key: int
    value: int
    before: Node | None
    after: Node | None

    def __repr__(self):
        return f'(key={self.key} value={self.value} before={self.before.key if self.before else None} after={self.after.key if self.after else None})'

class LRUCache:
    def __init__(self, capacity: int):
        self.keys = {}
        self.head = None
        self.tail = None     
        self.capacity = capacity   

    def move_to_front(self, node: Node):
        if node.before is None:
            assert self.head is node
            return
        assert node.before is not None
        if node.after is None:
            assert self.tail is node
            node.before.after = None
            self.tail = node.before
            node.before = None
            self.head.before = node
            node.after = self.head
            self.head = node
            return
        assert node.before is not None and node.after is not None
        node.before.after = node.after
        node.after.before = node.before
        node.before = None
        self.head.before = node
        node.after = self.head
        self.head = node

    def get(self, key: int) -> int:
        if key in self.keys:
            node = self.keys[key]
            self.move_to_front(node)
            return node.value
            
        return -1

    def print_list(self):
        node = self.head
        while node is not None:
            node = node.after

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.value = value
            self.move_to_front(node)
        else:
            node = Node(key, value, None, self.head)
            if self.head is not None:
                self.head.before = node
            if self.tail is None:
                self.tail = node
            self.head = node
            self.keys[key] = self.head

            if len(self.keys) > self.capacity:
                del self.keys[self.tail.key]
                self.tail.before.after = None
                self.tail = self.tail.before


        




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)