while True:
    try:
        x = int(input("Enter a Number: "))
    except:
        print("Not a Number")
    else:
        print(f"Number is {x}")
        break;

print("Program complete")

#if the try: doesnt give exception the else part will be executed 
#if the try: gives exception then only the except part will executed