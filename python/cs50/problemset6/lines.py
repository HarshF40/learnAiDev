import sys

def main():
    if len(sys.argv) == 1 :
        sys.exit("Too few command-line arguments!")
    elif len(sys.argv) > 2 :
        sys.exit("Too many command-line arguements!")
        
    extension = sys.argv[1][-2:]
    
    if extension != "py" :
        sys.exit("Not a python file")
        
    try :
        count = 0
        with open(sys.argv[1],"r") as file:
            for line in file:
                code = line.strip()
                if len(code) != 0 : 
                    if code[0] != "#" :
                        count+=1
        print(f"{count}")
    except FileNotFoundError:
        sys.exit("File doesnt exist!")
        
if __name__ == "__main__":
    main()