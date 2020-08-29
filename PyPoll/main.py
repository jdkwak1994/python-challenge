# import and path the csv
import os
import csv
path = os.path.join("resources", "election_data.csv")

# reading csv file
with open(path, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # declare lists for candidates
    cand = []
    unique_cand = []

    # skip the header line
    next(csvreader)

    # let's loop the csv
    for row in csvreader:
        
        # add up all candidate into a list
        cand.append(row[2])

        # check for list of candidate, and add them to unique list
        if row[2] not in unique_cand:
            unique_cand.append(row[2])

# find total votes
tvote = len(cand)

# find vote and percentage for each candidate using a list
cand_vote = []
cand_percent = []
for n in range(len(unique_cand)):
    cand_vote.append(cand.count(unique_cand[n]))
    
    percent = round((cand_vote[n] / tvote) * 100, 3)
    cand_percent.append(percent)

# finding winner
win_index = 0
for x in range(len(cand_vote) - 1):
    if cand_vote[x] < cand_vote[x + 1]:
        win_index = x + 1

# printing final value
print(f'Election Result')
print(f'----------------------------')
print(f'Total Votes: {tvote}')
print(f'----------------------------')
for n in range(len(unique_cand)):
    print(f'{unique_cand[n]}: {cand_percent[n]}% ({cand_vote[n]} votes)')
print(f'----------------------------')
print(f'Winner: {unique_cand[win_index]}')
print(f'----------------------------')

# export as text
path = os.path.join("analysis", "election_result.txt")
with open(path, "w") as text:
    text.write(f'Election Result \n')
    text.write(f'---------------------------- \n')
    text.write(f'Total Votes: {tvote} \n')
    text.write(f'---------------------------- \n')
    for n in range(len(unique_cand)):
        text.write(f'{unique_cand[n]}: {cand_percent[n]}% ({cand_vote[n]} votes) \n')
    text.write(f'---------------------------- \n')
    text.write(f'Winner: {unique_cand[win_index]} \n')
    text.write(f'----------------------------')