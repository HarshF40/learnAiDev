str = input()
words = str.split() #this will split the words in the string and store them in the words
print(*words,sep="...") #this will unpack all the words in the words so that they are passed as an individual arguement
print(words[0]) #this shows that words is an array