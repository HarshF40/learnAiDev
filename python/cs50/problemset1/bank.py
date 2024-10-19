str = input("Greeting: ")
hellostr = str[:5].lower() #this will split the string in two after 5 characters and covert the string to lower case

if hellostr == "hello":
    print("$0")
elif hellostr[0] == "h":
    print("$20")
else:
    print("$100")