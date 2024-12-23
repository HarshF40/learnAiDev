def rotations(arr):
    low = 0
    high = len(arr) - 1
    while low != high :
        position = int((low+high)/2)
        print(f"Position: {position}")

        if high < len(arr) - 1 and low > -1 :
            if arr[high - 1] > arr[high] < arr[high + 1]:
                return high
            elif arr[low - 1] > arr[low] < arr[low + 1]:
                return low

        if arr[position - 1] < arr[position] < arr[position + 1]:
            print("Case 1")
            high = position - 1

        elif arr[position - 1] > arr[position] > arr[position + 1]:
            print("Case 2")
            low = position + 1

        elif arr[position - 1] < arr[position] > arr[position + 1]:
            print("Case 3")
            return position + 1

        elif arr[position - 1] > arr[position] < arr[position + 1]:
            return position

def main():
    arr = [ 19, 25, 29, 3, 5, 6, 7, 9, 11, 14 ]
    print(f"Roatations: {rotations(arr)}")

if __name__ == "__main__":
    main()
