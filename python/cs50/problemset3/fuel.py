def fuel():
    while True :
        try:
            str = input("Fraction: ")
            if int(str[0])<5 and int(str[2])<5 and int(str[0])<=int(str[2]):
                return int(str[0])/int(str[2])*100
            else:
                continue
        except:
            pass
        
def main():
    val = fuel()
    if(val == 100):
        print("F")
    elif(val == 0):
        print("E")
    else:
        print(f"{val}%")
        
main()