#sys library is used to communicate with the sysytem i guess 
import sys

#we can pass the arguement from the cli(terminal)
#try:
#    print("Hello My Name is",sys.argv[1])
#except IndexError:
#    print("too few arguements")
#argv -> arguement vectot; stores all the arguements 
#0th arguement is the name of the program
#sys.exit() -> exits the code prematurely

if len(sys.argv) < 2 :
    sys.exit("Too few arguements!")

for arg in sys.argv[1:-1] : #the -1 will cut the last aruguement, if -2 then it will cut last two arguements
    print("Hello My Name is",arg)