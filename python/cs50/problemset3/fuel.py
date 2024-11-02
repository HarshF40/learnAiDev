def convert(fraction):
    while True :
        try:
            if int(fraction[0])<5 and int(fraction[2])<5 and int(fraction[0])<=int(fraction[2]):
                return gauge(int(fraction[0])/int(fraction[2])*100)
            else:
                continue
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        
def gauge(percentage):
     if(percentage == 100):
        return "F"
     elif(percentage == 0):
        return "E"
     else:
        return f"{percentage:.1f}%"
    
        
def main():
    str = input("Input: ")
    print(f"{convert(str)}")
    
if __name__ == "__main__":
    main()