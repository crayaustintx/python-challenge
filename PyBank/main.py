

#-------------------------START IMPORT CSV------------------------------------

import os
import csv
#create empty list for data
budget_data_00 = []

# Full path to the CSV file
csv_file = "c:/Users/craya/Desktop/class_notes/graded_work/module_3_challenge/python-challenge/PyBank/Resources/budget_data.csv"

# Check if the CSV file exists
if os.path.exists(csv_file):
    # Initialize an empty list to store rows
    
    # Open the CSV file and read its contents
    with open(csv_file, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        # Iterate through each row in the CSV file
        for row in csvreader:
            budget_data_00.append(row)
    
#-------------------------END IMPORT CSV------------------------------------


#-------------------------START CALC VARIABLES------------------------------------

#initiate empty list and variables to get the number of total (unique) months included in the dataset
date_entry_fill_list=[]
unique_months = 0
#initiate variable to get the net total amount of "Profit/Losses" over the entire period
total_profit_losses = 0
#initiate variable to get the numerator of average change as part of calculating the average change
total_change = 0
#initiate list to store row changes to eventually get min/max
row_changes = []

for row in budget_data_00:
    if row not in date_entry_fill_list:
        #get the number of momths included in the dataset
        unique_months += 1
        date_entry_fill_list.append(row)
        #get total amount of "Profit/Losses" over the entire period
        total_profit_losses += int(row['Profit/Losses'])

#get the numerator of average change as part of calculating the average change
for i in range(1,len(budget_data_00)):
    #get current record and prior record, find difference, cumulate difference
    current_profit_losses = int(budget_data_00[i]['Profit/Losses'])
    prior_profit_losses = int(budget_data_00[i-1]['Profit/Losses'])
    row_change = current_profit_losses - prior_profit_losses
    total_change += row_change
    # Store row changes along with the date of the current record
    row_changes.append({'Date': budget_data_00[i]['Date'], 'change': row_change})


#run through row change list to get max / min change in Profit/Losses 
min_row_change = row_changes[0]
max_row_change = row_changes[0]

for change in row_changes:
    if change['change'] < min_row_change['change']:
        min_row_change = change
    if change['change'] > max_row_change['change']:
        max_row_change = change

#-------------------------END CALC VARIABLES------------------------------------


#-------------------------START PRINT SUMMARY TABLE TO TERMINAL------------------------------------

#number of total months in dataset
print(" ")
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {unique_months}")
print(f"Total: ${total_profit_losses}")
#get average change
average_change = round(total_change/(unique_months-1),2)
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_row_change['Date']} (${max_row_change['change']})")
print(f"Greatest Decrease in Profits: {min_row_change['Date']} (${min_row_change['change']})")


#-------------------------END PRINT SUMMARY TABLE TO TERMINAL------------------------------------

#-------------------------START PRINT SUMMARY TABLE TO TEXT FILE------------------------------------


# Set file path
file_path = r"C:\Users\craya\Desktop\class_notes\graded_work\module_3_challenge\python-challenge\PyBank\financial_analylsis_summary.txt"

#Print table
print_table = f"""
Financial Analysis
---------------------------
Total Months: {unique_months}
Total: ${total_profit_losses}
Average Change: ${average_change}
Greatest Increase in Profits: {max_row_change['Date']} (${max_row_change['change']})
Greatest Decrease in Profits: {min_row_change['Date']} (${min_row_change['change']})

"""

# Write file
with open(file_path, "w") as file:
    file.write(print_table)


#-------------------------END PRINT SUMMARY TABLE TO TEXT FILE------------------------------------