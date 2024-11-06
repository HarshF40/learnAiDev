# special symbols in re.search(pattern,string,ags=0)
# . --> any character except a new line
# * --> 0 or more repitations
# + --> 1 or more repitations
# ? --> 0 or 1 repitations
# {m} --> m repitations
# {m,n} --> m-n repitations

#checking for valid email

import re

email = input("Enter Email: ").strip()

if re.search(r".+@.+\..+",email) :
  print("Valid")
else :
  print("Invalid")