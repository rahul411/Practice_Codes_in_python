class hashTable:
    table = [[] for i in range(256)]

    def getValue(self, val):
        print(hash(val))
        return hash(val) % 256

    def insertValue(self, val):
        key = self.getValue(val)
        print(key)
        self.table[key].append(val)

    def deleteValue(self, val):
        key = self.getValue(val)
        if val in self.table[key]:
            del self.table[key][self.table[key].index(val)]

    def lookup(self, val):
        key = self.getValue(val)
        if key in self.table and val in self.table[key]:
            return self.table[key]


a = hashTable()
a.insertValue(2)
a.insertValue(3)
a.insertValue("asd")
a.insertValue(19)
a.insertValue(259)
a.deleteValue(259)
print(a.lookup(1))
print(a.table)
print(a.getValue(1))
