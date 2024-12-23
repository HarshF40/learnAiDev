def rotations(arr):
    i = 1

    while i<len(arr) and arr[i-1] < arr[i] :
        i+=1

    if i < len(arr):
        return i
    elif i == len(arr):
        return 0

def main():
    arr = [7, 3, 5]
    print(f"Rotations: {rotations(arr)}")

if __name__ == "__main__":
    main()
