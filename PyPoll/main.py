
#-------------------------START IMPORT CSV------------------------------------

import os
import csv
#create empty list for data
election_data_00 = []

# Full path to the CSV file
csv_file = "c:/Users/craya/Desktop/class_notes/graded_work/module_3_challenge/python-challenge/PyPoll/Resources/election_data.csv"
# Check if the CSV file exists
if os.path.exists(csv_file):
    # Initialize an empty list to store rows
    
    # Open the CSV file and read its contents
    with open(csv_file, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        # Iterate through each row in the CSV file
        for row in csvreader:
            election_data_00.append(row)
    
#-------------------------END IMPORT CSV------------------------------------


#-------------------------START CALC VARIABLES------------------------------------

#initiate empty counter to count ballots
ballot_id_counter = 0
#initiate empty dictionary to get candidates and votes
candidate_counter = {}

for row in election_data_00:
        #count ballots
        ballot_id_counter += 1
        #count votes per candidate
        candidate = row["Candidate"]
        if candidate not in candidate_counter:
             #count first vote
             candidate_counter[candidate] = 1
        else:
            #count add'l votes after first
            candidate_counter[candidate] += 1

    

# Create a list of unique candidates and their counts
unique_candidates = list(candidate_counter.items())

# Display the list of unique candidates, the percentage of votes they received, and their vote counts


#return winner
winner = max(candidate_counter, key=candidate_counter.get)


#-------------------------END CALC VARIABLES------------------------------------
#--------------------------START PRINT SUMMARY TABLE------------------------------------

#number of total months in dataset
print(" ")
print("Election Results")
print("---------------------------")
print(f"Total Votes: {ballot_id_counter}")
print("---------------------------")

for candidate, count in unique_candidates:
    print(f"{candidate}:  {(count/ballot_id_counter)*100:.3f}% ({count})")

print("---------------------------")

print(f"Winner: {winner}")

print("---------------------------")

#--------------------------END PRINT SUMMARY TABLE------------------------------------


#-------------------------START PRINT SUMMARY TABLE TO TEXT FILE------------------------------------


# Set file path
file_path = r"C:\Users\craya\Desktop\class_notes\graded_work\module_3_challenge\python-challenge\PyPoll\Election_Results_Summary.txt"

#Create Print tables
print_table1 = f"""
---------------------------
Election Results
---------------------------
Total Votes: {ballot_id_counter}
---------------------------
"""

print_table2 = f"""
---------------------------
Winner: {winner}
---------------------------
"""

# Write file
with open(file_path, "w") as file:
    #write #Print table1
    file.write(print_table1)
    #repeat logic to write 1 line per candidate
    for candidate, count in unique_candidates:
        file.write(f'{candidate}:  {(count/ballot_id_counter)*100:.3f}% ({count})\n')
    #write #Print table2
    file.write(print_table2)

#-------------------------END PRINT SUMMARY TABLE TO TEXT FILE------------------------------------