import csv

with open('res/product.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=';')
    for line_dict in reader:
        old = int(line_dict['Old price'])
        new = int(line_dict['New price'])
        if old > new:
            print(line_dict['Name'])