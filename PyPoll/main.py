import os
import csv

#importing the csv
csvpath = csvpath = os.path.join('Resources', 'election_data.csv')

#setting a variable ahead of time
candidate = []
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #isolating the candidate column
    for row in csvreader:
        candidate.append(row[2])
#total of all votes
votecount = len(candidate)
#determining the names of candidates
candidate_set = set(candidate)
#setting up variables for each candidate's vote count and percent
charles_count = candidate.count("Charles Casper Stockham")
diana_count = candidate.count("Diana DeGette")
raymon_count = candidate.count("Raymon Anthony Doane")
charles_percent = round((charles_count/votecount) * 100, 3)
diana_percent = round((diana_count/votecount) * 100, 3)
raymon_percent = round((raymon_count/votecount) * 100, 3)

#determining the winner of the candidates
winner = []
if charles_count > diana_count & charles_count > raymon_count:
    winner = "Charles Casper Stockham"
elif diana_count > charles_count & diana_count > raymon_percent:
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"

#setting up the analysis
print("Election Results")
print("-----------------------------------")
print("Total Votes: " + str(len(candidate)))
print("------------------------------------------------------------------------")
print("Charles Casper Stockham: " + str(charles_percent) + "% (" + str(charles_count) + ")")
print("Charles Casper Stockham: " + str(diana_percent) + "% (" + str(diana_count) + ")")
print("Charles Casper Stockham: " + str(raymon_percent) + "% (" + str(raymon_count) + ")")
print("------------------------------------")
print("Winner: " + winner)
print("------------------------------------")

#write the results into a csv
output_path = os.path.join("analysis", "results.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    #set up header
    csvwriter.writerow(["Total Votes", "Charles Total", "Charles %", "Diana Total", "Diana %", "Raymon Total", "Raymon %", "Winner"])
    #set up data
    csvwriter.writerow([len(candidate), charles_count, charles_percent, diana_count, diana_percent, raymon_count, raymon_percent, winner])