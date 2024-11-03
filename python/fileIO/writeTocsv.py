import csv

name = input("Whats your Name? ")
home = input("Whats your Home? ")

with open("writeTocsv.csv","a") as file :
    # writer = csv.writer(file)
    writer = csv.DictWriter(file, fieldnames = ["name" , "home"]) #better than the normal writer... DictWriter directly writes a dictionary, fieldname is the hint that tell in which order those columns are
    writer.writerow({"name" : name , "home" : home}) #writes a row in the .csv file, this order doesnt matter beacuse we have passed fieldnames