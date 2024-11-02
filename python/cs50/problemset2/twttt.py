def main():
    text = input("Input : ")
    print(f"{shorten(text)}")

def shorten(str):
    
    i=0
    while i < len(str):
        if str[i] in {'a','e','i','o','u','A','E','I','O','U'}:
            str = str[:i] + str[i+1:]
        i+=1
        
    i=0
    while i < len(str):
        if str[i] in {'a','e','i','o','u','A','E','I','O','U'}:
            str = str[:i] + str[i+1:]
        i+=1

    return str

if __name__ == "__main__":
    main()
