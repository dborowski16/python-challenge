# Import need modules for import csv
import os
import csv

# Define the csv path
thisFolder = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(thisFolder,'Resources', 'election_data.csv')
print(csvpath)

with open(csvpath) as election_file:
    election = csv.reader(election_file, delimiter = ',')

    election_header = next(election)
    # print(f'Election Header: {election_header}')

    total_votes = 0
    candidates = []
    candidate =[]
    candidate_total = []
    county = []

    for row in election:
        total_votes = total_votes + 1
        candidates.append(row[2])
        county.append(row[1])

    for name in candidates:
        if name not in candidate:
            candidate.append(name)
    print(candidate)
             
    # print(candidates)

