# Importing packages
import csv
import os

#Setting filepaths
budget_data = os.path.join("budget_data", "/Users/evanreeves/Desktop/ucb-ber-data-pt-06-2020-u-c/02-Homework/03-Python/Python-Challenge/PyBank/Resources/budget_data.csv")
budget_analysis = os.path.join("budget_analysis", "budget_analysis.csv")

months = []
profit = 0
losses = 0
total = []


# Readind in the csv
with open(budget_data) as bd:
    reader = csv.reader(bd)
    header = next(reader)

 

    for row in reader:
        months = months + [row[0]]
        if int(row[1]) > 0:
            profit = profit + int(row[1])
        if int(row[1]) < 0:
            losses = losses + int(row[1])
        total = total + [row[1]]
        if row[1] == max(total):
            max_month = row[0]
        if row[1] == min(total):
            min_month = row[0]
        
        

    month_span = len(months)
    net = profit+losses
    average_change = (net)/len(months)
    max_profit = max(total)   
    max_loss = min(total)

    print("Total months: " + str(month_span))
    print("Net profits/losses: "+ "$"+ str(net))
    print("Average change: " + "$" + str(average_change))
    print("Greatest increase in profits: " + max_month +" : " + str(max_profit))
    print("Greatest decrease in profits: " + min_month +" : " + str(max_loss))
    
    
    
    
    
