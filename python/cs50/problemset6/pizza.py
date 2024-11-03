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
        data = []
        with open(sys.argv[1], newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)

        # Convert the data to a formatted table
        headers = data[0]  # The first row is the header
        table = data[1:]   # The remaining rows are the data  #tabulate(table data, table haeders, format)  
        print(tabulate(table, headers=headers, tablefmt='grid'))
    except FileNotFoundError :
        sys.exit("CSV file not found")
        
if __name__ == "__main__":
    main()