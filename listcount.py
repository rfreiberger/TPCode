#!/usr/bin/env python3

a = [1, 6, 2, 3, 5, 1, 4, 1, 2, 4]

def countitems(mylist):

    print("Starting count")

    countdict = {}

    for items in mylist:
 
        if items in countdict:

            countdict[items] =  (countdict[items] + 1)

        else:

            countdict[items] = 1

    for name in sorted(countdict):
        print("Number: " + str(name) + " Count: " + str(countdict[name]))
        
    print("Completed count")

countitems(a)