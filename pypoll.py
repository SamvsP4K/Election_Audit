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
counties =[]
county_votes = {}

#winning candiate and county
winner = ""
winner_total_votes = 0
winner_percentage = 0
top_county = ""
top_county_percentage = 0
top_county_votes = 0
line_break = "------------------------\n"
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
        #county calculation
        county_name = row[1]
        if county_name not in county_votes:
            counties.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

    print("County Turnout")
    print(f"The counties counted in this election were:\n",
    counties[0], counties[1],"and", counties[2])
    #print(county_votes)

#writes to txt
with open("election_analysis.txt","w") as txt:
    election_results = (
    f"\nElection Results\n"
    f"------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"------------------------\n")
    print(election_results,end="")

    #saves results to txt file
    txt.write(election_results)
    
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = round(float(votes/total_votes) * 100,1)    
        candidate_results = (f"Candidate {candidate_name} recieved {vote_percentage} % of the vote\n")
        print(candidate_results)
    #saves candidate results to terminal
        txt.write(candidate_results)

    #determines winner and writes to txt file
        if (votes > winner_total_votes) and (vote_percentage>winner_percentage):
            winner_total_votes = votes
            winner_percentage = vote_percentage
            winner = candidate_name
    
    txt.write(line_break)
    #County Calculaton
    print("County Turnout")
    print("-------------------------")
    for county_name in county_votes:
        amount = county_votes[county_name]
        county_percentage = round(float(amount/total_votes) * 100,1)
        county_results = (f"{county_name} recieved {county_percentage}% of the votes\n")

        txt.write(county_results)
        print(county_results)

        if (amount > top_county_votes) and (county_percentage > top_county_percentage):
            top_county_votes = amount
            top_county_percentage = county_percentage
            top_county = county_name
    print(f"The county with the highest voter turnout was {top_county} with {top_county_votes} votes. {top_county_percentage}% of the total votes.")

    top_county_summary = (f"\nThe county with the highest voter turnout was {top_county} with {top_county_votes} votes. {top_county_percentage}% of the total votes.") 
    txt.write(top_county_summary)


    winning_candidate_summary = (f"\n------------------------\n"
    f"Winner: {winner}\nTotal Votes: {winner_total_votes:,}\nWinning Percentage: {winner_percentage}%")
    print(winning_candidate_summary)
    txt.write(winning_candidate_summary)           




   




