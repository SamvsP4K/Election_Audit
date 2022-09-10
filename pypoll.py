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
candidate_votes = {}

#winning candiate
winner = ""
winner_total_votes = 0
winner_percentage = 0

#opens file in read mode
with open(file_path, "r") as election_data:
    file_reader = csv.reader(election_data)
    
    #reads header row
    headers = next(file_reader)

    #reads all rows in files
    for row in file_reader:
        #adds total votes and tracks vote count
        total_votes +=1
        
        #adds unique candidate names
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1
            
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = round(float(votes/total_votes) * 100,1)    
        print(f"Candidate {candidate_name} recieved {vote_percentage} % of the vote\n")


        #determines winner
        if (votes > winner_total_votes) and (vote_percentage>winner_percentage):
            winner_total_votes = votes
            winner_percentage = vote_percentage
            winner = candidate_name
    print("------------------------------")
    print(f"Winner: {winner}\nTotal Votes: {winner_total_votes:,}\nWinning Percentage: {winner_percentage}%")
            
# print(candidate_options)
# print(total_votes)
# print(candidate_votes)


#writes to txt
with open("analysis.txt","w") as txt:
    txt.write("Counties in the Elections\n--------------------\nArapahoe\nDenver\nJefferson")
   




