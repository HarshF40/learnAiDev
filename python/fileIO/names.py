#name = input("What's your name? ")

#open opens/creates the file specified in the first arguement in the mode specified in the second arguement
#here the file names.txt will be opened in write mode
#open will return a file handle to further access the file
#file = open("names.txt","w") #w -> write
#file = open("names.txt","a") #a -> append
#write will write the name in the file  
#file.write(name + "\n")
#close will close and save the file
#file.close()

#theres another way to open a file in which its not necessary to close the file
#with open("names.txt","a") as file : #opens the file in the append modeS
#    file.write(name + "\n")
    
#opens the file in the read mode
#with open("names.txt","r") as file :
    #reads all the lines in the file 
#    lines = file.readlines() #reads all the lines in the file and stores in the variable lines
#    for line in lines :
#        print(f"Hello, {line.rstrip()}")

#this all can be done in a short way
#with open("names.txt","r") as file:
#    for line in file:
#        print("Hello",line.rstrip()) 

#this will print names in the sorted manner
#with open("names.txt","r") as file :
#    for line in sorted(file) :
#        print("Hello",line.rstrip())

#if you want more control over the file content we can do this way
names = []
with open("names.txt","r") as file :
    for line in sorted(file) :
        names.append(line)