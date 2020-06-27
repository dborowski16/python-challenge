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

    # Define new lists and set values to zero
    num_mos = 0
    total = 0
    avg_delta = 0
    max_delta = 0
    min_delta = 0
    yr_pl = [] # individual year profit/loss
    yr = [] # month and year
    delta = [] # YoY change

