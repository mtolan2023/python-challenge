import os
import csv

#find csv file in project folder
poll_csv = os.path.join("Resources", "election_data.csv")

#set variables
can_set = set()
canlist = []
can1name = str()
can2name = str()
can3name = str()
winner = ""
can1 = 0
can2 = 0
can3 = 0
can1percent = float
can2percent = float
can3percent = float


#reading csv to extract candidate names
with open(poll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #cut off header
    header = next(csv_reader)

    #read as set first to filter unique values and add to list
    for row in csv_reader:
        if row[2] not in can_set:
            can_set.add(row[2])
            canlist.append(row[2])
   
    #naming candidates from list index
    can1name = canlist[0]
    can2name = canlist[1]
    can3name = canlist[2]

#opening second instance of reader to seach candidate names against rows 
with open(poll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #cutting off header
    header = next(csv_reader)
    #iterate through rows to tally vote counts per candidate
    for row in csv_reader:
        if row[2] == can1name:
            can1 += 1
        elif row[2] == can2name:
            can2 += 1
        elif row[2] == can3name:
            can3 += 1
        elif row[2] != can1name and row[2] != can2name and row[2] != can3name:
            print(f'There are more than three candidates, please reconfigure.')


    #tallying total votes by adding individual candidate quantities
    totalvote = can1 + can2 + can3

    #determininig winner
    if can1 > can2 and can1 > can3:
        winner = can1name
    elif can2 > can1 and can2 > can3:
        winner = can2name
    elif can3 > can1 and can3 > can2:
        winner = can3name

    #tallying candidate percentagers of total. {0:.3%} is limiting decimal to 3 places to align with prompt
    can1percent = "{0:.3%}".format(can1 / totalvote)

    can2percent = "{0:.3%}".format(can2 / totalvote)

    can3percent = "{0:.3%}".format(can3 / totalvote)
    
    #print results to terminal
    print("Election Results")
    print("---------------------------")
    print("Total Votes:", totalvote)
    print("---------------------------")

    print(f'{can1name}: {can1percent} ({can1})')
    print(f'{can2name}: {can2percent} ({can2})')
    print(f'{can3name}: {can3percent} ({can3})')
    print("---------------------------")
    print("Winner: ", winner)
    print("---------------------------")


poll_results = os.path.join("analysis", "poll_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(poll_results, 'w') as txtfile:
    print("Election Results", file=txtfile)
    print("---------------------------", file=txtfile)
    print("Total Votes:", totalvote, file=txtfile)
    print("---------------------------", file=txtfile)
    print(f'{can1name}: {can1percent} ({can1})', file=txtfile)
    print(f'{can2name}: {can2percent} ({can2})', file=txtfile)
    print(f'{can3name}: {can3percent} ({can3})', file=txtfile)
    print("---------------------------", file=txtfile)
    print("Winner: ", winner, file=txtfile)
    print("---------------------------", file=txtfile)


    
    
    





