def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def mul(a,b):
    return a*b

def main():
    opr = input("Enter + or - or / or *: ")
    x = int(input("Enter a number: "))
    y = int(input("Enter Another number: "))
    match opr:
        case "+" :
            print(f"Ans: {add(x,y)}")
        case "-" :
            print(f"Ans: {sub(x,y)}")
        case "/" :
            print(f"Ans: {div(x,y)}")
        case "*" :
            print(f"Ans: {mul(x,y)}")
        case _:
            print("Invalid")

main()
