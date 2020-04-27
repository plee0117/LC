class LRUCache:

    def __init__(self, capacity: int):
        self.item = dict()
        self.order = list()
        self.cap = capacity

    def get(self, key: int) -> int:
        if self.item.get(key):
            self.order.pop(self.order.index(key))
            self.order.insert(0, key)
            return self.item.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.item.get(key):
            self.item[key] = value
            self.order.pop(self.order.index(key))
            self.order.insert(0, key)
        else:
            self.item[key] = value
            self.order.insert(0, key)
            if len(self.order) > self.cap:
                self.item.pop(self.order[-1])
                self.order.pop()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)