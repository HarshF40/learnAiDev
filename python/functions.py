#def is used to create or define a function 
#default parameterised function
#functions must be defined before they are used

def hello(arg = "World"):
    print("Hello,",arg)

name = input("Your Name: ")
hello()
hello(name)