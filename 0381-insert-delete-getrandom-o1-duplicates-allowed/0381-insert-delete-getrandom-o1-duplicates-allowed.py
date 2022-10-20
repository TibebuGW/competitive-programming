class RandomizedCollection:

    def __init__(self):
        self.d = defaultdict(set)
        self.list = []
        self.last = []
    def insert(self, val: int) -> bool:
        if len(self.d[val]):
            self.list.append(val)
            self.d[val].add(len(self.list)-1)
            self.last = [val, len(self.list)-1]
            return False
        else:
            self.list.append(val)
            self.d[val].add(len(self.list)-1)
            self.last = [val, len(self.list)-1]
            return True

    def remove(self, val: int) -> bool:
        if len(self.d[val]):
            index_of_val = self.d[val].pop()
            # print(index_of_val)
            last_index = self.last[-1]
            # print(last_index)
            # print(self.d[self.last[0]])
            if len(self.d[self.last[0]]) and last_index != index_of_val:
                self.d[self.last[0]].remove(last_index)
            if index_of_val != last_index:
                self.d[self.last[0]].add(index_of_val)
            self.list[last_index], self.list[index_of_val] = self.list[index_of_val], self.list[last_index]
            self.list.pop()
            self.last = [self.list[-1], len(self.list)-1] if len(self.list) else []
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()