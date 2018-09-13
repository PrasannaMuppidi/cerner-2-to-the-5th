# cerner_2^5_2018
# Program to convert a CSV file to a JSON file

import csv,json

csvfile = open('Details_Test.csv', 'r')
jsonfile = open('Details_Test.json', 'w')
fieldnames = ("Benefit Plan","Coverage Begin Date","Deduction Begin Date","Coverage")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')