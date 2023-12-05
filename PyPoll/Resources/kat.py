# Gather information
import csv
import os
# import numpy as np

# Identify file
file_to_open = "PyPoll/Resources/election_results.csv"
# file_to_output = os.path.join("PyPoll/analysis/analysis1.txt")


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
    # debugging print statement
    # print(header)
    
    # Extract first row
    first_row = next(reader)
    # debugging print statement
    # print(first_row)
    
    total_votes += 1
    # debugging print statement
    # print(total_votes)
    
  
    # Iterate through the file    
    for row in reader:
        # debugging print statement
        # print(row)
        
        # Track the total
        total_votes += 1     
        # summary = sum(voting_data, row[2])
        # print(summary)
        '''kat... when you say if row[2] not in candidate list, python doesn't know what you mean by row[2]... it needs to be declared'''
        row[2]=row[2]
        # print(candidate)
        # Identify the candidates
        if row[2] not in candidate_list:
            candidate_list.append(row[2])            
            candidate_votes += 1
            '''kat your code below is assigning the candidate_name to a print statement... i realize you have it commmented out.. but'''
#             #candidate_name = print(row[2])
            ''' try this instead'''
#             candidate_name = (row[2])
#             print(candidate_name)

#             #candidate_votes = voting_data.count(row[2])
        else:
            candidate_votes += 1
'''your for i in candidate list was inside the for loop... if you want to loop through the candidate list it should be outside the for loop so it would be "ex-dented" (yes... i made that up) so that python can loop through it '''     
# # for i in candidate_list:
# #     while i in candidate_list:
# #         candidate_votes +=1
# #         summary.append(i)
# #         test = row.count(i)
# #         #summary.append(sum(row.count(i) for row in voting_data))
# #         # print(candidate_list + ", " + test)
# print(candidate_list)
#                 # print(test)
# # print(
# #         f'total votes = {total_votes}'


# #     )    

#     # print("total_votes = " + str(total_votes))
#     # print("candidate_list = " + str(candidate_list))
#     # print("candidate_votes = " + str(candidate_votes))
#     # print("summary: " + str(summary))
    
             


# # Create counts for each candidate
 
# #  s.count(x) is the total number of occurrences of x in s


