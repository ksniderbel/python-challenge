# Gather information
import csv
import os
# import numpy as np

# Identify file
file_to_open = "PyPoll\Resources\election_data.csv"
file_to_output = os.path.join("PyPoll/analysis/analysis.txt")

#Create list to hold candidates and declare starting values
candidate_list = []
candidate_dict = {}
total_votes = 0
results = {}

# Read the csv and convert it into a list of dictionaries
with open(file_to_open) as voting_data:
    reader = csv.reader(voting_data, delimiter=",")
    # Read the header row
    header = next(reader)
        
  
    # Iterate through the file    
    for row in reader:
                
        # Track the total
        total_votes += 1     
        

        candidate=row[2]
       # Identify the candidates
        if candidate not in candidate_list:
            candidate_list.append(candidate)          
            candidate_votes = 1
            candidate_dict[candidate] = candidate_votes
        else:
            candidate_dict[candidate] +=1 
        

candidate_sort = sorted(candidate_dict.items(), key=lambda x:x[1])

winner = candidate_sort[-1]
second = candidate_sort[-2]
third = candidate_sort[-3]

for person, total_person_votes in candidate_dict.items():
    print(person)
    print(total_person_votes)
    candidate_percentage = (total_person_votes/total_votes)*100
    candidate_percentage = f"{candidate_percentage:.3f}"
    print(candidate_percentage)
    results.update({person: person, candidate_percentage:candidate_percentage, total_person_votes:total_person_votes})
    print(candidate_dict)
    


# Write Output
output1 = (f"Election Results\n"
    f"--------------------------\n"
    f"Total Votes: {total_votes}\n" 
    f"----------------------------\n"
    f"{results}"
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n"
 )

# # Create the file
with open(file_to_output, "w") as vote_analysis:
     vote_analysis.write(output1)
# # Print to screen
# print(output1)
