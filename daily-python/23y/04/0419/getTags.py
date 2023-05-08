import csv
import pandas as pd

with open(r"23y\04\0419\tags.csv", 'r+', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(csvfile)
    for row in reader:
        print(row)
        writer.writerow([row[0], row[1], row[2], row[3], ''])

# tags = pd.read_csv(r"23y\04\0419\tags.csv", encoding='utf-8')
# print(tags)
