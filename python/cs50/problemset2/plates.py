def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (len(s) > 6) or len(s)<2 or not (s[0].isalpha() and s[1].isalpha()):
        return False
    for i in range (len(s)-1):
        if s[i].isdigit() and s[i+1].isalpha() or not s[i].isalnum() or (s[i].isalpha() and s[i+1] == "0"):
            return False
    return True        
  
if __name__ == "__main__":  
    main()
