#custom module/library

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")
    
def goodbye(name):
    print(f"Hello, {name}")
    
if __name__ == "__main__" : # the main will be only called if the file is called from the command line
    main()