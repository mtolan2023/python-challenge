import os
import csv

#navigate to Resource folder, load csv
budget_csv = os.path.join("Resources", "budget_data.csv")

#set initial values for counters/calculators
total = 0
months = 0
change = 0
lastchange = 0
change_list = []
change_month = []
value = int()
previous = 0

#open csv with reader function
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #chop off the header
    header = next(csv_reader)

    #iterate through rows
    for row in csv_reader:
       #this is the first row and since it has no previous value to compare against, it is treated differently.
       #Previous value is set to zero upon startup so this notices that the previous value is zero.
       if int(row[1]) - previous == int(row[1]):
        #value is set as first value
        value = int(row[1])
        #monthly change is current value - previous month
        change = value - previous
        #After calculation is done, previous adopts value of current month so that it can be referenced the next month.
        previous = value
        #1 month added to the total count
        months +=1
        #Value of row 1 added to total
        total += value


    #now that the first row has been handled, this will apply to the rest of the csv
       elif int(row[1]) - previous != int(row[1]):
          value = int(row[1])
          month = str(row[0])
          #average change is calculated per instance and added to list for averaging calculation.
          change = value - previous
          #Each change calculation is added to the change_list
          change_list.append(change)
          #At the same time, the coresponding month is added to a parallel list that can be referenced once the min/max and average are found.
          change_month.append(month)
          #reset previous value to current month value to be reference next month.
          previous = value
          #Add 1 month to month counter
          months +=1
          #Add current row value to the total
          total += value

    # average monthly change list 
    # Divided by the instances of change (first month is omitted since there is no change)
    average = sum(change_list)/len(change_month)

    # Looking for the Min and Max values in the list of monthly change
    min = min(change_list)
    max = max(change_list)

    #finding the index numbers in the change calculation list to reference against the change_month list
    min_index = change_list.index(min)
    max_index = change_list.index(max)
    #inserting the index numbers above to search for the cooresponding month for max and min changes.
    min_month = change_month[min_index]
    max_month = change_month[max_index]

    #print output according to prompt

    print("Financial Analysis")
    print("------------------------------")
    print(f'Total Months: {months}')
    print(f'Total: ${total}')
    # using {average:.2f} to limit calculation to 2 decimals
    print(f'Average Change: ${average:.2f}')
    print(f'Greatest Increase in Profits: {max_month} (${max})')
    print(f'Greatest Decrease in Profits: {min_month} (${min})')

bank_results = os.path.join("analysis", "bank_results.txt")

# Open text file using "write" mode. Specify the variable to hold the contents
with open(bank_results, 'w') as text_file:
   # printing to text file
   print("Financial Analysis", file=text_file)
   print("------------------------------", file=text_file)
   print(f'Total Months: {months}',file=text_file)
   print(f'Total: ${total}', file=text_file)
#    using {average:.2f} to limit calculation to 2 decimals
   print(f'Average Change: ${average:.2f}', file=text_file)
   print(f'Greatest Increase in Profits: {max_month} (${max})', file=text_file)
   print(f'Greatest Decrease in Profits: {min_month} (${min})', file=text_file)
   

 

    
    


   
        