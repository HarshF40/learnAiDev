def main():
    tm = input("What Time it is? ")
    val = convert(tm)

    if val >= 7.0 and val<= 8.0:
        print("Breakfast Time")
    elif val >= 12.0 and val<= 13.0:
        print("Lunch Time")
    elif val >= 18.0 and val <= 19.0:
        print("Dinner Time")
    else:
        print("")

def convert(time):
    colon_pos = time.rfind(":")
    meridiem = time[len(time)-2:]
    hours = float(time[:colon_pos])
    minute = float(time[colon_pos+1:len(time)-3])
    
    if meridiem == "am" and hours == 12.0:
        return 0.0 
    elif meridiem == "pm" and hours == 12.0:
        return 12.0
    elif meridiem == "am":
        return (hours+(minute/60))
    elif meridiem == "pm":
        return (hours(minute/60))+12

if __name__ == "__main__":
    main()