expression = input("Expression: ")

whitespaces = []

for i,char in enumerate(expression):
    if char == " ":
        whitespaces.append(i)

ptr0 = 0 #this points the first element of the expression
ptr1 = whitespaces[0] #this points to the first whitesapce in the expression
ans = float(expression[ptr0:ptr1]) #this will have thve value of the first value

ptr1+=1
if expression[ptr1] == "+":
    ans+=float(expression[ptr1+2:])
if expression[ptr1] == "-":
    ans-=float(expression[ptr1+2:])
if expression[ptr1] == "/":
    ans/=float(expression[ptr1+2:])
if expression[ptr1] == "*":
    ans*=float(expression[ptr1+2:])

print(ans)