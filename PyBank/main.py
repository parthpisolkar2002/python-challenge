import os
import csv

month_count = 0 #initializing the month count
tot_pl = 0 #initializing the total profit loss summing variable
difference = [] #initializing the array which will store the difference betweeen the profits/loss
oldpl = 0 #initializing the variable required to store the p/l value for the previous time period
index1 = 0
index2 = 0

budget_path = os.path.join('python-challenge','PyBank','Resources','budget_data.csv') #importing the csv

with open(budget_path) as csvfile:
    budget_data = csv.reader(csvfile,delimiter=',') #reading the csv
    header = next(budget_data) #skipping the header
    
    for row in budget_data: 
        month_count += 1 #counting months (assuming no months repeat)
        tot_pl += int(row[1]) #summing the total profit for dataset

with open(budget_path) as csvfile:
    budget_data = csv.reader(csvfile,delimiter=',') #re-reading the csv
    header = next(budget_data) #skipping the header
    
    for row in budget_data:
        cur_pl = int(row[1]) #initializing the current profit value at the beg. of 'for' loop
        
        if cur_pl != 0: #skipping the first value
            change = cur_pl - oldpl #calculating change
            difference.append(change) #adding the change to the array

        oldpl = cur_pl #updating the old value of profit loss

    maxinc = max(difference)
    index1 = int(difference.index(maxinc))
    
    maxdec = min(difference)
    index2 = int(difference.index(maxdec))

    difference.pop(0) #removing the first difference as it will equal the first value of the p/l
    avg_changes = round(sum(difference)/len(difference),2) #averaging the values, also rounding to 2 decimals



    print(f"Total Months: {month_count} months") #printing month count
    print(f"Total Profit/Loss: ${tot_pl}") #printing Total Profit/Loss
    print(f"Average Difference: ${avg_changes}") #printing Avg Changes
    print(f"Greatest Increase in Profits:  (${maxinc})")
    print(f"Greatest Decrease in Profits:  (${maxdec})")