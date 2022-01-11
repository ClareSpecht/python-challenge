#Setup Workspace to Interact with CSV Mod
import os

import csv

#Locate Specific election_data file
csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Ignore Column Headers
    csvheader = next(csvreader)

    # Initialize variables to store outputs
    Votes = 0
    Candidates = []
    CandVotes = []

    for row in csvreader:
        
        #Calculate total number of votes (Determine number of rows in dataset)
        Votes = Votes + 1

        #Compile List of candidates who received votes
        mycandidate = row[2]
        if mycandidate not in Candidates:
            Candidates.append(mycandidate)
            CandVotes.append(1) #Adds first vote to candidates vote count
        
        #Count up total number of votes each candidate won
        else:
            CandVotes[Candidates.index(mycandidate)] = CandVotes[Candidates.index(mycandidate)] + 1

    #Calculates percentages of votes each candidate won
    percentages = [(round(myvotes/Votes*100, 3)) for myvotes in CandVotes]

#Create results text
str1 = "Election Results"
str2 = "-------------------------"
str3 = (f"Total Votes: {Votes}")

#Index each list to print out all information relevant informatin per candidate
str4 = []
for breakdown in range(len(Candidates)):
    str4.append(f'{Candidates[breakdown]}: {percentages[breakdown]}% ({CandVotes[breakdown]})')

#Determine winner based on who had most votes
Winner = max(CandVotes)
    
str5 = (f"Winner: {Candidates[CandVotes.index(Winner)]}")

Analysis = [str1, str2, str3, str2, *str4, str2, str5, str2]

#Print Analysis to terminal
print(*Analysis, sep=os.linesep)

#Export Analysis to text file
output_path = os.path.join("analysis", "Election Results.txt")
    
with open(output_path, 'w') as txtfile:
    for result in range(len(Analysis)):
        txtfile.write(Analysis[result] + '\n')