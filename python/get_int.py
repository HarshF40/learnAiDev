def get_int():
    while True:
        try:
            return int(input("Input a Number: "))
        except ValueError:
            print("NaN")
            
def main() :
    print(f"Number: {get_int()}")
    
main()