# Gather information
import csv
import os
import numpy as np

# Identify file and set starting value
count_of_months = 0
file_to_open = os.path.join("PyBank/Resources/budget_data.csv")
file_to_output = os.path.join("PyBank/analysis/budget_analysis.txt")

#Track various financial parameters
total_months = 0
net_change_list = []
total_net = 0
delta = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_open) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")
    # Read the header row
    header = next(reader)
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    
    
# Iterate through the file
    for row in reader:
        # Track the total
        total_months += 1
        total_net += int(row[1])
        
        
        # Identify the change in value
                
        delta = int(row[1]) - prev_net
        net_change_list.append(delta)

        
        # establish that the current month net will become the new previous net for the next loop through the rows
        prev_net = int(row[1])
              
        
# Determine the Greatest Increase and Greatest Decrease
increase = max(net_change_list)
decrease = min(net_change_list)
average = (sum(net_change_list)/len(net_change_list))
avg = (f"{average:.2f}")

# Write Output
output1 = (
    f"Total Months: {total_months}\n" 
    f"----------------------------\n"
    f"Total: {total_net}\n"
    f"Average Change: {avg}\n"
    f"Greatest Increase in Profits: {increase} \n"
    f"Greatest Decrease in Profits: {decrease}\n"
)

# Create the file
with open(file_to_output, "w") as budget_analysis:
    budget_analysis.write(output1)
# Print to screen
print(output1)
