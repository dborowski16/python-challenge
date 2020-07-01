# Import need modules for import csv
import os
import csv

# Define the csv path
thisFolder = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(thisFolder, 'Resources', 'budget_data.csv')
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
    mo_pl = [] # individual month profit/loss
    mo = [] # month and year
    delta = [] # MoM change

    # Running calculations by row while reading the csv
    for row in budget:
        num_mos = num_mos + 1 # Counts the number of months in the budget file
        total = total + int(row[1]) # Adds the current month budget at index = 1 to the running total
        mo_pl.append(row[1]) # appends the current profit/loss value into a list for difference and average calculations
        mo.append(row[0]) # appends the current month into a list for reference for the max/min months
        prev = mo_pl[0] # Assigns the first month profit/loss to prev for difference calculation

    # For loop to calculate the MoM deltas, average delta, and check for max and min MoM change
    for i in range(1,num_mos):
        change = int(mo_pl[i]) - int(prev) # MoM change 
        delta.append(change) # Creates a new list containing the MoM change
        prev = mo_pl[i] # Sets the previous month value to the current month
        avg_delta = avg_delta + change # Calculates total of the MoM changes, to be used to calculate an average MoM later

        # Check to see it the current MoM change is greater than or less than the current values
        if int(delta[i-1]) > max_delta:
            max_delta = delta[i-1]
            max_month = mo[i]

        elif int(delta[i-1]) < min_delta:
            min_delta = delta[i-1]
            min_month = mo[i]

    # calculate average MoM change using the total months, formatted the float to 2 decimal places
    average = '{:.02f}'.format(avg_delta/(num_mos - 1))

# Creating a summary table
print('Financial Analysis')
print('-'*30)
print(f'Total Months: {num_mos}')
print(f'Total : ${total}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {max_month} (${max_delta})')
print(f'Greatest Decrease in Profits: {min_month} (${min_delta})')

# Adding code in to create a new text file and printing the summary to the text file

thisFolder = os.path.dirname(os.path.abspath(__file__))
afpath = os.path.join(thisFolder, 'Analysis', 'PyBank Analysis.txt')    # Sets the file path to place the summary in the Analysis folder

f = open(afpath, 'w')
f.write('Financial Analysis \n')
f.write('----------------------------- \n')
f.write(f'Total Months: {num_mos} \n')
f.write(f'Total : ${total} \n')
f.write(f'Average Change: ${average} \n')
f.write(f'Greatest Increase in Profits: {max_month} (${max_delta}) \n')
f.write(f'Greatest Decrease in Profits: {min_month} (${min_delta}) \n')
f.close()


