import os
import csv

#importing the csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#setting some variables ahead of time (not sure if this was needed to begin with)
months = []
profit = []
#storing the header row and making the data better to read
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #separating the two columns
    for row in csvreader:
        months.append(row[0])
        profit.append(row[1])

#changing the type of the profit column
profit = list(map(int, profit))
#setting up the variables needed for the analysis below
change = [t - s for s, t in zip(profit, profit[1:])]
profit_high = max(change)
profit_low = min(change)
profitavg = round(sum(change)/len(change), 2)
profit_high_months = months[change.index(profit_high)+1]
profit_low_months = months[change.index(profit_low)+1]

#building the analysis
print("Financial Analysis")
print("-------------------------------------------------")
print("Total Months: " + str(len(months)))
print("Total: $" + str(sum(profit)))
print("Average Change: $" + str(profitavg))
print("Greatest Increase in Profits: " + profit_high_months + " ($" + str(profit_high) + ")")
print("Greatest Decrease in Profits: " + profit_low_months + " ($" + str(profit_low) + ")")

#write the results into a csv
output_path = os.path.join("analysis", "results.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    #set up header
    csvwriter.writerow(["Total Months", "Total", "Average Change", "Greatest Increase Date", "Greatest Increase", "Greatest Decrease Date", "Greatest Decrease"])
    #set up data
    csvwriter.writerow([len(months), sum(profit), profitavg, profit_high_months, profit_high, profit_low_months, profit_low])