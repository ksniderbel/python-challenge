# Gather information
import csv
import os
import numpy as np

# Identify file
file_to_open = os.path.join("PyPoll\Resources\election_data.csv")
file_to_output = os.path.join("analysis/election_analysis.txt")


#Create list to hold candidates and declare starting values
candidate_list = []
candidate_votes = 0
summary = []
total_votes = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_open) as voting_data:
    reader = csv.reader(voting_data, delimiter=",")

    # Read the header row
    header = next(reader)
    
    # Extract first row
    first_row = next(reader)
    
    total_votes += 1
    
  
# Iterate through the file    
    for row in reader:
        
        # Track the total
        total_votes += 1
        row[2] = row[2]
        #print(row[2])
        #summary = sum(voting_data, row[2])
        #print(summary)
       
        # Identify the candidates
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_votes += 1
            candidate_name = print(row[2])
            #candidate_votes = voting_data.count(row[2])
        #else:
            #candidate_votes += 1
        
    for i in sorted(candidate_list, key=candidate_list.get):
        print(i)
        #summary.append(count.row in voting_data)
         #   while i in candidate_list:
          #      candidate_votes +=1
           #     summary.append(i)
            #    test = row.count(i)
                #summary.append(sum(row.count(i) for row in voting_data))
              #  print(candidate_list + ", " + test)
            

    print("total_votes = " + str(total_votes))
    print("candidate_list = " + str(candidate_list))
    #print("candidate_votes = " + str(candidate_votes))
    #print("summary: " + str(summary))
    
             


# Create counts for each candidate
 
#  s.count(x) is the total number of occurrences of x in s


