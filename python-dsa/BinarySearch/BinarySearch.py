def BinarySearch(arr, val):
    low = 0
    high = len(arr) - 1
    while low != high :
        position = int((low + high) / 2)
        if arr[position] == val :
            return position
        elif arr[position] > val :
            low = position + 1
        elif arr[position] < val :
            high = position - 1

def main():
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    val = 10
    print(BinarySearch(arr, val))

if __name__ == "__main__":
    main()
