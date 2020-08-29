# import and path the csv
import os
import csv
path = os.path.join("resources", "budget_data.csv")

# reading csv file
with open(path, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # declare counter variables
    tmonths = 0
    tpl = 0
    gprofit = 0
    gloss = 0

    # skip the header line
    next(csvreader)

    # let's loop the csv
    for row in csvreader:

        # counting months
        tmonths = tmonths + 1

        # adding profit/loss
        tpl = tpl + int(row[1])

        # finding the average change
        avchange = round(tpl / tmonths,2)

        # finding greatest profit and loss
        if gprofit < int(row[1]):
            gprofit_month = str(row[0])
            gprofit = int(row[1])
        
        if gloss > int(row[1]):
            gloss_month = str(row[0])
            gloss = int(row[1])

# printing final value
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {tmonths}')
print(f'Net Total: ${tpl}')
print(f'Average Change: ${avchange}')
print(f'Greatest Gain in Profit: {gprofit_month} (${gprofit})')
print(f'Greatest Loss in Profit: {gloss_month} (${gloss})')

# export as text
path = os.path.join("analysis", "analysis_result.txt")
with open(path, "w") as text:
    text.write(f'Financial Analysis \n')
    text.write(f'---------------------------- \n')
    text.write(f'Total Months: {tmonths} \n')
    text.write(f'Net Total: ${tpl} \n')
    text.write(f'Average Change: ${avchange} \n')
    text.write(f'Greatest Gain in Profit: {gprofit_month} (${gprofit}) \n')
    text.write(f'Greatest Loss in Profit: {gloss_month} (${gloss}) \n')