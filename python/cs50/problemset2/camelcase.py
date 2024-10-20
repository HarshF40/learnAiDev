#obj.isupper() to check if a char is a upper case or a lower case

def main():
    text = input("camelcase: ")
    new = convert(text)
    print(new)

def convert(string):
    snakecase = ""
    for char in string:
        if char.isupper():
            snakecase += "_" + char.lower()
        else :
            snakecase += char
    return snakecase

if __name__ == "__main__":
    main()