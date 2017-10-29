import os
import csv
import sys
import string

#""" Get the csv file as input """"
f1 = input("Enter the csv filename for revenue analysis: ")

def pybank_main(f1):

    mkey = []                               # declarations / initiations
    rev_list = []
    rev_diff = []
    months = 0
    total_revenue = 0 

    with open(f1) as revdata:
        mydict = dict(csv.reader(revdata))  # dictionary from data
        mydict.pop('Date', None)            # delete headers

    for key, value in mydict.items():       # compute total revenue
        months += 1                         # and months
        rev_list.append(int(value))         # create list of revenues
        total_revenue = total_revenue + int(value)
    
    for i in range(1, len(rev_list)):       # create list of month to month changee
        rev_diff.append(rev_list[i] - rev_list[i-1])
    
    k_list = list(mydict.keys())            # list of keys or months
    maxval = max(rev_diff)                  # max month to month revenue change
    minval = min(rev_diff)                  # min month to month revenue change
    
    indx_max = rev_diff.index(max(rev_diff))
    indx_min = rev_diff.index(min(rev_diff))
    indx_max += 1   # adjustment for rev_diff list index starting from 0 (as csv from 1 after headers removed)
    indx_min += 1   # same as comment for indx_min
    key_maxval = k_list[indx_max]           # key i.e.month of max revenue
    key_minval = k_list[indx_min]           # key i.e.month of min revenue

    file = open("PyBank_revenue_analysis2.txt", "w")     # create/open output file, and write results

    file.write("\nTotal months: " + str(months) + "\n")   
    file.write("Total revenue: $" + str(total_revenue) + "\n")
    file.write("Average revenue change/month: $" + str(round(sum(rev_diff)/(len(rev_list)-1),2)) + "\n")
    file.write("Greatest increase in revenue (date & amount): " + key_maxval + " ($" + str(maxval) + ") \n")
    file.write("Greatest decrease in revenue (date & amount): " + key_minval + " ($" + str(minval) + ") \n")

    file.close()

    file = open("PyBank_revenue_analysis2.txt", "r")     # print to screen from output file
    for line in file:
        print(line)

    file.close()

pybank_main(f1)
