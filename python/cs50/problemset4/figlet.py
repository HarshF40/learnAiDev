import random
import sys
from pyfiglet import Figlet

def main():
   figlet = Figlet()
   fList = figlet.getFonts()
   
   if len(sys.argv) == 1 :
       no = random.randint(1,549)
       font = fList[no]
   elif len(sys.argv) == 3 :
       if ((sys.argv[1] == "-f" or sys.argv[1] == "--font" ) and sys.argv[2] in fList):
           font = sys.argv[2]
       else :
           sys.exit("Invalid Usage")
   else :
       sys.exit("Invalid Usage")
       
   string = input("Input: ")
   figlet.setFont(font = font)
   print(figlet.renderText(string))
   
main()