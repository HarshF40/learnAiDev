MAX_HASH_SIZE = 4096

class ProbingHashTable:
    def __init__(self, max_size = MAX_HASH_SIZE):
        self.data_list : list[ tuple[ str, int ] | None ] = [None] * max_size
        self._key_idx = {}

    def insert(self, key, value):
        idx = self._get_valid_index(key)
        if idx > 4095 :
            idx = 0
        if self.data_list[idx] != None :
            start_pt = idx
            while idx+1 != start_pt :
                if idx + 1 > 4095 :
                    idx = 0
                if self.data_list[idx] == None :
                    self.data_list[idx] = key, value
                    break
                else :
                    idx += 1
        else : self.data_list[idx] = key, value
        self._key_idx[key] = idx

    def _get_valid_index(self, key):
        idx = 0
        for char in key :
            idx += ord(char)
        return idx

    def display(self):
        for i in range(len(self.data_list)):
            if self.data_list[i] == None:
                pass
            else :
                print(self.data_list[i], i)

    def find(self, key):
        if key in self._key_idx :
            return self.data_list[self._key_idx[key]], self._key_idx[key]
        else :
            return "No Value for the corresponding key"

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
    print(f"Find: {table.find("arshH")}")
    print(f"Find: {table.find("Harsh")}")
    print(f"Find: {table.find("rhsHa")}")
    print(f"Find: {table.find("rsahH")}")
    print(f"Find: {table.find("AAAAAABBBCCCDDDDEAAAAAABBBCCCDDDDEAAAAAABBBCCCDDDDEddddddi")}")
    print(f"Find: {table.find("AAAAAABBBCCCDDDDEAAAAAABBBCCCDDDDEAAAAAABBBCCCDDDDEddddddi")}")

if __name__ == "__main__":
    main()
