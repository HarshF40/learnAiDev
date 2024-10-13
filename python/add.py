x = int(input("Enter a Number: ")) 
y = int(input("Enter a number: "))

#above statements take value as a string

#z = int(x) + int(y) #this converts the string value to intergers

#we can format the numbers too
print(f"{x+y : ,}") #f before the double quotes makes the string format string

a = float(input("Enter a Float value: "))
b = float(input("Enter a Float value: "))
print(a+b)

#rounded value (we can round of the value using round() function)
print(round(a+b))
print(round(a+b,2)) #rounds till the two decimals positions
#the above ones can be done with fstream too
print(f"{a+b :.2f}")