def main():
    _str = input("Greeting: ")
    print(f"${value(_str)}")

def value(_str):
    hellostr = _str[:5].lower() #this will split the string in two after 5 characters and covert the string to lower case

    if hellostr == "hello":
        return 0
    elif hellostr[0] == "h":
        return 20
    else:
        return 100
    
if __name__ == "__main__":
    main()