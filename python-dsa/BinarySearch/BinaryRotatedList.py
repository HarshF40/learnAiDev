def rotations(arr):
    low = 0
    high = len(arr) - 1
    while low<=high :
        mid = (low+high)//2
        print(mid, low, high)

        if mid > 0 and (arr[mid - 1] > arr[mid] or low == high == mid) :
            return mid
        elif (abs(arr[low] - arr[mid]) < abs(arr[high] - arr[mid])) and (arr[low - 1] < arr[low]) :
            low = mid + 1
        else :
            high = mid - 1

    return 0

def main():
    arr = [ 6,7,8,9,1,2,3,4,5 ]
    print(f"Roatations: {rotations(arr)}")

if __name__ == "__main__":
    main()
