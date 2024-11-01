import inflect

def main():
    p = inflect.engine()
    name = []
    while True:
        try:
            name.append(input("Name: "))
        except EOFError:
            string = p.join((name),final_sep="")
            print("Adieu, adieu, to",string)
            break
        
main()