import csv
import os
import sys
import string

#""" Get the csv file as input """"
f1 = input("Enter the csv filename for election results analysis: ")

def pypoll_main(f1):
    
    votes_sum = 0
    rows_list = []
    list_candidates = []
    dict_candidates = {}

    with open(f1, newline='') as csvfile:           # read input file
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            rows_list.append(row)   # get all rows in a list

    del(rows_list[0])               # delete header row           
    
    # create list of unique candidates while dropping ones with no votes.
    for row in rows_list:
        if (row[2] not in list_candidates and row[0] != ""):    # go to next row if voter ID is Nil
            list_candidates.append(row[2])
    
    # create a dictionary of format 'candidate : votes' from list
    dict_candidates = {candidate:0 for candidate in list_candidates}

    # Fill in the dictionary with votes to each candidate
    for row in rows_list:
        if (row[0] != ""):           # go to next row if voter ID is Nil
            for key in dict_candidates:
                if key == row[2]:
                    dict_candidates[key] += 1  # add votes for each candidate

    #print(dict_candidates)
    
    votes_sum = sum(dict_candidates.values())

    # Open the file to write required information

    file = open("PyPoll_election_analysis.txt", "w")
    file.write("Election Results " + "\n")
    file.write("-------------------------------" + "\n")
    file.write("Total votes: " + str(votes_sum) + "\n")
    for key in dict_candidates:
         file.write(key + ": " + "{0:.1f}%".format((dict_candidates[key]/votes_sum)*100) + "(" + str(dict_candidates[key])  + ")" + "\n")
    file.write("-------------------------------" + "\n")
    file.write("Winner: " + max(dict_candidates, key=dict_candidates.get) + "\n")
    file.write("-------------------------------" + "\n")

    file.close()

    file = open("PyPoll_election_analysis.txt", "r")
    for line in file:
        print(line)

    file.close()
    
pypoll_main(f1)