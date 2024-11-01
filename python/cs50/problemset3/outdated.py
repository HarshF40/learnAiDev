months = {
    "January" : "01",
    "February" : "02",
    "March" : "03",
    "April": "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"
}

def outdated():
    while True:
        try:
            date = input("Date: ")
            if "/" in date :
                month,day,year = date.split("/")
                year = int(year)
                day = int(day)
                month = int(month)
                if 1 <= month <= 12 and 1 <= day <= 31:
                        print(f"{year:04}-{month:02}-{day:02}")
                        break
            elif "," in date :
                month_day , year = date.split(",")
                year = int(year.strip())
                month, day = month_day.split(" ")
                day = int(day)
                month = int(months[month])
                if 1 <= month <= 12 and 1 <= day <= 31:
                        print(f"{year:04}-{month:02}-{day:02}")
                        break
        except (ValueError,KeyError):
            pass
        
def main():
    outdated()
    
main()
