def main(): 
    x = int(input("Input a Number: "))
    print("X squared is",square(x))

def square(n):
    return n*n #or n**2 or pow(n,2)

main()