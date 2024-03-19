import os
import csv

month_count = 0
tot_pl = 0
difference = []
oldpl = 0

budget_path = os.path.join('Starter_Code','PyBank','Resources','budget_data.csv')

with open(budget_path) as csvfile:
    budget_data = csv.reader(csvfile,delimiter=',')
    header = next(budget_data)
    
    for row in budget_data:
        month_count += 1
        tot_pl += int(row[1])
        cur_pl = int(row[1])

        if cur_pl != 0:
            change = cur_pl - oldpl
            difference.append(change)

        oldpl = cur_pl

    avg_changes = sum(difference)/len(difference)
    
    print(f"Total Months: {month_count} months")
    print(f"Total Profit/Loss: ${tot_pl}")
    print(f"Average Difference: ${avg_changes}")





#

# Method 2: Improved Reading using CSV module

#with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    #csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
        #print(row)