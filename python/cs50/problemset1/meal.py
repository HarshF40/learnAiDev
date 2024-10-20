def main():
    tm = input("What time it is? ")
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
    hour = int(time[:colon_pos])
    minute = int(time[colon_pos+1:])
    return (hour+(minute/60))

if __name__ == "__main__":
    main()