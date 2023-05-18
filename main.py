import os
import csv

budgetcsv = os.path.join('Resources', 'budget_data.csv')
with open(budgetcsv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    
