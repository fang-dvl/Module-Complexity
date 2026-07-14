class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class LruCache:
    def __init__(self,limit):
        if limit <= 0:
            raise ValueError("limit must be > 0")
        self.limit = limit
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next=self.tail
        self.tail.previous=self.head

    def _add_to_head(self,node):
        node.previous=self.head
        node.next=self.head.next
        self.head.next.previous=node
        self.head.next=node


    def _move_to_front(self, node):
        self._remove(node)
        self._add_to_head(node)


    def _remove(self,node):
        node.previous.next=node.next
        node.next.previous=node.previous

    def get(self,key):
        if key not in self.cache:
            return None
        else: 
            node=self.cache[key]
            self._move_to_front(node)
            return self.cache[key].value
  
    def set(self,key,value):
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self._move_to_front(node)
        else:  
            node=Node(key,value)
            self.cache[key]=node
            self._add_to_head(node)
            if len(self.cache) > self.limit:
                lru=self.tail.previous
                self._remove(lru)
                del self.cache[lru.key]