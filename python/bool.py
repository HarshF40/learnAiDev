def main():
    x = int(input("input a number: "))
    if is_even(x):
        print("The number is even!")
    else:
        print("The number is not even")

def is_even(num) :
    if num % 2 == 0:
        return True
    else:
        False

main()