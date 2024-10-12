name = input("Whats Your Name? ") #input("args") returns the value entered while after printing the passed arguement.
print("Hello, " + name) #we have to manually insert a space to seperate the string, Because by + operator the two string are concatinated.
print("Hello,",name) #we dont have to provide a separate space because we pass multiple arguement and not a single arguement like the above.
print("Hello, ",end="") #thsi will replace the new line which is set by default by the end parameter with the no character
print(name)
print("Hello,",name,sep="???") #over writting the seperation which is by default is a whitespace


###new way to use the variable in the string###
print(f"Hello, {name}") #fstream 
