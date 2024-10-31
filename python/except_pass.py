#we can pass the except if we use pass keyword in in the except

def get_int(val):
    while True:
        try:
            return int(input(f"{val}: "))
        except ValueError:
            pass
        
def main():
    print(f"Number: {get_int('Input Number')}")
    
main()