# Import the os module
import os

# Import the module for reading CSV
import csv

# Read the data from the CSV file
budget_csv = r"C:\Users\NECEE\python-challenge\python-challenge\PyBank\Resources\budget_data.csv"
total_months = 0
net_total = 0
changes = []
dates = []

# Open and read the CSV file
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

# Process the CSV data and print each row
    prev_profit_loss = 0
    for row in csvreader:
        total_months += 1
        net_total +=int(row[1])
        if prev_profit_loss == 0:
            prev_profit_loss = int(row[1])
        else:
            changes.append(int(row[1])-prev_profit_loss)
            dates.append(row[0])
            prev_profit_loss = int(row[1])

#calculate the average change
average_change= sum(changes)/ len(changes)

#Find greatest increase and decrease in profits
greatest_increase= max(changes)
greatest_decrease= min(changes)

#Find corresponding dates for greatest increase and decrease
increase_date = dates[changes.index(greatest_increase) + 1]
decrease_date = dates[changes.index(greatest_decrease) + 1]

#Print and export results
output = f"""
Financial analysis
--------------------------------------------------------------
Total Months: {total_months}
Total: ${net_total}
Average Changes: ${average_change:.2f}
Greatest Increase in Profits: {increase_date} (${greatest_increase})
Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})
"""
print(output)
with open("financial_analysis.txt", "w") as output_file:
    output_file.write(output)