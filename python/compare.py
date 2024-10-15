x = int(input("Enter X: "))
y = int(input("Enter Y: "))

if x > y:
    print("X is greater than Y")
if y > x:
    print("Y is greater than X")
if x == y:
    print("X is equal to Y")

 ### elif ###
if x>y:
    print("X is greater than y")
elif x<y:
    print("X id less than y")
else:
    print("X is equal to Y")

#or keyword

if x>y or x<y :
    print("X is not equal to Y")
else :
    print("X is equal to Y")

if x>2 and y>2:
    print("Both are greater than 2")
else:
    print("Both are not greater than 2")

# if 2<x and x<5 , we can simplify this my combining the two expression
# if 2<x<5