def subarr(k):
    arr = [2,1,5,1,3,2]
    current_sum = getSum(arr[0:k])
    max_sum = current_sum
    for i in range(1 ,len(arr)-k+1):
        current_sum = current_sum - arr[i-1] + arr[k + i - 1]
        if current_sum > max_sum :
            max_sum = current_sum
    return max_sum

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
