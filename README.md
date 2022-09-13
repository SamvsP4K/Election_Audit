# Full Election Analysis

## Project Overview
Seth and Tom from the Colorado Board of elections have requested a summmary and audit of a rcent local congressional election. 

The following report includes:
    * Total number of cast votes
    * Complete list of candidates and tallied votes
    * Percentage of total won votes for each candidate
    * Election Winner

## Resources
Provided CSV file: election_results.csv
Software used for calculations: VScode, Python v 3.10.5

## Calculation Summary
The CSV provided included 3 columns of data which were "Ballot ID", "County", and "Candidate"
Using python and VScode, the total number of votes were calculated by counting the total number of Ballot IDs.
A list of unique candidate names was created, which was then used to tally a vote for each candidate.
Once each candidate's votes were tallied they were divided by the total number of votes and multiplied by 100 to get the percentage of votes. 
A similar process was done to calculate the voter turnout for each county.

## Election Summary
There was a total number of 369,711 votes cast.

The counties that participated in the election were:
* Jefferson
* Denver
* Arapahoe

Denver had the highest voter turnout with 306,055 votes. Out of all 3 counties, Denver covered 82.8% of the votes.

The candidate options were:
* Charles Casper Stockham
* Diana DeGette
* Raymon Anthony Doane

The results for each candidate were as follows:
Candidate Charles Casper Stockham recieved 23.0 % of the vote
Candidate Diana DeGette recieved 73.8 % of the vote
Candidate Raymon Anthony Doane recieved 3.1 % of the vote

## Based on the results above Diana Degette was the winner with 272,892 total votes which was 73.8% of all votes.

