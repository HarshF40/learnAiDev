def sheep(num):
    for i in range(num):
        yield "*" * i ##yield will return the value without the loop being stopped... s yield will return teh value while the process si going of for eg  -> * -> ** -> *** it will keep returning the values as they are genreated.. returns the value after each iteration

num = int(input("Enter A number: "))
for s in sheep(num):
    print(s)