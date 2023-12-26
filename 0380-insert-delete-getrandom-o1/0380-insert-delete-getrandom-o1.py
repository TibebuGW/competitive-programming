import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        present = val in self.dict
        if not present:
            self.arr.append(val)
            self.dict[val] = len(self.arr) - 1
        return not present

    def remove(self, val: int) -> bool:
        present = val in self.dict
        if present:
            index_to_swap = self.dict[val]
            self.dict[self.arr[-1]] = index_to_swap
            self.arr[index_to_swap], self.arr[-1] = self.arr[-1], self.arr[index_to_swap]
            self.arr.pop()
            del self.dict[val]
        return present

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()