class HashTable:
    def __init__(self):
        self.size = 1
        self.data_list : list[ tuple[str, int | None] | None] = [None] * self.size
        self.used = 0
        self.LOAD_FACTOR = 0.6

    def __setitem__(self, key, value):
        #To update a value
        idx = self.getIndex(key)
        if self.data_list[idx] is not None: 
            if hash(key) == hash(self.data_list[idx][0]) :
                self.data_list[idx] = (key, value)
                return 
        #to insert
        self._checkFactor()
        start_idx = idx
        while self.data_list[idx] != None and self.data_list[idx] != ("__tombstone__", None) :
            idx = (idx + 1) % len(self.data_list)
            if start_idx == idx :
                print("Table is FULL")
                return
        self.data_list[idx] = (key, value)
        self.used += 1

    def __repr__(self):
        return f"{[x for x in self.data_list if x is not None]}"

    def _str__(self):
        return repr(self)

    def __delitem__(self, key):
        #deletion with tombstone
        idx = self.getIndex(key)
        while True :
            if self.data_list[idx] is not None :
                if self.data_list[idx][0] == key :
                    self.data_list[idx] = ("__tombstone__", None)
                    self.used -=1
                    return
            idx = (idx + 1) % self.size

    def getIndex(self, key):
        return hash(key) % self.size

    def resize(self):
        old_data = self.data_list
        self.size *= 2
        self.data_list = [None] * self.size
        self.used = 0
        for data in old_data:
            if data != None and data != ("__tombstone__", None):
                self[data[0]] = data[1]

    def _checkFactor(self):
        if(self.LOAD_FACTOR <= (self.used + 1)/self.size) :
            self.resize()

def main():
    table = HashTable()
    table["Harsh"] = 123
    print(table)
    table["harsH"] = 456
    print(table)
    table["Harsh"] = 999
    print(table)
    table["john"] = 789
    print(table)
    table["doe"] = 112
    print(table)
    del table["doe"]
    table["edo"] = 556
    table["jamal"] = 98798
    print(table)
    del table["jamal"]
    del table["Harsh"]
    print(table)
    table["austen"] = 753
    table["ausnet"] = 2626
    table["qwerty"] = 9929
    print(table)

if __name__ == "__main__" :
    main()
