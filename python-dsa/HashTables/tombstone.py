MAX_HASH_SIZE = 10

class HashTable:
    def __init__(self, max_size = MAX_HASH_SIZE):
        self.data_list : list[ tuple[str, int | None] | None ] = [None] * max_size
        self._key_idx = {}

    def __setitem__(self, key, value):
        #To update a value
        if key in self._key_idx:
            self.data_list[self._key_idx[key]] = (key, value)
            print("Value updated successfully")
            return
        #to insert
        print("Inserting new key value pair")
        idx = hash(key) % len(self.data_list)
        start_idx = idx
        while self.data_list[idx] != None and self.data_list[idx] != ("__tombstone__", None) :
            idx = (idx + 1) % len(self.data_list)
            if start_idx == idx :
                print("Table is FULL")
                return
        self.data_list[idx] = (key, value)
        self._key_idx[key] = idx

    def __getitem__(self, key):
        if key in self._key_idx : return self.data_list[self._key_idx[key]]
        else : return "No value for the corresponding key"

    def __repr__(self):
        return f"{[x for x in self.data_list if x is not None]}"

    def _str__(self):
        return repr(self)

    def __delitem__(self, key):
        #deletion with tombstone
        if key in self._key_idx :
            self.data_list[self._key_idx[key]] = ("__tombstone__", None)
            del self._key_idx[key]
        else :
            print("Element Not found")

def main():
    table = HashTable()
    table["Harsh"] = 123
    table["harsH"] = 456
    print(table)
    table["Harsh"] = 999
    print(table)
    print(table["Harsh"])
    print(table["jkjkjk"])
    table["John"] = 778
    table["joe"] = 409
    table["doe"] = 667
    table["edo"] = 4567
    print(table)
    print("-------------------------------------------------------------------")
    del table["Harsh"]
    print(table)
    table["Harsh"] = 123
    print(table)

if __name__ == "__main__" :
    main() 
