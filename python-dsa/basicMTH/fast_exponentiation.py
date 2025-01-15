def power(x, n):
    ans = 1
    while(n != 0):
        if n % 2 != 0 :
            ans = x * pow(x, n - 1)
        else :
            ans = pow(x**2, n//2)
    return ans

def main():
    print(pow(2,5))

if __name__ == "__main__":
    main()
