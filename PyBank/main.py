#Setup Workspace to Interact with CSV File Types
import os

import csv

#Locate Specific budget_data file
csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print('Financial Analysis')
    print('----------------------------')
    
    #Ignore Column Headers
    csvheader = next(csvreader)
    
    #Calculate total number of months included in dataset (Determine number of rows in dataset)
    rows = len(list(csvreader))
    print(f"Total Months: {rows}")

    #Calculate net total amount of "Profit/Losses"
    print(f"Total: $")

    #Calculate changes in "Profit/Losses"

    #Calculate average change in "Profit/Losses"
    print(f"Average  Change: $")

    #Find greatest increase in profits
    #Print Date and Amount
    print(f"Greatest Increase in Profits: ")

    #Find greatest decrease in profits
    #Print Date and Amount
    print(f"Greatest Decrease in Profits: ")