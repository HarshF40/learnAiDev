from validator_collection import checkers

def main():
    string = input("Email: ")
    print(check(string))  # Print the result of the check function
    
def check(s):
    mail = checkers.is_email(s)
    if mail:
        return 'Valid'
    else:
        return 'Invalid'

if __name__ == "__main__":
    main()