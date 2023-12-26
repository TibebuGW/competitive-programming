import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.set = set()
        self.dict = defaultdict(list)

    def insert(self, val: int) -> bool:
        present = val in self.set
        if not present:
            self.set.add(val)
            self.arr.append(val)
            self.dict[val].append(len(self.arr) - 1)
        return not present

    def remove(self, val: int) -> bool:
        present = val in self.set
        if present:
            self.set.remove(val)
            swapped_num = self.arr[-1]
            self.arr[-1], self.arr[self.dict[val][0]] = self.arr[self.dict[val][0]], self.arr[-1]
            swapped_index = self.dict[val].pop()
            self.arr.pop()
            self.dict[swapped_num] = [swapped_index]
        return present

    def getRandom(self) -> int:
        rand_int = random.randint(0, len(self.arr) - 1)
        return self.arr[rand_int]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()