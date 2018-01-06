#!/usr/bin/env python3

import random

newlist = [random.randint(0,101) for r in range(50)]

def bubblesort(mylist):

	print("Starting sort on following random list: ")
	print(newlist)

	for outloop in range(0, len(mylist) -1, 1):

		for inloop in range(0, len(mylist) -1, 1):

			if mylist[inloop] > mylist[inloop + 1]:

				temp = mylist[inloop]
				mylist[inloop] = mylist[inloop + 1]
				mylist[inloop + 1] = temp

	print("Completed sort")
	print(newlist)


bubblesort(newlist)

