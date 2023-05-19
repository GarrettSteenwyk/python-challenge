import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

months = []
totalnet = []
avgchange = []
profitup = []
profitdown = []

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


