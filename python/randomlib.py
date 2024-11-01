import random #this imports the whole library and the functions can be only accssed with namespace random
#from random import choice # this imports the choice function from random and can be directly accessed with the namespace

#if import random
# side = random.choice(["heads","tails"])
#print(side)

side = random.choice(["head","tail"])
print(side)

#to get a andom number between 1 and 10
number = random.randint(1,10)
print(number)

#this shuffles the list provided
list = ["one","two","three","four","five","six"]
random.shuffle(list)
print(list)