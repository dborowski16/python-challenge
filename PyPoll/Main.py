# Import need modules for import csv
import os
import csv

# Define the csv path
thisFolder = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(thisFolder,'Resources', 'election_data.csv')
# print(csvpath)

# Open csv file with comma as delimiter
with open(csvpath) as election_file:
    election = csv.reader(election_file, delimiter = ',')

    # Set header to ignore first row of data
    election_header = next(election)
    # print(f'Election Header: {election_header}')

    # Define variables and new lists
    total_votes = 0
    vote = []
    candidate = []
    candidate_total = [0, 0, 0, 0]
    win_percent = [0, 0, 0, 0]
    county = []

    # for loop through rows to calculate total votes and create new list with candidates and counties
    for row in election:
        total_votes = total_votes + 1
        vote.append(row[2])
        county.append(row[1])
    # print(total_votes)
    # print(len(vote))

    # for loop to create a new list with unique candidate names
    for name in vote:
        if name not in candidate:
            candidate.append(name)
    # print(vote[0])
    # print(candidate)

    # for loop to calculate number of votes per candidate
    for i in range(1, (total_votes+1)):
        for j in range(1,len(candidate)+1):
            if vote[i-1] == candidate[j-1]:
                candidate_total[j-1] = candidate_total[j-1] + 1
        
        # if vote[i-1] == candidate[0]:
        #     candidate_total[0] = candidate_total[0] + 1
        # elif vote[i-1] == candidate[1]:
        #     candidate_total[1] = candidate_total[1] + 1  
        # elif vote[i-1] == candidate[2]:
        #     candidate_total[2] = candidate_total[2] + 1
        # elif vote[i-1] == candidate[3]:
        #     candidate_total[3] = candidate_total[3] + 1

    # for loop to calculate candidate win percentage based upon voter share
    for i in range(1,5):
        win_percent[i-1] = '{:0.003%}'.format(candidate_total[i-1]/total_votes)
    # print(win_percent)

    #Calculating the winner based upon the greatest win percent
    winner = candidate[win_percent.index(max(win_percent))]
    # print(winner)

# Creating a summary table
print('Election results')
print('-'*30)
print(f'Total Votes: {total_votes}')
print('-'*30)
print(f'{candidate[0]} : {win_percent[0]} ({candidate_total[0]})')
print(f'{candidate[1]} : {win_percent[1]} ({candidate_total[1]})')
print(f'{candidate[2]} : {win_percent[2]} ({candidate_total[2]})')
print(f'{candidate[3]} : {win_percent[3]} ({candidate_total[3]})')
print('-'*30)
print(f'Winner: {winner}')
print('-'*30)


# Adding code in to create a new text file and printing the summary to the text file
afpath = os.path.join(thisFolder, 'Analysis', 'PyBank Analysis.txt')    # Sets the file path to place the summary in the Analysis folder

f = open(afpath, 'w')
f.write('Election results \n')
f.write('----------------------------- \n')
f.write(f'Total Votes: {total_votes} \n')
f.write('----------------------------- \n')
f.write(f'{candidate[0]} : {win_percent[0]} ({candidate_total[0]}) \n')
f.write(f'{candidate[1]} : {win_percent[1]} ({candidate_total[1]}) \n')
f.write(f'{candidate[2]} : {win_percent[2]} ({candidate_total[2]}) \n')
f.write(f'{candidate[3]} : {win_percent[3]} ({candidate_total[3]}) \n')
f.write('----------------------------- \n')
f.write(f'Winner: {winner} \n')
f.write('----------------------------- \n')
f.close()



