import csv

with open('avengers.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row['name'])
        print(row['gender'])
        print(row['appearances'])
        print(row['years since joining'])
        print()
    