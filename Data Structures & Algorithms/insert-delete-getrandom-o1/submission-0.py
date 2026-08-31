class RandomizedSet:

    def __init__(self):
        self.num_set = set()
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.num_set:
            return False
        else:
            self.num_set.add(val)
            self.size += 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.num_set:
            self.num_set.remove(val)
            self.size -= 1
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        idx = random.randint(0, self.size - 1)
        return list(self.num_set)[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()