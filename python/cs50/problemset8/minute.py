from datetime import date
from datetime import timedelta
import sys


def main():
    try:
        t1 = date.fromisoformat(input("DOB: "))
    except ValueError :
        sys.exit("Invalid")
    
    t2 = date.today()
    difference = t2-t1
    print(difference.total_seconds()/60)

if __name__ == "__main__":
    main()
