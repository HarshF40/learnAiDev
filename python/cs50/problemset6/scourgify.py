import csv
import sys

def main():
  if len(sys.argv) < 3 :
    sys.exit("Too few command-line arguements")
  elif len(sys.argv) > 3 :
    sys.exit("Too many command-line arguements")
  
  before_file = sys.argv[1]
  after_file = sys.argv[2]
  
  if before_file != "before.csv" :
    sys.exit(f"Couldn't read {before_file}")
    
  if after_file[-3:] != "csv" :
      sys.exit("Result file is not a csv file!")
  
  
  before_data = []
  with open(before_file,"r") as file :
    reader = csv.DictReader(file)
    for row in reader :
      before_data.append({"name" : row["name"].strip() , "house" : row["house"]})
  
  after_data = []
  with open(after_file,"a") as afile :
    writer = csv.DictWriter(afile,fieldnames = ["name","house"])
    #after_data.append({"name" : "name" , "house" : "house"})
    writer.writeheader()
    for data in before_data[2:] :
      last_name , first_name = data["name"].strip().split(",")
      name = first_name + ", " + last_name
      writer.writerow({"name" : name , "house" : data["house"]})
      
if __name__ == "__main__" :
  main()