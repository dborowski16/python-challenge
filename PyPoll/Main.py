# Import need modules for import csv
import os
import csv

# Define the csv path
thisFolder = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(thisFolder,'Resources', 'election_data.csv')

# Define variables and new lists
total_votes = 0
vote = []   # List to store the candidate name of each voter
cand = []  # List to store the unique candidate name
can_tot = [0, 0, 0, 0]  # Total number of votes by candidate
win_pct = [0, 0, 0, 0]  # Win percentage of the votes by candidate

# Open csv file with comma as delimiter
with open(csvpath) as election_file:
    election = csv.reader(election_file, delimiter = ',')

    # Set header to ignore first row of data
    election_header = next(election)

    # Calculate total votes and create new list with candidate names
    vote = [row[2] for row in election]
    total_votes = len(vote)

    # for loop to create a new list with unique candidate names
    for name in vote:
        if name not in cand:
            cand.append(name)

    # nested for loop to calculate number of votes per candidate
    for i in range(1, (total_votes+1)):
        for j in range(1,len(cand)+1):
            if vote[i-1] == cand[j-1]:
                can_tot[j-1] = can_tot[j-1] + 1

    # for loop to calculate candidate win percentage based upon voter share
    for i in range(1,len(cand)+1):
        win_pct[i-1] = '{:0.003%}'.format(can_tot[i-1]/total_votes)

    #Calculating the winner based upon the greatest win percent
    winner = cand[win_pct.index(max(win_pct))]

# Creating a summary table
print('Election results')
print('-'*30)
print(f'Total Votes: {total_votes}')
print('-'*30)
for i in range(1,len(cand)+1):
    print(f'{cand[i-1]} : {win_pct[i-1]} ({can_tot[i-1]})')
print('-'*30)
print(f'Winner: {winner}')
print('-'*30)


# Adding code in to create a new text file and printing the summary to the text file
afpath = os.path.join(thisFolder, 'Analysis', 'PyPoll Analysis.txt')    # Sets the file path to place the summary in the Analysis folder

f = open(afpath, 'w')
f.write('Election results \n')
f.write('----------------------------- \n')
f.write(f'Total Votes: {total_votes} \n')
f.write('----------------------------- \n')
for i in range(1,len(cand)+1):
    f.write(f'{cand[i-1]} : {win_pct[i-1]} ({can_tot[i-1]}) \n')
f.write('----------------------------- \n')
f.write(f'Winner: {winner} \n')
f.write('----------------------------- \n')
f.close()



