import math

def compute(n):
    prime = [1] * (n + 1)
    prime[0], prime[1] = -1, -1
    for i in range(2, int(math.sqrt(n)) + 1) :
        if prime[i] == 1 :
            for j in range(i*i, n + 1, i) :
                prime[j] = 0
    return prime


def main():
    n = int(input("Enter the range"))
    prime = compute(n)
    print(prime)

if __name__ == "__main__":
    main()
