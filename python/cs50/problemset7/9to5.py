import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #r'((0?[1-9])|(1[0-2]))(:([0-5][0-9]))?\s(AM|PM)\sto\s((0?[1-9])|(1[0-2]))(:([0-5][0-9]))?\s(AM|PM)'
    match = re.search(r'((0?[1-9])|(1[0-2]))(:([0-5][0-9]))?\s(AM|PM)\sto\s((0?[1-9])|(1[0-2]))(:([0-5][0-9]))?\s(AM|PM)',s)
    # for i in range(match.lastindex+1):
    #     print(match.group(i))
    
    try : 
        if match.group(6) == 'PM' and match.group(1) == '12':
            start_hour = "12"
        elif match.group(6) == 'PM' :
            start_hour = str(int(match.group(1)) + 12).zfill(2)
        elif match.group(6) == 'AM' and match.group(1) == '12' :
            start_hour = "00"
        else :
            start_hour = match.group(1).zfill(2)
            
        if match.group(5) is not None :
            start_min = match.group(5).zfill(2)
        else :
            start_min = '00'
            
#############################################################
            
        if match.group(12) == 'PM' and match.group(7) == '12':
            end_hour = '12'       
        elif match.group(12) == 'PM' :
            end_hour = str(int(match.group(7)) + 12).zfill(2)
        elif match.group(12) == 'AM' and match.group(7) == '12' :
            end_hour = "00"        
        else :
            end_hour = match.group(7).zfill(2)
            
        if match.group(11) is not None :
            end_min = match.group(11).zfill(2)
        else :
            end_min = '00'
    except AttributeError :
     sys.exit("Invalid Format")
    return (start_hour + ":" + start_min + " to " + end_hour + ":" + end_min)

if __name__ == "__main__":
    main()