import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2 :
        sys.exit("Too few command-line arguements!")
    elif len(sys.argv) > 2 :
        sys.exit("Too many command-line arguements!")
        
    extension = sys.argv[1][-3:]
    
    if extension != "csv" :
        sys.exit("Not a CSV file")
        
    try :
        data =[]
        with open(sys.argv[1],"r") as file :
            reader = csv.DictReader(file)
            for row in file :
                data.append(row)
        print(tabulate(data[1:],headers=data[0],tablefmt='grid'))  #tabulate(table data, table haeders, format)  
    except FileNotFoundError :
        sys.exit("CSV file not found")
        
if __name__ == "__main__":
    main()