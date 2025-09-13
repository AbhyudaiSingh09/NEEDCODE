from typing import List, Any

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                temp = self.cache.pop(i)
                self.cache.append(temp)  # move to end (MRU)
                return temp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                temp = self.cache.pop(i)
                temp[1] = value
                self.cache.append(temp)  # move to end (MRU)
                return
        if self.capacity == len(self.cache):
            self.cache.pop(0)  # evict LRU
        self.cache.append([key, value])

# --- LeetCode-style test harness ---
ops  = ["LRUCache", "put", "get", "put", "put", "get", "get"]
args = [[2],        [1, 10], [1],   [2, 20], [3, 30], [2],   [1]]

obj = None
outputs: List[Any] = []
for op, arg in zip(ops, args):
    if op == "LRUCache":
        obj = LRUCache(*arg)
        outputs.append(None)     # LeetCode prints null for constructor
    elif op == "put":
        outputs.append(obj.put(*arg))
    elif op == "get":
        outputs.append(obj.get(*arg))

print(outputs)  # -> [None, None, 10, None, None, 20, -1]