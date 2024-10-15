#match --> switch of python... no break keyword init
#default :  --> case_:
#to execute for multiple use | as or

str = input("Your Name: ")
match str:
    case "apple" | "banana":
        print("Hello fruit")
    case "tomato":
        print("Hello veggie")
    case _:
        print("who?")
