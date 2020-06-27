# Import need modules for import csv
import os
import csv

# Define the csv path
csvpath = os.path.join('..','PyBank\Resources', 'budget_data.csv')
print(csvpath)

# Open the csv w/ comma as delimiter
with open(csvpath) as budget_file:
    budget = csv.reader(budget_file, delimiter = ',')

    # Set the budget header to leave out of calculations
    budget_header = next(budget)
    # print(f'Budget Header: {budget_header}')

    # Define new lists and set values to zero
    num_mos = 0
    total = 0
    avg_delta = 0
    max_delta = 0
    min_delta = 0
    yr_pl = [] # individual year profit/loss
    yr = [] # month and year
    delta = [] # YoY change

    # Running calculations by row while reading the csv
    for row in budget:
        num_mos = num_mos + 1 # Counts the number of months in the budget file
        total = total + int(row[1]) # Adds the current month budget at index = 1 to the running total
        yr_pl.append(row[1]) # appends the current profit/loss value into a list for difference and average calculations
        yr.append(row[0]) # appends the current month into a list for reference for the max/min months
        prev = yr_pl[0] # Assigns the first year profit/loss to prev for difference calculation

    print(num_mos)
    print(total)
    print(yr_pl)
    print(prev)


