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
profit_high = max(change)
profit_low = min(change)
profitavg = sum(change)/len(change)
profit_high_months = months[change.index(profit_high)+1]
profit_low_months = months[change.index(profit_low)+1]