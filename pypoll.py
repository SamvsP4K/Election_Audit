#Data required:
#1-The total number of votes cast
#2-A complete list of candidates who receieved votes
#3-the percentage of votews each candidate wonm
#4-the total number of votes each candidate won
#5-The winner based on popular vote

import csv 
#file path
file_path = "resources/election_results.csv"

#accumualtors
total_votes = 0
candidate_options = []

#opens file in read mode
with open(file_path, "r") as election_data:
    file_reader = csv.reader(election_data)
    
    #reads header row
    headers = next(file_reader)

    #reads all rows in files
    for row in file_reader:
        #adds total votes
        total_votes +=1
        #adds unique candidate names
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
       
print(candidate_options)
print(total_votes)

#writes to txt
with open("analysis.txt","w") as txt:
    txt.write("Counties in the Elections\n--------------------\nArapahoe\nDenver\nJefferson")
   




