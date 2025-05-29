import random
import time


class RandomizedSet:
    objects: dict[int, int]

    def __init__(self):
        self.objects = {}

    def insert(self, val: int) -> bool:
        if val in self.objects:
            return False
        self.objects[val] = val
        return True

    def remove(self, val: int) -> bool:
        if val not in self.objects:
            return False
        _ = self.objects.pop(val)
        return True

    def getRandom(self) -> int:
        random.seed(time.time())
        index = int(random.random() * 1000000 % len(self.objects))

        keys: list[int] = []
        for k in self.objects.keys():
            keys.append(k)
        return self.objects[keys[index]]
