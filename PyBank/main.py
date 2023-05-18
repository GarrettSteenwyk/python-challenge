import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
profit = []

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        months.append(row[0])
        profit.append(row[1])

profit = list(map(int, profit))
change = [t - s for s, t in zip(profit, profit[1:])]
max(change)