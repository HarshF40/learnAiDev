def subarr(k):
    arr = [2,1,5,1,3,2]
    sum = getSum(arr[0:k])
    for i in range(1 ,len(arr)-k):
        if getSum(arr[i:k+i]) > sum :
            sum = getSum(arr[i:k+i])
    return sum

def getSum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

def main():
    k = int(input("Enter the size of the sub array: "))
    print(subarr(k))

if __name__ == "__main__":
    main()
