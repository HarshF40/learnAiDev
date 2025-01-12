MAX_HASH_TABLE_SIZE = 4096

class BasicHashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        self.data_list: list[ tuple[str, int] | None ] = [None] * max_size

    def insert(self, key, value):
        idx = self.get_index(key)
        self.data_list[idx] = key, value

    def find(self, key):
        idx = self.get_index(key)
        key_value = self.data_list[idx]
        if key_value == None : return "Value not found"
        else : 
            key, value = key_value
            return value

    def get_index(self, key):
        idx = 0 
        for char in key:
            idx += ord(char)
        idx = idx % len(self.data_list)
        return idx

    def list_all(self):
        for values in self.data_list :
            if values == None :
                pass
            else :
                print(values)

def main():
    table = BasicHashTable()
    table.insert("harsh", "1231231234")
    table.list_all()
    print(table.find("harsh"))

    table.insert("rsash", 9879879871)
    table.list_all()
    print(table.find("harsh"))
    print(table.find("rsash"))

if __name__ == "__main__":
    main()
