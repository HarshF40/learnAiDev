# special symbols in re.search(pattern,string,ags=0)
# . --> any character except a new line
# * --> 0 or more repitations
# + --> 1 or more repitations
# ? --> 0 or 1 repitations
# {m} --> m repitations
# {m,n} --> m-n repitations
# ^ --> match the start of the string
#$ --> match the end of the string
#[] --> set of characters,takes care of .
#[^] --> complementing the set,takes care of .
#\d --> any decimal digit
#\D --> not a Decimal digit
#\s --> whitespace characters
#\S --> not a white space characters
#\w --> word (can also contain number and underscore)
#\w --> not a word

#checking for valid email

import re

email = input("Enter Email: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|net|gov)$",email,re.IGNORECASE) :
  print("Valid")
else :
  print("Invalid")