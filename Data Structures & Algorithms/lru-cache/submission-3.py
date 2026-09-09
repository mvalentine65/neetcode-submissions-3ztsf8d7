class Node:
    def __init__(self,key:int, value:int, nxt=None):
        self.value = value  
        self.key = key
        self.next = None
        self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.keys = {}
        self.capacity = capacity
    
    def _remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        
    def _insert(self, node: Node) -> None:
        temp = self.head.next
        node.next = temp
        temp.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        node = self.keys[key]
        self._remove(node)
        self._insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self._remove(self.keys[key])
        node = Node(key, value)
        self._insert(node)
        self.keys[key] = node
        if len(self.keys) > self.capacity:
            unused = self.tail.prev
            self._remove(unused)
            del self.keys[unused.key]