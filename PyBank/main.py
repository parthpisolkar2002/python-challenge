# Importing required modules
import os
import csv

# Initializing variables
month_count = 0 # Counts the number of months
tot_pl = 0 # Total profit/loss
difference = {} # Dictionary to store differences between consecutive months
dates = {} # Dictionary to store dates and corresponding profit/loss

# Path to the CSV file
budget_path = os.path.join('PyBank','Resources','budget_data.csv')

# Opening the CSV file
with open(budget_path) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',') # Creating CSV reader
    header = next(budget_data) # Skipping the header
    
    oldpl = None # Initializing old profit/loss to None
    
    # Looping through each row in the CSV file
    for row in budget_data:
        month_count += 1 # Incrementing month count
        date = row[0] # Extracting date
        profit_loss = int(row[1]) # Extracting profit/loss value
        tot_pl += profit_loss # Updating total profit/loss
        
        if oldpl is not None: # Skipping first row
            change = profit_loss - oldpl # Calculating change in profit/loss
            difference[date] = change # Storing change in the dictionary
        
        oldpl = profit_loss # Updating old profit/loss
        dates[date] = profit_loss # Storing profit/loss for each date

# Calculating average change
avg_changes = round(sum(difference.values()) / len(difference), 2) if difference else 0

# Finding date and value for the greatest increase in profits
maxinc_date = max(difference, key=difference.get)
maxinc = difference[maxinc_date]

# Finding date and value for the greatest decrease in profits
maxdec_date = min(difference, key=difference.get)
maxdec = difference[maxdec_date]

# Printing the results
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count} months")
print(f"Total Profit/Loss: ${tot_pl}")
print(f"Average Difference: ${avg_changes}")
print(f"Greatest Increase in Profits: {maxinc_date} (${maxinc})")
print(f"Greatest Decrease in Profits: {maxdec_date} (${maxdec})")

# Write results to a text file
output_file = os.path.join('PyBank','analysis','profit_loss.txt')
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------------------------\n")
    file.write(f"Total Months: {month_count} months\n")
    file.write(f"Total Profit/Loss: ${tot_pl}\n")
    file.write(f"Average Difference: ${avg_changes}\n")
    file.write(f"Greatest Increase in Profits: {maxinc_date} (${maxinc})\n")
    file.write(f"Greatest Decrease in Profits: {maxdec_date} (${maxdec})\n")
