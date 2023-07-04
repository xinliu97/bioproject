import csv
import pandas as pd

total_ones = 0
row_num = 0

with open('false_data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        row_num += 1
        total_ones += sum(map(int, row))

        if row_num % 1000 == 0:
            print("每600行的1的总数为:", total_ones)
            total_ones = 0

if row_num % 1000 != 0:
    print("每600行的1的总数为:", total_ones)