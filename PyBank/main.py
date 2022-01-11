#Setup Workspace to Interact with CSV Mod
import os

import csv

#Locate Specific budget_data file
csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Ignore Column Headers
    csvheader = next(csvreader)

    # Initialize variables to store outputs
    Rows = 0
    Total = 0
    PreviousProfit = 0
    ChangeTotal = 0
    increase = 0
    decrease = 0

    for row in csvreader:

        #Calculate total number of months included in dataset (Determine number of rows in dataset)
        Rows = Rows + 1
        
        #Calculate net total amount of "Profit/Losses"
        MonthlyProfit = int(row[1])
        Total = Total + MonthlyProfit

        #Calculate changes in "Profit/Losses"
        Change = MonthlyProfit - PreviousProfit
        ChangeTotal = ChangeTotal + Change #????Currently just returning profit of final date????

        #Find greatest increase/decrease in profits
        if increase <= Change:
            increase = Change
            BestMonth = row[0]
        elif decrease >= Change:
            decrease = Change
            WorstMonth = row[0]

        #Store profit as PreviousProfit
        PreviousProfit = MonthlyProfit
    
    #Calculate average change in "Profit/Losses"
    AvgChange = round((ChangeTotal / Rows), 2)

#Print Analysis to terminal
Analysis = ['Financial Analysis', '----------------------------', f"Total Months: {Rows}", 
    f"Total: ${Total}", f"Average  Change: ${AvgChange}", 
    f"Greatest Increase in Profits: {BestMonth} (${increase})", f"Greatest Decrease in Profits: {WorstMonth} (${decrease})"]

print(*Analysis, sep=os.linesep)

#Export Analysis to text file
output_path = os.path.join("analysis", "Financial Analysis.txt")
    
with open(output_path, 'w') as txtfile:
    for result in range(len(Analysis)):
        txtfile.write(Analysis[result] + '\n')