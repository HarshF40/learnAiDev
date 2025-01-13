MAX_HASH_SIZE = 4096

class ProbingHashTable:
    def __init__(self, max_size = MAX_HASH_SIZE):
        self.data_list : list[ tuple[ str, int ] | None ] = [None] * max_size
        self._key_idx = {}

    def insert(self, key, value):
        idx = self._get_valid_index(key) % len(self.data_list)
        start_idx = idx
        while self.data_list[idx] != None :
            idx = (idx + 1) % len(self.data_list)
            if start_idx == idx :
                print("Table is FULL")
                return 
        self.data_list[idx] = key, value
        self._key_idx[key] = idx

    def _get_valid_index(self, key):
        idx = 0
        for char in key :
            idx += ord(char)
        return idx

    def display(self):
        for i in range(len(self.data_list)):
            if self.data_list[i] != None:
                print(self.data_list[i], i)

    def find(self, key):
        if key in self._key_idx :
            return self.data_list[self._key_idx[key]], self._key_idx[key]
        else :
            return "No Value for the corresponding key"

    def update(self, key, value):
        if key in self._key_idx :
            idx = self._key_idx[key]
            self.data_list[idx] = key, value
        else :
            print("No existing element")

def main():
    table = ProbingHashTable()
    table.insert("Harsh", 1231231234)
    table.insert("rsahH", 980980987)
    table.insert("rhsHa", 4564567898)
    table.insert("arshH", 9999999999)
    table.insert("AAAAAABBBCCCDDDDEAAAAAABBBCCCDDDDEAAAAAABBBCCCDDDDEddddddi", 0000000000)
    table.insert("AAAAAABBBCCCiDDDDEAAAAAABBBCCCDDDDEAAAAAABBBCCCDDDDEdddddd", 111111111)
    table.display()
    print("---------------------------------------------------------------------------------")
    table.update("AAAAAABBBCCCiDDDDEAAAAAABBBCCCDDDDEAAAAAABBBCCCDDDDEdddddd", 5555555555)
    table.update("rhsHa", 3333333333)
    table.display()
    print("---------------------------------------------------------------------------------")
    print(table.find("Harsh"))
    print(table.find("rsahH"))
    print(table.find("rhsHa"))
    print(table.find("AAAAAABBBCCCDDDDEAAAAAABBBCCCDDDDEAAAAAABBBCCCDDDDEddddddi"))
    print(table.find("AAAAAABBBCCCiDDDDEAAAAAABBBCCCDDDDEAAAAAABBBCCCDDDDEdddddd"))

if __name__ == "__main__":
    main()
