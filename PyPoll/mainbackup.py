# Gather information
import csv
import os
# import numpy as np

# Identify file
file_to_open = "PyPoll\Resources\election_data.csv"
# file_to_output = os.path.join("PyPoll/analysis/analysis1.txt")

#Create list to hold candidates and declare starting values
candidate_list = []
candidate_dict = {}
total_votes = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_open) as voting_data:
    reader = csv.reader(voting_data, delimiter=",")
    # Read the header row
    header = next(reader)
        # debugging print statement
        # print(header)
        
        # Extract first row
    # first_row = next(reader)
    #     # debugging print statement
    # print(first_row)
        
   # total_votes += 1
        # debugging print statement
    #print(total_votes)
    
  
    # Iterate through the file    
    for row in reader:
        # debugging print statement
        # print(row)
        
        # Track the total
        total_votes += 1     
        # summary = sum(voting_data, row[2])
        # print(summary)

        candidate=row[2]
        # print(candidate)
        # Identify the candidates
        if candidate not in candidate_list:
            candidate_list.append(candidate)          
            candidate_votes = 1
            candidate_dict[candidate] = candidate_votes
        else:
            candidate_dict[candidate] +=1 
        
           
print(candidate_dict)   
#''' kat if you sort the dictionary, the winning candidate will be the last item. i helped you with some code to sort it ...'''
# print("first candidate dictionary not sorted: --- ", candidate_dict)
candidate_sort = sorted(candidate_dict.items(), key=lambda x:x[1])
# print("second candidate dictionary sorted: ---" ,candidate_dict)
print(candidate_sort[-1])
print(candidate_sort[-2])
print(candidate_sort[-3])
#kat, over here you can loop through the dictionary and do your calculations for total votes et, assign variables and send it to your analysis file...'''
# do it the python way, loops
#for x in candidate_dict:
#    print(x)
winner = candidate_sort[-1]
second = candidate_sort[-2]
third = candidate_sort[-3]

for person, total_person_votes in candidate_dict.items():
    print(person)
    print(total_person_votes)
    candidate_percentage = (total_person_votes/total_votes)*100
    candidate_percentage = f"{candidate_percentage:.3f}"
    print(candidate_percentage)
    
