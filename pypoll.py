#Data required:
#1-The total number of votes cast
#2-A complete list of candidates who receieved votes
#3-the percentage of votews each candidate wonm
#4-the total number of votes each candidate won
#5-The winner based on popular vote

import csv 
#file path
file_path = "resources/election_results.csv"

#opens file in read mode
with open(file_path, "r") as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(headers)



#writes to txt
with open("analysis.txt","w") as txt:
    txt.write("Counties in the Elections\n--------------------\nArapahoe\nDenver\nJefferson")
   




