balance = 0
##by default the global variables only give read permissions to the functions
##so to use the the variable with write access we use gloabal keyword 

def deposit(n):
    global balance
    balance += n
    
def withdraw(n):
    global balance
    balance -= n

def main():
    print(balance)
    deposit(100)
    withdraw(50)
    print(balance)
    
if __name__ == "__main__" :
    main()